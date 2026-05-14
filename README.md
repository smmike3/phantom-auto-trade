# Phantom Auto Trade

Phantom Auto Trade is the training-mode foundation for the GhostOps automation system.

The goal is to learn AI, Python, APIs, webhooks, risk logic, and trading infrastructure by building a real system step by step.

## Current Stage

**v0.1 — Training Mode**

This version does not place live trades. It receives or simulates a TradingView-style alert, parses the signal, runs risk checks, logs the trade decision, and prints whether the signal is approved or rejected.

## System Flow

```text
Fake TradingView Alert
        ↓
Python Webhook Receiver
        ↓
Signal Parser
        ↓
Risk Manager
        ↓
Trade Logger
        ↓
Approved / Rejected Decision
```

## Project Structure

```text
phantom-auto-trade/
├── README.md
├── requirements.txt
├── .gitignore
├── app/
│   ├── main.py
│   ├── signal_parser.py
│   ├── risk_manager.py
│   └── trade_logger.py
├── data/
│   └── trades.csv
├── tests/
│   └── fake_signal.json
└── docs/
    └── roadmap.md
```

## Learning Goals

- Learn Python fundamentals
- Understand JSON signal data
- Understand APIs and webhooks
- Build clean project structure
- Practice risk management logic
- Log trade decisions like a real system
- Prepare for future AI scoring and Google Sheets sync

## Run Locally

```bash
python app/main.py
```

## Safety Rule

This repo starts in training mode only. No live execution should be added until the parser, risk manager, logging, and review flow are stable.