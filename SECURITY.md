# Security Notes

This is a public portfolio reconstruction of an academic private-blockchain lab.

## Sanitization policy

The recruiter-facing documentation intentionally removes:

- course-lab private IP addresses;
- bootnode/enode identifiers;
- validator passwords;
- local filesystem paths tied to the original environment;
- any keystore/private-key material.

Public validator addresses in the retained `genesis.json` are not secret keys, but private keys and keystore files must never be committed.

## Lab commands are not production defaults

The original coursework used permissive settings to simplify a controlled lab. Production systems should avoid exposing configurations such as:

```text
--http.addr 0.0.0.0
--http.corsdomain '*'
--allow-insecure-unlock
broad personal/admin RPC exposure
plaintext password files
```

## Recommended production controls

### Validator identity

- use dedicated validator identities;
- protect keys with HSM/KMS or equivalent secure custody;
- rotate / revoke compromised identities through consortium governance;
- never share keystores between nodes.

### RPC boundary

- bind RPC to private interfaces or localhost where possible;
- place authenticated gateways in front of application-facing RPC;
- expose only required RPC modules;
- enforce TLS and network ACLs;
- rate-limit application clients.

### P2P network

- firewall P2P ports to approved peers where appropriate;
- monitor peer churn and unexpected nodes;
- use static/trusted peer configuration for a permissioned deployment.

### Application layer

- authenticate write APIs;
- authorize institution-specific actions;
- make transaction submission idempotent;
- validate transaction receipts;
- protect crawler inputs and external URLs;
- validate IPFS CID and content hash relationships.

### Smart-contract / registry layer

- restrict registry writes to authorized identities;
- define record update/revocation semantics;
- audit contract events;
- test duplicate submissions and malformed records.

## Responsible use

The repository is intended for academic and portfolio purposes. Do not reuse lab credentials or expose Ethereum RPC endpoints to untrusted networks.
