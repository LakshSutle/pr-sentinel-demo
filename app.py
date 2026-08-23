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

def apply_discount(total, discount):
    if not isinstance(total, (int, float)):
        raise TypeError("total must be numeric")

    if not isinstance(discount, (int, float)):
        raise TypeError("discount must be numeric")

    if discount < 0:
        raise ValueError("discount cannot be negative")

    if discount > total:
        raise ValueError("discount cannot exceed total")

    return total - discount
