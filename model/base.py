from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session

from config.config import POSTGRES_CONNECTION_STRING


engine = create_engine(POSTGRES_CONNECTION_STRING)
session_factory = sessionmaker(bind=engine)

Session = scoped_session(session_factory)
Base = declarative_base()
