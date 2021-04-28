import asyncio
import asyncpg




def Password():
    return "hui"

async def run():
    global conn

    conn = await asyncpg.connect(user='postgres', password = Password(), database='Download_Music', host='127.0.0.1')
    await conn.close()







loop = asyncio.get_event_loop()
