from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)   # позволяет GitHub Pages обращаться к серверу


# ================================
#  Пример API для WebApp
# ================================
@app.route("/api/user", methods=["POST"])
def user_data():
    """
    Принимает данные авторизации WebApp и возвращает статистику.
    Telegram WebApp отправляет объект initData — его можно валидировать.
    Пока валидируем упрощённо.
    """
    data = request.json

    if not data:
        return jsonify({"error": "No data provided"}), 400

    # здесь можно добавить проверку Telegram initData
    # https://core.telegram.org/bots/webapps#validating-data

    user_id = data.get("user_id")

    # ВРЕМЕННАЯ СТАТИСТИКА (как заглушка под YearReview)
    stats = {
        "user_id": user_id,
        "round_videos": 4492,
        "top_word": "hello",
        "stories_views": 123,
        "messages_count": 54210,
    }

    return jsonify(stats)


@app.route("/", methods=["GET"])
def home():
    return "Backend is running"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)