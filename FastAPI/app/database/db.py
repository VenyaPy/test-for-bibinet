import asyncpg
import os


DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:0000@localhost/bibinet")


async def connect_to_db():
    conn = await asyncpg.connect(DATABASE_URL)
    return conn


async def close_db_connection(conn):
    await conn.close()