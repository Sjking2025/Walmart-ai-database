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
