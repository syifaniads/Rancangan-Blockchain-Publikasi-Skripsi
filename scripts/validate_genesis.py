#!/usr/bin/env python3
"""Validate retained Clique PoA genesis invariants for the portfolio lab.

This checks structural consistency of the sanitized/retained academic genesis
artifact. It does not connect to, operate, or attack any blockchain network.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GENESIS = ROOT / "genesis.json"


def fail(message: str) -> None:
    raise AssertionError(message)


def main() -> int:
    data = json.loads(GENESIS.read_text(encoding="utf-8"))
    config = data.get("config", {})
    clique = config.get("clique", {})

    if config.get("chainId") != 20260315:
        fail("unexpected chainId")
    if clique.get("period") != 5:
        fail("Clique block period should remain 5 seconds")
    if clique.get("epoch") != 30000:
        fail("Clique epoch should remain 30000")
    if str(data.get("difficulty")) != "1":
        fail("Clique genesis difficulty should remain 1")
    if str(data.get("gasLimit")) != "8000000":
        fail("unexpected gas limit")

    extra = data.get("extradata", "")
    if not isinstance(extra, str) or not extra.startswith("0x"):
        fail("extradata must be a 0x-prefixed hex string")
    raw = extra[2:]
    if len(raw) < 64 + 130:
        fail("extradata is too short for Clique vanity + signature")
    if len(raw) % 2 != 0:
        fail("extradata must contain whole bytes")
    try:
        bytes.fromhex(raw)
    except ValueError as exc:
        fail(f"extradata is not valid hex: {exc}")

    signer_hex = raw[64:-130]
    if len(signer_hex) % 40 != 0:
        fail("Clique signer section is not aligned to 20-byte addresses")
    signers = [signer_hex[i : i + 40].lower() for i in range(0, len(signer_hex), 40)]

    alloc = data.get("alloc", {})
    alloc_addresses = {str(address).lower().removeprefix("0x") for address in alloc}

    if len(signers) != 4:
        fail(f"expected 4 Clique signers, found {len(signers)}")
    if len(set(signers)) != len(signers):
        fail("duplicate Clique signer address found")
    if set(signers) != alloc_addresses:
        fail("Clique signer set and funded validator allocation have drifted")

    for address, account in alloc.items():
        normalized = address.lower().removeprefix("0x")
        if len(normalized) != 40:
            fail(f"invalid validator address length: {address}")
        try:
            int(normalized, 16)
        except ValueError:
            fail(f"invalid validator address: {address}")
        balance = int(str(account.get("balance", "0")))
        if balance <= 0:
            fail(f"validator {address} must have positive genesis balance")

    print("Clique genesis validation passed")
    print(f"- chainId: {config['chainId']}")
    print(f"- validators: {len(signers)}")
    print(f"- block period: {clique['period']}s")
    print(f"- epoch: {clique['epoch']}")
    print("- signer set matches funded validator set")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
