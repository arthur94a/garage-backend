from typing import Annotated
from fastapi import Depends
from sqlmodel import Field, Session, SQLModel, create_engine, select
import os
from urllib.parse import quote_plus

# >>> MODELS HERE (START)
from .user import User
from .user_vehicle import UserVehicle
from .vehicle import Vehicle
from .vehicle_price_history import VehiclePriceHistory
from .brand import Brand
from .brand_model import BrandModel
from .brand_model_year import BrandModelYear
from .cache_control import CacheControl
# <<< MODELS HERE (END)

def _build_database_url() -> str:
    database_url = os.getenv("DATABASE_URL")
    if database_url:
        return database_url

    host = os.getenv("RDS_HOSTNAME") or os.getenv("DB_HOST") or "localhost"
    port = os.getenv("RDS_PORT") or os.getenv("DB_PORT") or "5432"
    db_name = os.getenv("RDS_DB_NAME") or os.getenv("DB_NAME") or "garage"
    user = os.getenv("RDS_USERNAME") or os.getenv("DB_USER") or "garage"
    password = os.getenv("RDS_PASSWORD") or os.getenv("DB_PASSWORD") or "garage"
    ssl_mode = os.getenv("DB_SSLMODE") or "require"

    encoded_user = quote_plus(user)
    encoded_password = quote_plus(password)
    encoded_db_name = quote_plus(db_name)

    return (
        f"postgresql+psycopg://{encoded_user}:{encoded_password}"
        f"@{host}:{port}/{encoded_db_name}?sslmode={ssl_mode}"
    )


DB_URL = _build_database_url()

engine = create_engine(DB_URL, pool_pre_ping=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]