import sqlite3
import pytest

from app import get_user, apply_discount


@pytest.fixture
def test_db(monkeypatch, tmp_path):
    db_path = tmp_path / "users.db"

    conn = sqlite3.connect(db_path)
    conn.execute("CREATE TABLE users (id INTEGER, email TEXT)")
    conn.execute(
        "INSERT INTO users VALUES (?, ?)",
        (1, "alice@example.com"),
    )
    conn.commit()
    conn.close()

    def connect(_):
        return sqlite3.connect(db_path)

    monkeypatch.setattr("app.sqlite3.connect", connect)


def test_get_user_valid_email(test_db):
    result = get_user("alice@example.com")
    assert result == (1, "alice@example.com")

def test_user_endpoint_returns_expected_response():
    from app import app

    client = app.test_client()

    response = client.get("/user?email=alice@example.com")

    assert response.status_code == 200

def test_get_user_special_characters(test_db):
    result = get_user("alice'@example.com")
    assert result is None


def test_get_user_missing_email(test_db):
    result = get_user(None)
    assert result is None


def test_apply_discount_normal():
    assert apply_discount(100, 20) == 80


def test_apply_discount_zero():
    assert apply_discount(100, 0) == 100
