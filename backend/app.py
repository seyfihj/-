from dataclasses import dataclass
from typing import Dict

from flask import Flask, jsonify, request

app = Flask(__name__)


@dataclass(frozen=True)
class User:
    username: str
    password: str
    display_name: str


# NOTE: In a real application credentials would be stored in a database and
# passwords would be hashed. This in-memory store is only for demonstration
# purposes.
USERS: Dict[str, User] = {
    "demo": User(username="demo", password="demo123", display_name="デモ ユーザー"),
    "admin": User(username="admin", password="secret", display_name="管理者"),
}


@app.post("/api/login")
def login() -> "tuple[str, int] | tuple[dict, int]":
    """Authenticate the user using a JSON payload.

    Expected request payload::

        {"username": "...", "password": "..."}
    """

    if not request.is_json:
        return jsonify({"error": "JSON形式のリクエストを送信してください。"}), 400

    data = request.get_json(silent=True) or {}
    username = data.get("username", "").strip()
    password = data.get("password", "")

    if not username or not password:
        return jsonify({"error": "ユーザー名とパスワードを入力してください。"}), 400

    user = USERS.get(username)
    if not user or user.password != password:
        return jsonify({"error": "ユーザー名またはパスワードが正しくありません。"}), 401

    return jsonify({
        "message": "ログインに成功しました。",
        "displayName": user.display_name,
    })


@app.get("/api/health")
def health() -> dict:
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(debug=True)
