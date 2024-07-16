import asyncpg


async def get_db():
    conn = await asyncpg.connect("postgresql://postgres:postgres@db/bibinet_test")
    try:
        yield conn
    finally:
        await conn.close()
