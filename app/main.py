from fastapi import FastAPI
from app.routers.user_router import router as user_router
from app.routers.auth_router import router as auth_router
from app.routers.ml_router import router as ml_router

app = FastAPI(
    title="User API with ML",
    description="API REST con Machine Learning integrado",
    version="2.0.0"
)

app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(auth_router)
app.include_router(ml_router)

@app.get("/")
def health_check():
    return {"status": "ok", "version": "2.0.0", "ml_enabled": True}