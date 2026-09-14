# Limitations and Non-Claims

## 1. Academic lab scale

The network is a small multi-VM consortium experiment. It does not establish performance, governance, or failure behavior at production consortium scale.

## 2. Clique PoA is a legacy-style lab choice

The project uses the Clique PoA mechanism supported by the selected Geth version in the coursework environment. This repository documents the historical project architecture; it is not a recommendation that every new production consortium should choose the same stack.

## 3. Validator topology changed during experimentation

The final report contains evidence from multiple intermediate configurations. Some sections describe four validators while a later genesis example includes an additional address.

The retained repository `genesis.json` defines four validators and is treated as the portfolio reference artifact. The report should not be interpreted as one perfectly frozen topology across every screenshot.

## 4. No production key management

The coursework demonstrates validator-account creation and unlocking, but does not implement HSM/KMS-grade key custody.

## 5. Lab RPC settings

Some original commands use permissive RPC/CORS and insecure-unlock options to simplify the controlled exercise. Those settings are explicitly not presented as production best practice.

## 6. Smart-contract implementation is not fully preserved here

The report demonstrates publication submission and query behavior, but this repository does not currently contain the complete original backend / smart-contract implementation.

The portfolio therefore documents the verified workflow rather than fabricating missing source files.

## 7. Block-height growth is not enough for application confirmation

The report observes block-number growth around submissions. In production, transaction success should be determined from transaction receipts, status, and an explicit confirmation policy.

## 8. IPFS durability requires pinning / governance

A CID is content-addressed, but availability is not automatic. Production use requires reliable pinning, replication, retention, and deletion policies.

## 9. Privacy / legal governance

Academic publications can contain personal information. A real cross-university registry would need explicit governance for consent, retention, correction, takedown, and access control.

## 10. Collaborative authorship

This was a six-person team project. The personal portfolio does not claim sole authorship of every implementation component.
