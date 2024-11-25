from fastapi import FastAPI, Depends
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    """ユーザーモデルの定義."""

    username: str  # 名前
    is_active: bool = True  # 状態


# ユーザーデータのリスト
users = [
    User(username="太郎", is_active=True),
    User(username="次郎", is_active=False),
    User(username="花子", is_active=True),
]


def get_active_users():
    """アクティブなユーザーをフィルタリングする依存関係関数,"""
    active_users = [user for user in users if user.is_active]
    print("=== アクティブなユーザーを取得 ===")
    return active_users


@app.get("/active")
async def list_active_users(active_users: list[User] = Depends(get_active_users)):
    print("=== 【依存】してデータを取得 ===")
    return active_users
