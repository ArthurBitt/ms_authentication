# third party
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
#  local
from src.infrastructure.config.settings import settings

dns = settings.DNS

# create a configured engine
engine = create_engine(
    dns,
    connect_args={"check_same_thread": False}
) if "sqlite" in dns else create_engine(dns)


# create a Session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# base to orm models
Base = declarative_base()


