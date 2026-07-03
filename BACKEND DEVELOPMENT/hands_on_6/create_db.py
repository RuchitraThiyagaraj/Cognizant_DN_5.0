'''import asyncio
from database import engine
from models import Base

#this function is necessary because 'await' can only be used inside an async function.
async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

asyncio.run(create_tables())

#without using async => Base.metadata.create_all(bind=engine)'''

import asyncio
from database import engine
from models import Base

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    
    await engine.dispose()

if __name__ == "__main__":
    #to avoid ProactorEventLoop issue
    asyncio.run(create_tables())
