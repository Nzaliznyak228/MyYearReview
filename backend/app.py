import os
from flask import Flask, request, jsonify, send_from_directory
import sqlite3
from flask_cors import CORS

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'data.sqlite')

app = Flask(__name__, static_folder='../web', static_url_path='/')
CORS(app)

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        first_name TEXT,
        username TEXT,
        messages INTEGER DEFAULT 0,
        rounds INTEGER DEFAULT 0,
        photos INTEGER DEFAULT 0
    );
    ''')
    conn.commit()
    conn.close()

@app.route('/api/results')
def results():
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({"error":"user_id required"}), 400
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT id, first_name, username, messages, rounds, photos FROM users WHERE id=?", (user_id,))
    row = cur.fetchone()
    if not row:
        # create demo record
        cur.execute("INSERT INTO users (id, first_name, username, messages, rounds, photos) VALUES (?, ?, ?, ?, ?, ?)",
                    (user_id, "Guest", "guest", 42, 12, 7))
        conn.commit()
        cur.execute("SELECT id, first_name, username, messages, rounds, photos FROM users WHERE id=?", (user_id,))
        row = cur.fetchone()
    conn.close()
    return jsonify({
        "id": row[0],
        "first_name": row[1],
        "username": row[2],
        "messages": row[3],
        "rounds": row[4],
        "photos": row[5]
    })

@app.route('/')
def web_root():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', '8080')))
