from fastapi import FastAPI
from app.routes import router
from app.database import engine, Base

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Portfolio API")
app.include_router(router, prefix="/api", tags=["Portfolio"])
