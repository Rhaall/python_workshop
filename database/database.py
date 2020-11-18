from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#JSON data
import json
from pathlib import Path

engine = create_engine('postgresql+psycopg2://postgres:root@127.0.0.1:5432/spare_time', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import Models.User
    import Models.Keyword
    import Models.KeywordByUser
    import Models.Location
    import Models.Event
    Base.metadata.create_all(bind=engine)

# Import JSON data
def get_data():
    with open(Path(__file__).parent / "data.json", "r") as read_file:
        return json.load(read_file)