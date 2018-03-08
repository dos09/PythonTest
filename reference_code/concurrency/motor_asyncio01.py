import asyncio
import json
import os
import sys

import pymongo
from motor.motor_asyncio import AsyncIOMotorClient

# ATTENTION, READ: !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Motor with asyncio prohibits callbacks
# NOT WORKING FOR WINDOWS


def get_mongo_url_db(filename):
    if not os.path.exists(filename):
        sys.exit('%s not found' % filename)
    with open(filename) as fin:
        conf = json.load(fin)
        mongo_url = conf['mongo_m3']['url']
        mongo_db = conf['mongo_m3']['db']
        return mongo_url, mongo_db


def pymongo_find_one(mongo_url, mongo_db):
    db = pymongo.MongoClient(mongo_url)[mongo_db]
    res = db.org.find_one({'org_id': 134357}, {'name': 1})
    return res


async def motor_asyncio_find_one(mongo_url, mongo_db):
    db = AsyncIOMotorClient(mongo_url)[mongo_db]
    return await db['org'].find_one({'org_id': 134357}, {'name': 1})


if __name__ == '__main__':
#     fis_config_file = r'/etc/fis/fis-config.json'
#     mongo_url, mongo_db = get_mongo_url_db(fis_config_file)
    mongo_url = 'mongodb://localhost:27017'
    mongo_db = 'rimm'
    res = pymongo_find_one(mongo_url, mongo_db)
    print('pymongo find one result: %s' % res)
    event_loop = asyncio.get_event_loop()
    res = event_loop.run_until_complete(
        asyncio.gather(motor_asyncio_find_one(mongo_url, mongo_db)))
    print('motor asyncio find one result: %s' % res)
