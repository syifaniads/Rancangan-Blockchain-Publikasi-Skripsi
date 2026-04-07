# BLOCKCHAIN PRIVATE NETWORK

## Setup Guide — genesis.json & Node Configuration

### Kelas B · SKT · Clique PoA · Geth v1.13.15

Dokumen ini berisi panduan lengkap step-by-step untuk setup genesis block, instalasi Geth, konfigurasi node, dan menjalankan jaringan blockchain private consortium untuk proyek skripsi plagiasi.

## 1. Overview Jaringan

Jaringan ini menggunakan Clique Proof-of-Authority (PoA) dengan 4 validator node yang merepresentasikan 4 universitas berbeda. Setiap VM bertindak sebagai full node sekaligus validator.

| Node      | Kelompok     | Universitas      | IP Address    | Port P2P | Port RPC |
| --------- | ------------ | ---------------- | ------------- | -------- | -------- |
| VM-1 (K1) | K1 – Syifani | Univ. Diponegoro | 10.34.100.182 | 30303    | 8545     |
| VM-2 (K2) | K2 – Rafly   | IPB University   | 10.34.100.183 | 30303    | 8545     |
| VM-3 (K3) | K3 – Asyraf  | Univ. Brawijaya  | 10.34.100.184 | 30303    | 8545     |
| VM-4 (K4) | K4 – Wahyu   | Univ. Hasanuddin | 10.34.100.185 | 30303    | 8545     |

⚠ Semua 4 node adalah validator. Clique PoA membutuhkan majority (>50%) validator aktif untuk memproduksi blok — minimal 3 dari 4 node harus online.

## 2. Instalasi Geth (Semua VM)

Jalankan perintah berikut di SEMUA VM (VM-1, VM-2, VM-3, VM-4) sebelum melakukan konfigurasi apapun.

### STEP 2.1    Download & Install Geth v1.13.15

```bash
# Download binary Geth v1.13.15
wget https://gethstore.blob.core.windows.net/builds/geth-linux-amd64-1.13.15-c5ba367e.tar.gz

# Ekstrak archive
tar -xvf geth-linux-amd64-1.13.15-c5ba367e.tar.gz

# Pindahkan ke system PATH
sudo mv geth-linux-amd64-1.13.15-c5ba367e/geth /usr/local/bin/

# Tambahkan ke PATH (jika belum ada)
echo 'export PATH=/usr/local/bin:$PATH' >> ~/.bashrc
source ~/.bashrc

# Verifikasi — harus muncul: 1.13.15
geth version
```

⚠ Pastikan SEMUA VM menggunakan versi yang sama persis (v1.13.15). Perbedaan versi dapat menyebabkan gagal peering.

## 3. Buat Akun Validator (Semua VM)

Setiap VM harus membuat akun Ethereum sendiri. Akun ini akan menjadi identity validator node di jaringan.

### STEP 3.1    Buat Struktur Direktori

```bash
# Buat direktori kerja
mkdir -p ~/blockchain/geth
cd ~/blockchain
```

### STEP 3.2    Generate Akun Validator

```bash
# Buat akun baru — akan diminta membuat password
geth account new --datadir ./geth
```

# Output contoh:

# Your new key was generated

# Public address of the key: 0xAbCd1234...

# Path of the secret key file: ./geth/keystore/UTC--...

⚠ Catat address yang muncul (0x...) dan simpan password dengan aman. Address ini akan dikirim ke genesis owner (VM-1).
✓ Setiap VM mengirimkan address mereka ke K1 (Syifani/VM-1) untuk dimasukkan ke genesis.json

### STEP 3.3    Backup Keystore (WAJIB)

```bash
# Lokasi file keystore
ls ~/blockchain/geth/keystore/

# Backup ke lokasi aman
cp -r ~/blockchain/geth/keystore/ ~/keystore_backup/
```

⛔ JANGAN HAPUS KEYSTORE — File keystore adalah identitas validator. Jika terhapus, address hangus dan genesis harus dibuat ulang dari awal.

## 4. Konfigurasi genesis.json (VM-1 / Genesis Owner)

Bagian ini HANYA dilakukan oleh VM-1 setelah menerima address dari semua VM lain.

### STEP 4.1    Kumpulkan 4 Address Validator

Sebelum membuat genesis.json, pastikan sudah menerima address dari semua node:

• VM-1 (K1): address milik sendiri dari Step 3.2
• VM-2 (K2): address dari Rafly
• VM-3 (K3): address dari Asyraf
• VM-4 (K4): address dari Wahyu

### STEP 4.2    Format extradata

extradata adalah field kritis di Clique PoA yang mendefinisikan siapa saja validatornya. Format HARUS tepat:

```
# Struktur extradata:
0x
  + 64 hex chars  (32 bytes zeros — prefix wajib)
  + 40 hex chars  (address K1, tanpa 0x prefix)
  + 40 hex chars  (address K2, tanpa 0x prefix)
  + 40 hex chars  (address K3, tanpa 0x prefix)
  + 40 hex chars  (address K4, tanpa 0x prefix)
  + 130 hex chars (65 bytes zeros — signature placeholder)

# Total panjang string: 2 + 64 + (40x4) + 130 = 356 karakter
```

⚠ Hapus 0x dari setiap address saat memasukkan ke extradata. Jangan beri spasi atau koma antar address.

### STEP 4.3    genesis.json Lengkap

