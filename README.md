# 🚀 Blockchain Private Network (Clique PoA)

**Setup Guide — genesis.json & Node Configuration**
Kelas B · SKT · Clique PoA · Geth v1.13.15

---

## 1. 🌐 Overview Jaringan

Jaringan menggunakan **Clique Proof-of-Authority (PoA)** dengan 4 validator node.

| Node      | Kelompok | Universitas      | IP Address    | P2P Port | RPC Port |
| --------- | -------- | ---------------- | ------------- | -------- | -------- |
| VM-1 (K1) | Syifani  | Univ. Diponegoro | 10.34.100.182 | 30303    | 8545     |
| VM-2 (K2) | Rafly    | IPB University   | 10.34.100.183 | 30303    | 8545     |
| VM-3 (K3) | Asyraf   | Univ. Brawijaya  | 10.34.100.184 | 30303    | 8545     |
| VM-4 (K4) | Wahyu    | Univ. Hasanuddin | 10.34.100.185 | 30303    | 8545     |

⚠ Minimal **3 dari 4 validator aktif** agar blok bisa diproduksi.

---

## 2. ⚙️ Instalasi Geth (Semua VM)

### Download & Install

```bash
wget https://gethstore.blob.core.windows.net/builds/geth-linux-amd64-1.13.15-c5ba367e.tar.gz

tar -xvf geth-linux-amd64-1.13.15-c5ba367e.tar.gz

sudo mv geth-linux-amd64-1.13.15-c5ba367e/geth /usr/local/bin/

echo 'export PATH=/usr/local/bin:$PATH' >> ~/.bashrc
source ~/.bashrc

geth version
```

✅ Pastikan semua VM pakai versi **1.13.15**

---

## 3. 👤 Buat Akun Validator

### Setup Direktori

```bash
mkdir -p ~/blockchain/geth
cd ~/blockchain
```

### Generate Account

```bash
geth account new --datadir ./geth
```

⚠ Simpan:

* Address (0x...)
* Password

### Backup Keystore

```bash
ls ~/blockchain/geth/keystore/

cp -r ~/blockchain/geth/keystore/ ~/keystore_backup/
```

⛔ Jangan hapus keystore!

---

## 4. 🧩 Konfigurasi genesis.json (VM-1)

### Format extradata

```
0x
+ 64 hex (zeros)
+ 40 hex (ADDR K1)
+ 40 hex (ADDR K2)
+ 40 hex (ADDR K3)
+ 40 hex (ADDR K4)
+ 130 hex (zeros)
```

✅ Total panjang: **356 karakter**

---

### Template genesis.json

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
  "extradata": "0x...",
  "alloc": {
    "addr1": { "balance": "1000000000000000000000" },
    "addr2": { "balance": "1000000000000000000000" },
    "addr3": { "balance": "1000000000000000000000" },
    "addr4": { "balance": "1000000000000000000000" }
  }
}
```

---

### Validasi extradata

```bash
python3 -c "
extradata = '0x...'
print(len(extradata))
print(len(extradata) == 356)
"
```

---

## 5. 🔗 Inisialisasi Chain

```bash
cp genesis.json ~/blockchain/genesis.json

cd ~/blockchain

geth init --datadir ./geth genesis.json
```

⚠ Semua VM HARUS pakai file yang sama persis

---

## 6. ▶️ Menjalankan Node

### VM-1 (Bootnode)

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

### Ambil enode

```bash
admin.nodeInfo.enode
```

---

### VM-2,3,4

```bash
geth \
--datadir ~/blockchain/geth \
--networkid 20260315 \
--port 30303 \
--bootnodes <ENODE_VM1> \
--http \
--http.addr 0.0.0.0 \
--http.port 8545 \
--http.api eth,net,web3,clique,personal \
--http.corsdomain '*' \
--unlock <ADDR_KX> \
--password ~/blockchain/password.txt \
--mine \
--miner.etherbase <ADDR_KX> \
--allow-insecure-unlock \
console
```

---

## 7. ✅ Verifikasi Jaringan

### Cek Peer

```bash
net.peerCount
```

➡️ Harus = 3

### Cek Validator

```bash
clique.getSigners()
```

### Cek Block

```bash
eth.blockNumber
```

➡️ Harus terus bertambah

---

## 8. 🛠 Troubleshooting

| Problem           | Solusi                 |
| ----------------- | ---------------------- |
| peerCount = 0     | Cek port 30303 & enode |
| blok tidak jalan  | minimal 3 node aktif   |
| genesis mismatch  | init ulang             |
| account locked    | cek password           |
| extradata invalid | panjang harus 356      |

---

## 🔁 Urutan Eksekusi

1. Install Geth
2. Buat account
3. Kirim address ke VM-1
4. Buat genesis.json
5. Init semua VM
6. Start VM-1
7. Start VM lain
8. Verifikasi jaringan

---

📄 Sumber dokumen: 
