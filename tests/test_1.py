import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

@pytest.fixture(scope="session")
def db_engine(request):
    db_url = request.config.getoption("--dburl")
    engine_ = create_engine(db_url, echo=True)
    yield engine_ 
    engine_.dispose()

@pytest.fixture(scope="session")
def db_session_factory(db_engine):
    return scoped_session(sessionmaker(bind=db_engine))

@pytest.fixture(scope="function")
def db_session(db_session_factory):
    session_ = db_session_factory
    yield session_
    session_.rollback()
    session_.close()

