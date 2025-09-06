from sqlalchemy import create_engine, engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db = "postgresql://posgres:admin.localhost/5432/user"
engine = create_engine(db,echo =True)

SessionLocal = sessionmaker(bind = engine, autoflush=False, autocommit = False)

