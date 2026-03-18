from flask import Flask, jsonify
import os

app = Flask(__name__)

def greet(name: str = "world") -> str:
    return f"Hello, {name}!"

@app.get("/health")
def health():
    return jsonify(status="ok")

@app.get("/quote")
def quote():
    author = os.getenv("QUOTE_AUTHOR", "Harness")
    return jsonify(message=greet(author))
