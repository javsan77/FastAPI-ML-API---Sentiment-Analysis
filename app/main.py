from fastapi import FastAPI
from app.routers.user_router import router as user_router
from app.routers.auth_router import router as auth_router

app = FastAPI(
    title="User API",
    description="API REST básica con FasAPI",
    version="1.0.0"
)

app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(auth_router)

@app.get("/")
def health_check():
    return {"status": "ok"}