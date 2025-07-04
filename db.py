from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "mongodb://localhost:27017/"

client = AsyncIOMotorClient(MONGO_URI)
db = client["walmart_ai"]  # You can name it anything
