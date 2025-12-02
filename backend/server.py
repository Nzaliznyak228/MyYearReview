
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/api/results")
def results():
    user_id = request.args.get("user_id", "0")
    return jsonify({
        "round_videos": 4492,
        "photos": 1231,
        "fav_emojis": ["😂", "🔥", "😍"]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
