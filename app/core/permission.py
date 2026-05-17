from fastapi import Depends
from app.core.exceptions import PermissionDenied
from app.core.security import get_current_user


def require_roles(*roles):
    def checker(user=Depends(get_current_user)):
        if user["role"] not in roles:
            raise PermissionDenied("权限不足")
        return user
    return checker
