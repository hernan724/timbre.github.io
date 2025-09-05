from flask import Flask, render_template, request
import requests, os

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <html>
    <head><title>Timbre Digital</title></head>
    <body style='text-align:center; margin-top:20%; font-family:sans-serif;'>
        <h1>🔔 Timbre Digital</h1>
        <form action='/timbre'>
            <button style='font-size:2em; padding:20px; border-radius:15px; background:#28a745; color:white; border:none; cursor:pointer;'>
                Tocar Timbre
            </button>
        </form>
    </body>
    </html>
    """

@app.route("/timbre")
def timbre():
    mensaje = "🔔 Alguien tocó el timbre (escaneó el QR)"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": mensaje}
    requests.post(url, data=data)
    return "<h2>✅ Timbre enviado, alguien ya fue notificado!</h2>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
