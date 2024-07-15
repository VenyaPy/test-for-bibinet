import asyncpg


async def get_db():
    conn = await asyncpg.connect("postgresql://postgres:0000@localhost/bibinet_test")
    try:
        yield conn
    finally:
        await conn.close()
