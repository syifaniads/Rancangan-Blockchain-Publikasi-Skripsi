# Portfolio Summary

## 30-second recruiter summary

**Private Blockchain for Academic Publication Registry** is a collaborative distributed-systems project that deploys a permissioned Ethereum-compatible network across multiple validator VMs using Geth and Clique Proof-of-Authority.

The project connects the validator network to an application workflow that crawls thesis/publication metadata, stores an artifact in IPFS, submits registry transactions through a backend API, and verifies the stored publication record.

## Technical highlights

- Geth v1.13.15
- private Ethereum-compatible network
- Clique Proof-of-Authority
- multi-VM validator/full-node topology
- shared genesis configuration and signer set
- P2P peer bootstrap / verification
- IPFS content-addressed storage
- backend transaction submission
- publication metadata ingestion / crawler
- chain-state verification
- security analysis of lab vs production RPC configuration

## CV-ready version

> **Private Blockchain for Academic Publication Registry** - Built and validated a multi-validator private Ethereum network using Geth and Clique PoA, including shared genesis configuration, P2P peering and block-production verification. Integrated an academic-publication workflow with metadata ingestion, IPFS content addressing, backend transaction submission and blockchain-backed record verification.

## Short portfolio-card version

> Permissioned blockchain prototype for cross-institution academic-publication registration using Geth, Clique PoA, IPFS and a backend API across multiple validator VMs.

## Interview talking points

1. **Why a shared genesis matters** - every node must agree on chain ID, signer set and genesis state.
2. **Why PoA fits the experiment** - validators represent known consortium members rather than anonymous miners.
3. **What makes peering a distributed-systems concern** - reachable nodes can still fail to join correctly if chain identity or bootstrap configuration differs.
4. **Why IPFS is separate from chain state** - keep large content off-chain while storing integrity/reference metadata on-chain.
5. **How writes were validated** - transaction submission, ongoing block production and record lookup were checked in the lab.
6. **What was unsafe in the lab setup** - broad RPC exposure, permissive CORS and insecure account unlocking are lab conveniences, not production defaults.
7. **What production needs** - secure validator key custody, authenticated RPC, governance, transaction idempotency, observability and durable IPFS pinning.

## Suggested tags

`Blockchain` · `Ethereum` · `Geth` · `Clique PoA` · `IPFS` · `Distributed Systems` · `P2P Networking` · `Node.js` · `Smart Contracts` · `Backend API`
