def approve_trade(signal):
    print("Running risk checks...")

    if signal["risk_reward"] >= 2.0:
        return True

    return False
