from fastapi import FastAPI
from app.api.student_api import router
from app.api import user_api
from app.api.announce_api import announce_router
from app.api.employee_api import employee_router
from app.api.department_api import department_router
import uvicorn
from app.db.session import Base, engine
from app.core.handlers import register_exception_handler
Base.metadata.create_all(bind=engine)

app = FastAPI(title="企业管理系统 API")
register_exception_handler(app)

app.include_router(user_api.router)
app.include_router(announce_router)
app.include_router(employee_router)
app.include_router(department_router)
app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
    )
