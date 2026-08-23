from flask import Flask, request
import sqlite3

app = Flask(__name__)

def get_user(email):
    conn = sqlite3.connect("users.db")
    query = f"SELECT * FROM users WHERE email = '{email}'"
    return conn.execute(query).fetchone()

@app.route("/user")
def user():
    email = request.args.get("email")
    return str(get_user(email))

def apply_discount(total, discount):
    return total - discount
