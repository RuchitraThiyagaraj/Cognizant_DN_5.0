from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

DATABASE_URL = "mysql+pymysql://root:rootnew@localhost/college_db"

engine = create_engine(DATABASE_URL)

try:
    connection = engine.connect()
    print("Database Connected Successfully!")
    connection.close()
except Exception as e:
    print(e)

Base = declarative_base()
