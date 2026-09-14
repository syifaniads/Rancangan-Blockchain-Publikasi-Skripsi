# Source Evidence

## Primary repository

This repository is the original project repository used for the academic exercise:

https://github.com/syifaniads/Rancangan-Blockchain-Publikasi-Skripsi

The pre-portfolio state contained the original network setup guide and `genesis.json` artifact.

## Final course report

The portfolio was also reconstructed from the 2026 course report:

**Blockchain Private Network - Sistem Komputasi Terdistribusi B**

The report documents:

- a Clique PoA private network across multiple validator VMs;
- Geth v1.13.15;
- validator-account creation;
- genesis construction;
- `extradata` verification;
- chain initialization;
- P2P bootstrapping;
- peer/signer/block-number checks;
- backend API startup;
- thesis/publication crawling;
- IPFS upload;
- blockchain transaction submission;
- post-submit block-height observation;
- publication-record lookup.

## Why the raw report is not committed

The raw report includes course-lab infrastructure addresses and a sample validator password. Those values are unnecessary for recruiter review and should not be duplicated in a public portfolio repository.

The portfolio therefore preserves the engineering facts while sanitizing operational details.

## Retained chain artifact

[`genesis.json`](./genesis.json) is retained as an original lab artifact. It contains the four public validator addresses encoded into the Clique signer configuration.

Public addresses are not private keys. No validator keystore/private key is stored in this repository.

## Reusable sanitized artifact

[`genesis.example.json`](./genesis.example.json) demonstrates the same configuration structure using placeholders rather than real lab validator addresses.

## Evidence caveat

The final report includes more than one intermediate genesis/topology state. A later example contains an additional address while other sections continue to describe a four-validator network.

For portfolio clarity:

- the retained repository `genesis.json` is treated as the reference chain artifact;
- report screenshots are treated as historical experiment evidence;
- the portfolio does not claim every report page represents the exact same network state.

## Missing original source

The report demonstrates backend/crawler/IPFS/registry integration, but the complete original backend and smart-contract source are not currently present in this GitHub repository.

This portfolio documents the demonstrated workflow and explicitly avoids fabricating source code that is not preserved here.
