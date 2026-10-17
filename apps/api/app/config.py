"""Environment settings. Loaded once here so a missing variable stops the app at startup
instead of failing later in the middle of a request."""

import os

from dotenv import load_dotenv

# loads variables from .env
load_dotenv()


def require_env(name: str) -> str:
    value = os.getenv(name)

    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")

    return value


def to_psycopg_url(url: str) -> str:
    # Neon gives URLs starting with postgresql:// (or postgres://). SQLAlchemy would look for the
    # psycopg2 driver for those, but we installed psycopg 3, so we name the driver explicitly.
    for prefix in ("postgres://", "postgresql://"):
        if url.startswith(prefix):
            return "postgresql+psycopg://" + url[len(prefix):]

    return url


DATABASE_URL = to_psycopg_url(require_env("DATABASE_URL"))

JWT_SECRET_KEY = require_env("JWT_SECRET_KEY")

# set ENVIRONMENT=production when deployed. This turns on secure cookies (sent over HTTPS only)
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
IS_PRODUCTION = ENVIRONMENT == "production"
