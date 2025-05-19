from fastapi import FastAPI, Request
import httpx
import os
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

        # Log execution
        print(f"👻 PHANTOM: Executing {side.upper()} on {symbol} at ${price} via {bot}")

        # Call dYdX live order
        dydx_result = await place_dydx_order(side=side, size="0.012", price=price)

        print("📤 dYdX Response:", json.dumps(dydx_result, indent=2))

        return {
            "status": "executed",
            "bot": bot,
            "side": side,
            "symbol": symbol,
            "price": price,
            "dydx": dydx_result
        }

    return {"status": "ignored", "reason": "phantom_control missing"}


# 🔧 LIVE dYdX ORDER FUNCTION
async def place_dydx_order(side: str, size: str, price: str, market: str = "BTC-USD"):
    url = "https://api.dydx.exchange/v3/orders"

    headers = {
        "DYDX-API-KEY": os.getenv("DYDX_API_KEY"),
        "DYDX-API-SECRET": os.getenv("DYDX_API_SECRET"),
        "DYDX-API-PASSPHRASE": os.getenv("DYDX_API_PASSPHRASE"),
        "Content-Type": "application/json"
    }

    order = {
        "market": market,
        "side": side,
        "type": "market",
        "size": size,
        "postOnly": False,
        "cancelAfter": "day",
        "clientId": f"phantom-{os.urandom(4).hex()}",
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, json=order)
        return response.json()
