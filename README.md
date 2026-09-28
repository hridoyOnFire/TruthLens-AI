# 🔍 TruthLens AI — Decentralized Anti-FUD & Content Verification Engine

> **Built for GenLayer Intelligent Contracts** | *AI-Powered On-Chain Truth Verification*

TruthLens AI is an Intelligent Contract on GenLayer designed to fight misinformation, market manipulation, and viral FUD (Fear, Uncertainty, Doubt) in Web3 ecosystems. By leveraging GenLayer's native web connectivity and non-deterministic AI consensus, TruthLens directly parses external news and social media claims to issue immutable, on-chain Truth Scores.

---

## 🌟 Key Features

- **Direct Web Connectivity**: Reads live news and social posts without third-party centralized oracles.
- **AI Consensus Engine**: Multiple validator nodes process content through LLMs to establish non-deterministic consensus on truth scores.
- **Anti-FUD Scoring (0–100)**: Quantifies misinformation levels and detects panic-inducing narratives.
- **On-Chain Auditability**: Stores analysis state directly on the GenLayer ledger for transparent referencing.

---

## 📂 Repository Structure

```text
├── contract.py         # Main GenLayer Intelligent Contract (Python)
├── utils/
│   └── scrapers.py     # Text cleaning & helper utilities
├── test_contract.py    # Unit test suite with GenLayer mocks
└── README.md           # Project Documentation
