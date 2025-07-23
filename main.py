# from fastapi import FastAPI
# from app.routes import router
# from app.database import engine, Base

# # Create DB tables
# Base.metadata.create_all(bind=engine)

# app = FastAPI(title="Portfolio API")
# app.include_router(router, prefix="/api", tags=["Portfolio"])
from fastapi import FastAPI
from app.routes import router
from app.database import engine, Base

# Create DB tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(title="Portfolio API")

# Include API router
app.include_router(router, prefix="/api", tags=["Portfolio"])

# Add root endpoint to prevent 404 error
@app.get("/")
def root():
    return {
        "message": "🚀 Portfolio API is up and running!",
        "docs_url": "/docs",
        "endpoints": ["/api/portfolio", "/api/projects", "/api/experience"]
    }
