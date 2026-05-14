from signal_parser import parse_signal
from risk_manager import approve_trade
from trade_logger import log_trade

fake_signal = {
    "ticker": "MNQ",
    "direction": "LONG",
    "entry": 21450,
    "stop_loss": 21420,
    "take_profit": 21510,
    "risk_reward": 2.0
}

parsed_signal = parse_signal(fake_signal)

approved = approve_trade(parsed_signal)

if approved:
    decision = "APPROVED"
else:
    decision = "REJECTED"

print(f"Phantom Decision: {decision}")

log_trade(parsed_signal, decision)
