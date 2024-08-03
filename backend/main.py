from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes import authentication
from backend.routes import user
from contextlib import asynccontextmanager
from backend.database.database import SessionLocal
from backend.database.init_database import init_database

app = FastAPI()

app.include_router(authentication.router, tags=["login"])
app.include_router(user.router, tags=["user"])

# Define CORS settings to allow requests from specified origins
origins = ["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, # Allow requests from these origins
    allow_credentials=True, # Allow credentials to be sent
    allow_methods=["*"], # Allow all HTTP methods
    allow_headers=["*"], # Allow all headers
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    db = SessionLocal()
    try:
        init_database(db)
        yield
    finally:
        db.close()

app.router.lifespan_context = lifespan

@app.get("/")
def read_root():
    return {"message": "Hello World!"}