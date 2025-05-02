from urllib.parse import quote_plus
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import setting

encoded_password = quote_plus(setting.DATABASE_PASSWORD)

SQLALCHEMY_DATABASE_URL = f"postgresql://{setting.DATABASE_USERNAME}:{encoded_password}@{setting.DATABASE_HOSTNAME}:{setting.DATABASE_PORT}/{setting.DATABASE_NAME}"


engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit = False, autoflush=False, bind= engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()





#connect database with postgres driver to run raw sql query


# while True:
#     try:
#         conn = psycopg2.connect(host='localhost',database = 'fastapi',
#         user = 'postgres', password = 'Rachit@10',cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("database connect succesfull")
#         break
#     except Exception as error:
#         time.sleep(2)
#         print("connecting to database failed")
#         print("Error:", error)



