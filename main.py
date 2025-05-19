from fastapi import FastAPI, Request
import json

app = FastAPI()

@app.get("/status")
def status():
    return {"status": "phantom-online"}

@app.post("/webhook")
async def webhook_handler(request: Request):
    payload = await request.json()
    print("🔥 Incoming webhook payload:")
    print(json.dumps(payload, indent=2))

    if payload.get("phantom_control"):
        bot = payload.get("bot", "Unknown")
        side = payload.get("side", "buy")
        symbol = payload.get("symbol", "BTCUSD")
        price = payload.get("price", "0.00")

        print(f"👻 PHANTOM: Executing {side.upper()} on {symbol} at ${price} via {bot}")

        return {
            "status": "executed",
            "bot": bot,
            "side": side,
            "symbol": symbol,
            "price": price
        }

    return {"status": "ignored", "reason": "phantom_control missing"}
