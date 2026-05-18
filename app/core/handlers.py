from fastapi import Request
from starlette.responses import JSONResponse

from app.core.exceptions import PermissionDenied, ConflictError, NotFoundError


def register_exception_handler(app):

    @app.exception_handler(ConflictError)
    async def conflict_error_handler(request: Request, exc: ConflictError):
        return JSONResponse(
            status_code=409,
            content={
                "code": 409,
                "message": exc.message,
            }
        )

    @app.exception_handler(PermissionDenied)
    async def permission_error_handler(request: Request, exc: PermissionDenied):
        return JSONResponse(
            status_code=403,
            content={
                "code": 403,
                "message": exc.message,
            }
        )

    @app.exception_handler(NotFoundError)
    async def not_found_handler(request: Request, exc: NotFoundError):
        return JSONResponse(
            status_code=404,
            content={
                "code": 404,
                "message": exc.message,
            }
        )

    @app.exception_handler(Exception)
    async def exception_handler(request: Request, exc: Exception):
        return JSONResponse(
            status_code=500,
            content={
                "code": 500,
                "message": "Internal Server Error",
            }
        )
