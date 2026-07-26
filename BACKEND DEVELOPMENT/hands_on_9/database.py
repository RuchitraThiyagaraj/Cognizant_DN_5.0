from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

#this is a global file for the engine ,session maker [we can create new sessions using Dependency injection]

DATABASE_URL = "mysql+aiomysql://root:root15@localhost/fastapi"

engine = create_async_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)


async def get_db():
    async with SessionLocal() as db:
        yield db
