from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Bot container is alive and reachable!", 200

@app.route('/health')
def health():
    return jsonify({
        "status": "ok",
        "service": "telegram-bot",
        "message": "Healthy"
    }), 200


def healthcheck():
    """Run Flask app (used when imported in main.py)"""
    port = int(os.getenv("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
