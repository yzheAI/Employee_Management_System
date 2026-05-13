from fastapi import FastAPI
from app.api.student_api import router
from app.api import user_api
from app.api.announce_api import announce_router
import uvicorn
from app.db.session import Base, engine
Base.metadata.create_all(bind=engine)

app = FastAPI(title="学生管理系统 API")
app.include_router(router)
app.include_router(user_api.router)
app.include_router(announce_router)

if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
    )
