# Portfolio Summary

## 30-second recruiter summary

**Private Blockchain for Academic Publication Registry** is a class-wide distributed-systems project based on a lecturer-provided specification for a four-validator consortium network using Geth and Clique Proof-of-Authority.

**Syifani's role:** Group 1 PIC / VM-1 coordination. The upstream assignment assigns Group 1 responsibility for creating and distributing the shared `genesis.json` and coordinating the initial network setup. Group 1 also operated its validator, submitted publication data from the assigned Undip repository, joined consensus, and participated in end-to-end integration/testing of the shared class system.

The wider class integration connected the validator network to smart-contract registration, REST/API processing, plagiarism-related workflow, and IPFS-backed content handling, with component ownership distributed across the four groups.

## Technical highlights

- Geth v1.13.15
- private Ethereum-compatible consortium network
- Clique Proof-of-Authority
- four-group / multi-VM validator topology
- shared genesis configuration and signer set
- P2P peer bootstrap / verification
- validator / block-production checks
- IPFS content-addressed storage in the class-wide workflow
- backend transaction submission in the integrated system
- academic publication ingestion from university repositories
- chain-state / record verification
- security analysis of lab vs production RPC configuration

## CV-ready version

> **Private Blockchain for Academic Publication Registry** — Served as Group 1 PIC in a class-wide four-validator Ethereum consortium project using Geth and Clique PoA. Coordinated shared genesis/bootstrap setup, operated the Group 1 validator, validated P2P peering and block production, and participated in end-to-end publication-registry integration using shared smart-contract, API and IPFS components.

## Short portfolio-card version

> Four-validator private Ethereum consortium for academic-publication registration. Led Group 1's genesis/bootstrap setup and validator operation, then participated in class-wide integration and verification across Geth, Clique PoA, API, smart-contract and IPFS components.

## Important provenance note

The overall architecture and group responsibility split came from the lecturer's assignment specification:

https://github.com/3k0sakti/SKT/blob/main/case/case-B.md

The portfolio therefore distinguishes **course design provenance** from **student implementation and operational evidence**.

## Interview talking points

1. **Why a shared genesis matters** — every node must agree on chain ID, signer set and genesis state.
2. **Why Group 1 had coordination responsibility** — VM-1 distributed the shared genesis/bootstrap configuration used by the other groups.
3. **Why PoA fits the experiment** — validators represent known consortium members rather than anonymous miners.
4. **What makes peering a distributed-systems concern** — reachable nodes can still fail to join correctly if chain identity or bootstrap configuration differs.
5. **How class-wide component ownership worked** — Group 2 handled smart contract deployment, Group 3 the REST API/plagiarism engine, and Group 4 the OAI-PMH/IPFS pipeline, while all groups operated validators and integrated the full workflow.
6. **Why IPFS is separate from chain state** — keep large content off-chain while storing integrity/reference metadata on-chain.
7. **How writes were validated** — transaction submission, ongoing block production and record lookup were checked in the lab.
8. **What was unsafe in the lab setup** — broad RPC exposure, permissive CORS and insecure account unlocking are lab conveniences, not production defaults.
9. **What production needs** — secure validator key custody, authenticated RPC, governance, transaction idempotency, observability and durable IPFS pinning.

## Suggested tags

`Blockchain` · `Ethereum` · `Geth` · `Clique PoA` · `IPFS` · `Distributed Systems` · `P2P Networking` · `Consensus` · `Smart Contracts` · `Backend Integration`
