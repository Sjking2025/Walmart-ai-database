# test_db.py
from motor.motor_asyncio import AsyncIOMotorClient
import asyncio

async def test_connection():
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    db = client["walmart_ai"]
    collections = await db.list_collection_names()
    print("Connected. Collections:", collections)

asyncio.run(test_connection())
# This script tests the connection to the MongoDB database and lists the collections.