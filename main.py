from fastapi import FastAPI, Request
import httpx
import json

app = FastAPI()

@app.post("/webhook")
async def webhook_handler(req: Request):
    payload = await req.json()
    print("🔥 Incoming webhook payload:", json.dumps(payload, indent=2))

    # Filter for Phantom control flag
    if payload.get("phantom_control"):
        bot = payload.get("bot", "Unknown")
        side = payload.get("side", "buy")
        symbol = payload.get("symbol", "BTCUSD")
        price = payload.get("price", "0.00")

        # Simulate trade execution
        print(f"👻 PHANTOM: Executing {side.upper()} on {symbol} at ${price} via {bot}")
        
        # Later: Call real dYdX trade function here

        return {
            "status": "executed",
            "bot": bot,
            "side": side,
            "symbol": symbol,
            "price": price
        }

    return {"status": "ignored"}
