import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY",  os.urandom(32).hex())
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
JWT_ACCESS_TOKEN_EXPIRE_SECONDS = int(os.getenv("JWT_ACCESS_TOKEN_EXPIRE_SECONDS", 3600))
JWT_REFRESH_TOKEN_EXPIRE_SECONDS = int(os.getenv("JWT_REFRESH_TOKEN_EXPIRE_SECONDS", 86400))
AUTH_MODULE_DB_PATH = os.getenv("AUTH_MODULE_DB_PATH", "sqlite:///./auth.db")
MONGODB_LOCAL_URI = os.getenv("MONGODB_LOCAL_URI", "mongodb://localhost:27017")
MONGODB_DOCKER_URI = os.getenv("MONGODB_DOCKER_URI", "mongodb://mongo:27017")
MONGODB_DATABASE_NAME = os.getenv("MONGODB_DATABASE_NAME", "shinnam")
IS_DOCKER = os.getenv("IS_DOCKER", "false")
MAX_FAILURES = int(os.getenv("MAX_FAILURES", 5))
LOCK_TIME_MINUTES = int(os.getenv("LOCK_TIME_MINUTES", 5))
DEFAULT_ROOT_ACCOUNT_ID = os.getenv("DEFAULT_ROOT_ACCOUNT_ID", "root")
DEFAULT_ROOT_ACCOUNT_PASSWORD = os.getenv("DEFAULT_ROOT_ACCOUNT_PASSWORD", "root1234")
REHASH_COUNT_STANDARD = int(os.getenv("REHASH_COUNT_STANDARD", 10))