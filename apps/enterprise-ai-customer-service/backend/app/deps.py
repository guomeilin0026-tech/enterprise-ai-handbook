from fastapi import Header, HTTPException

from app.store import get_user_by_token


def current_user(authorization: str = Header(default="")) -> dict:
    token = authorization.replace("Bearer ", "")
    user = get_user_by_token(token)
    if not user:
        raise HTTPException(status_code=401, detail="未登录或 token 无效")
    return user

