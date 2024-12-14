from os import getenv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

URL = getenv('DB_URL')
engine = create_engine(URL)
Session = sessionmaker(bind=engine)
session = Session()
