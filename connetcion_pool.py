import asyncio, logging
import aiomysql

__pool = None


async def create_pool(loop, **kw):
    logging.info("create database connection pool...")
    global __pool
    __pool = await aiomysql.create_pool(
        host=kw.get('host', 'localhost'),
        port=kw.get('port', 3306),
        user=kw['user'],
        password=kw['password'],
        db=kw['db'],
        charset=kw.get('charset', 'utf8'),
        autocommit=kw.get('autocommit', True),
        maxsize=kw.get('maxsize', 10),
        minsize=kw.get('minsize', 1),
        loop=loop
    )


async def select(sql, args, size=None):
    global __pool
    with (await __pool) as conn:
        cursor = await conn.cursor(aiomysql.DictCursor)
        await cursor.execute(sql.replace('?', '%s'), args or ())
        if size:
            rs = await cursor.fetchmany(size)
        else:
            rs = await cursor.fetchall()
            await cursor.close()
        logging.info("rows returned: %s" % len(rs))
        return rs


async def test():
    await create_pool(loop=loop, host='67.218.132.112', user='jty', password='jty_1994127', db='lychee')
    await select("select * from ly__lychee_photos", "")


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    data = test().send(None)
    print(data)
