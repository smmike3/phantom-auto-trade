from datetime import datetime


def log_trade(signal, decision):
    timestamp = datetime.now()

    print("Logging trade...")
    print(f"[{timestamp}] {signal['ticker']} {signal['direction']} -> {decision}")
