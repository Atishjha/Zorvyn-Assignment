from fastapi import HTTPException, Depends
from app.core.deps import get_current_user
def require_role(roles: list):
    def role_checker(user: dict = {"role": "admin"}): 
        if user["role"] not in roles:
            raise HTTPException(status_code=403, detail="Forbidden")
        return user
    return role_checker