```json
{
  "config": {
    "chainId": 20260315,
    "homesteadBlock": 0,
    "eip150Block": 0,
    "eip155Block": 0,
    "eip158Block": 0,
    "byzantiumBlock": 0,
    "constantinopleBlock": 0,
    "petersburgBlock": 0,
    "istanbulBlock": 0,
    "clique": {
      "period": 5,
      "epoch": 30000
    }
  },
  "difficulty": "1",
  "gasLimit": "8000000",
  "extradata": "0x[64_zeros][ADDR_K1_no_0x][ADDR_K2_no_0x][ADDR_K3_no_0x][ADDR_K4_no_0x][130_zeros]",
  "alloc": {
    "addr_k1_lowercase_no_0x": { "balance": "1000000000000000000000" },
    "addr_k2_lowercase_no_0x": { "balance": "1000000000000000000000" },
    "addr_k3_lowercase_no_0x": { "balance": "1000000000000000000000" },
    "addr_k4_lowercase_no_0x": { "balance": "1000000000000000000000" }
  }
}
```

⚠ Balance 1000000000000000000000 = 1000 ETH dalam satuan wei. Ini hanya berlaku di jaringan private ini.

### STEP 4.4    Verifikasi extradata (Penting!)

```bash
python3 -c "
extradata = '0x...'
total = len(extradata)
print(f'Panjang: {total} karakter')
print(f'Valid: {total == 356}')
"
```

✓ Jika output: Valid: True — genesis.json siap didistribusikan

## 5. Inisialisasi Chain (Semua VM)

Setelah VM-1 mendistribusikan genesis.json, SEMUA VM menjalankan langkah ini.

### STEP 5.1    Terima & Simpan genesis.json

```bash
cp genesis.json ~/blockchain/genesis.json
```

### STEP 5.2    Init Geth dengan Genesis Block

```bash
cd ~/blockchain

geth init --datadir ./geth genesis.json
```

# Output sukses akan muncul:

# INFO Successfully wrote genesis state

# INFO database=chaindata

⛔ KRITIS: Semua VM HARUS menggunakan file genesis.json yang PERSIS SAMA. Satu karakter berbeda = chain berbeda = tidak bisa peering.

## 6. Menjalankan Node

### STEP 6.1    Start VM-1 Terlebih Dahulu (Bootnode)

```bash
geth \
  --datadir ~/blockchain/geth \
  --networkid 20260315 \
  --port 30303 \
  --http \
  --http.addr 0.0.0.0 \
  --http.port 8545 \
  --http.api eth,net,web3,clique,personal \
  --http.corsdomain '*' \
  --unlock <ADDR_K1> \
  --password ~/blockchain/password.txt \
  --mine \
  --miner.etherbase <ADDR_K1> \
  --allow-insecure-unlock \
  console
```

### STEP 6.2    Ambil enode URL dari VM-1

```bash
admin.nodeInfo.enode
```

# Output contoh:

# enode://abc123...@10.34.100.182:30303

Salin enode URL ini dan kirimkan ke VM-2, VM-3, dan VM-4.

### STEP 6.3    Start VM-2, VM-3, VM-4

```bash
geth \
  --datadir ~/blockchain/geth \
  --networkid 20260315 \
  --port 30303 \
  --nat extip:<IP_PEER> \
  --bootnodes "enode://bcd9fa2aeb705101bc15d6ecca3363cf8e555f742203e612f3f02ac1c13749a9925c71116b8a95e03a064affd1a0a61979b38d735d357cc38656bb6f6a0012da@10.34.100.182:30303" \
  --http \
  --http.addr 0.0.0.0 \
  --http.port 8545 \
  --http.api eth,net,web3,admin,clique,miner,personal \
  --http.corsdomain "*" \
  --mine \
  --miner.etherbase <ADDR_PEER> \
  --unlock <ADDR_PEER> \
  --password ~/blockchain/password.txt \
  --allow-insecure-unlock \
  --verbosity 3 \
  console
```

## 7. Verifikasi Jaringan

Setelah semua node berjalan, lakukan verifikasi berikut di setiap VM:

### STEP 7.1    Cek Jumlah Peer

```bash
net.peerCount
```

# Harus menampilkan: 3

# (setiap node terhubung ke 3 node lainnya)

### STEP 7.2    Cek Status Validator

```bash
clique.getSigners()
```

# Harus menampilkan 4 address validator

```bash
eth.blockNumber
```

# Angka harus terus bertambah (setiap ~5 detik)

### STEP 7.3    Checklist Final

✓ net.peerCount == 3 di semua VM
✓ clique.getSigners() menampilkan 4 address
✓ eth.blockNumber terus bertambah
✓ Tidak ada error di log geth

## 8. Troubleshooting

| Problem                 | Solusi                                                                                                     |
| ----------------------- | ---------------------------------------------------------------------------------------------------------- |
| net.peerCount == 0      | Cek firewall port 30303. Pastikan bootnodes enode URL benar. Coba tambah peer manual: admin.addPeer(enode) |
| Blok tidak bertambah    | Minimal 3 dari 4 validator harus online. Cek apakah --mine aktif dan akun ter-unlock.                      |
| Error: genesis mismatch | Salah satu VM punya genesis.json berbeda. Hapus chaindata dan init ulang dengan genesis yang benar.        |
| Error: account locked   | Pastikan file password.txt ada dan berisi password yang benar. Cek path --password.                        |
| extradata invalid       | Hitung ulang panjang extradata. Harus 356 karakter. Pastikan trailing zeros = 130 hex chars.               |

## Urutan Eksekusi Ringkas

1. Install Geth v1.13.15 di semua VM
2. Setiap VM: geth account new → kirim address ke VM-1
3. VM-1: buat genesis.json dengan 4 address → distribusikan
4. Semua VM: geth init --datadir ./geth genesis.json
5. VM-1 start geth → ambil enode URL → kirim ke VM-2,3,4
6. VM-2,3,4 start geth dengan --bootnodes enode VM-1
7. Verifikasi: net.peerCount == 3, eth.blockNumber bertambah
