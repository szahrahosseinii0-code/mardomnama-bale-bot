from flask import Flask, request
import requests
import os

app = Flask(__name__)

TOKEN = os.environ.get("BALE_TOKEN")
API_URL = f"https://tapi.bale.ai/bot{TOKEN}/sendMessage"

@app.route("/", methods=["POST"])
def webhook():
    data = request.json
    chat_id = data["message"]["chat"]["id"]

    message = (
        "سلام.\n"
        "اطلاعات اولیه پرونده شما دریافت شد.\n"
        "تیم مردم‌نما پس از بررسی با شما تماس می‌گیرد."
    )

    requests.post(API_URL, json={
        "chat_id": chat_id,
        "text": message
    })

    return "ok"

app.run(host="0.0.0.0", port=10000)
