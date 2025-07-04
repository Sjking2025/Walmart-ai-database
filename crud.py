from db import db
from models import Product, User, Review, Return, Provider, Recommendation

# -------- PRODUCT --------

async def add_product(product: Product):
    result = await db.products.insert_one(product.dict())
    return {"inserted_id": str(result.inserted_id)}


# -------- USER --------
async def add_user(user: User):
    return await db.users.insert_one(user.dict())  # Returns InsertOneResult



# -------- REVIEW --------
async def add_review(review: Review):
    return await db.reviews.insert_one(review.dict())

# -------- RETURN --------
async def add_return(return_obj: Return):
    return await db.returns.insert_one(return_obj.dict())

# -------- PROVIDER --------
async def add_provider(provider: Provider):
    return await db.providers.insert_one(provider.dict())

# -------- RECOMMENDATION --------
async def add_recommendation(rec: Recommendation):
    return await db.recommendations.insert_one(rec.dict())

# Utility to convert MongoDB ObjectId to str
def serialize_doc(doc):
    doc["_id"] = str(doc["_id"])
    return doc

# -------- GET METHODS --------

async def get_user_by_id(user_id: str):
    user = await db.users.find_one({"_id": ObjectId(user_id)})
    return serialize_doc(user) if user else None

async def get_product_by_id(product_id: str):
    product = await db.products.find_one({"_id": ObjectId(product_id)})
    return serialize_doc(product) if product else None

async def get_review_by_id(review_id: str):
    review = await db.reviews.find_one({"_id": ObjectId(review_id)})
    return serialize_doc(review) if review else None

# -------- UPDATE METHODS --------

async def update_user_preferences(user_id: str, new_prefs: dict):
    result = await db.users.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": {"preferences": new_prefs}}
    )
    return result.modified_count

async def update_product_stock(product_id: str, new_stock: int):
    result = await db.products.update_one(
        {"_id": ObjectId(product_id)},
        {"$set": {"stock": new_stock}}
    )
    return result.modified_count

# -------- DELETE METHODS --------

async def delete_product(product_id: str):
    result = await db.products.delete_one({"_id": ObjectId(product_id)})
    return result.deleted_count

async def delete_review(review_id: str):
    result = await db.reviews.delete_one({"_id": ObjectId(review_id)})
    return result.deleted_count