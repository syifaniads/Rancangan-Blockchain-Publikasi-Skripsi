# Source Evidence

This portfolio separates the **upstream assignment specification** from the **student implementation evidence**.

## 1. Upstream lecturer specification

Primary assignment source:

https://github.com/3k0sakti/SKT/blob/main/case/case-B.md

The lecturer-provided case defines the overall class-wide design:

- 4 groups working together on one network;
- one validator VM per group;
- consortium/private Ethereum using Geth + Clique PoA;
- the academic repositories assigned to each group;
- the responsibility split between groups;
- shared network/bootstrap workflow;
- smart-contract, REST API, plagiarism, and IPFS components;
- operational and failure-testing scenarios.

It also names **Syifani Adillah Salsabila** as the Group 1 PIC and assigns Group 1 the responsibility to create/distribute `genesis.json` and coordinate the initial network setup.

This source is the **design/specification provenance**. The personal portfolio does not claim the course architecture itself was independently authored by the student team.

## 2. Group 1 implementation repository

https://github.com/syifaniads/Rancangan-Blockchain-Publikasi-Skripsi

The pre-portfolio state preserved:

- the Group 1 network setup guide;
- the `genesis.json` used for the lab network.

The repository has since been reorganized as a recruiter-facing case study while preserving the original chain artifact.

## 3. Final implementation report

The 2026 course report is:

**Blockchain Private Network - Sistem Komputasi Terdistribusi B**

It documents actual implementation / operation evidence such as:

- Geth v1.13.15 installation;
- validator-account creation;
- Clique genesis construction;
- `extradata` verification;
- chain initialization;
- P2P bootstrapping;
- peer/signer/block-number checks;
- backend API startup;
- publication metadata crawling / ingestion;
- IPFS upload;
- blockchain transaction submission;
- post-submit block-height observation;
- publication-record lookup.

The report therefore acts as **execution evidence**, while the lecturer case acts as **assignment/design evidence**.

## Why the raw report is not committed

The raw report includes course-lab infrastructure addresses and a sample validator password. Those values are unnecessary for recruiter review and should not be duplicated in a public portfolio repository.

The portfolio preserves the engineering facts while sanitizing operational details.

## Retained chain artifact

[`genesis.json`](./genesis.json) is retained as an original Group 1 lab artifact. It contains the four public validator addresses encoded into the Clique signer configuration.

Public addresses are not private keys. No validator keystore/private key is stored in this repository.

## Reusable sanitized artifact

[`genesis.example.json`](./genesis.example.json) demonstrates the same configuration structure using placeholders rather than real lab validator addresses.

## Responsibility evidence from the lecturer case

The upstream specification assigns:

| Group | Primary responsibility |
|---|---|
| Group 1 / Syifani | Create + distribute `genesis.json`; coordinate initial setup |
| Group 2 | Configure and deploy smart contract |
| Group 3 | Build REST API + plagiarism engine |
| Group 4 | Build OAI-PMH crawler + IPFS storage pipeline |

All groups also operate their own validator, submit records from the assigned university source, and participate in consensus.

This responsibility split is important when interpreting portfolio claims: the full application is a **class-wide integration**, not a single-group implementation.

## Evidence caveat

The final report includes more than one intermediate genesis/topology state. A later example contains an additional address while other sections continue to describe a four-validator network.

For portfolio clarity:

- the retained repository `genesis.json` is treated as the reference Group 1 chain artifact;
- report screenshots are treated as historical experiment evidence;
- the upstream lecturer case is treated as the intended class topology;
- the portfolio does not claim every report page represents the exact same network state.

## Source-code preservation caveat

The report demonstrates backend/crawler/IPFS/registry integration, but the complete source for every class-wide component is not preserved inside this Group 1 repository.

That is expected because the lecturer specification distributed component ownership across multiple groups. This portfolio documents the demonstrated integrated workflow and avoids fabricating missing source code.
