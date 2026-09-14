# Private Network and Clique PoA

## Network model

The academic lab uses a small permissioned Ethereum-compatible network built with **Geth v1.13.15** and **Clique Proof-of-Authority (PoA)**.

The retained genesis artifact defines four validator addresses.

## Why PoA

For a controlled consortium-style network, authority-based validation is useful because:

- validators are known participants;
- no proof-of-work mining competition is required;
- block production is predictable;
- governance can be tied to institutional identities.

This is appropriate for an academic consortium experiment, but it changes the trust model: security depends heavily on validator governance and key custody.

## Genesis configuration

The project configuration uses:

```text
chainId      = 20260315
period       = 5 seconds
epoch        = 30000
difficulty   = 1
gasLimit     = 8000000
```

Clique encodes the initial signer set inside the `extradata` field.

Conceptually:

```text
32-byte vanity
+ validator address 1
+ validator address 2
+ validator address 3
+ validator address 4
+ 65-byte signature placeholder
```

For four validators, the expected encoded string length is checked before initialization.

## Node initialization

All validators must initialize using the exact same genesis state:

```bash
geth init --datadir <NODE_DATA_DIR> genesis.json
```

If nodes use different genesis files, they belong to different chains even if their network ports can reach each other.

## Peer bootstrap

One node can provide an `enode://...` identity used by the other validators as a bootstrap peer.

The public portfolio intentionally does not publish the course-lab enode or internal addresses. Use placeholders such as:

```text
enode://<BOOTNODE_PUBLIC_KEY>@<VALIDATOR_HOST>:30303
```

## Operational validation

The report verifies several properties from the Geth console:

### Peer connectivity

```text
net.peerCount
```

The expected value depends on topology. In a fully connected four-node network, each node sees three other peers.

### Active signer set

```text
clique.getSigners()
```

This confirms the validator addresses recognized by Clique.

### Block production

```text
eth.blockNumber
```

The value should continue increasing while the validator network is healthy.

## Configuration evolution note

The course report contains screenshots/text from more than one intermediate configuration, including a later genesis example with an additional address while other sections still describe four validators.

The repository therefore treats the retained four-validator `genesis.json` as the **portfolio reference artifact** and does not claim every screenshot in the report belongs to one identical final topology.

## Production considerations

A production permissioned chain should additionally define:

- validator onboarding/removal governance;
- HSM or secure key custody;
- encrypted and authenticated RPC access;
- network segmentation / firewall rules;
- backup and disaster recovery;
- node and consensus monitoring;
- contract deployment / upgrade governance;
- incident response for a compromised validator.
