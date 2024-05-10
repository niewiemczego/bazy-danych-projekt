from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

SQLALCHEMY_DATABASE_URL_POSTGRES = (
    "postgresql://postgres:Tymoteusz123@localhost:5432/todos-database"
)

SQLALCHEMY_DATABASE_URL_POSTGRES_SQLITE = "sqlite:///./todos-database.db"

# connect_args is used to avoid an error that occurs when using SQLite.
engine = create_engine(
    SQLALCHEMY_DATABASE_URL_POSTGRES_SQLITE, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
