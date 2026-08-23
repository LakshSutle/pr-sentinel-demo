from flask import Flask, request
import sqlite3

app = Flask(__name__)

def get_user(email):
    conn = sqlite3.connect("users.db")
    query = "SELECT * FROM users WHERE email = ?"
    return conn.execute(query, (email,)).fetchone()

@app.route("/user")
def user():
    email = request.args.get("email")
    return str(get_user(email))
# PR Sentinel CI test
