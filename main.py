from fastapi import FastAPI
from models import Product, User, Review, Return, Provider, Recommendation
from crud import (
    add_product, add_user, add_review, add_return,
    add_provider, add_recommendation
)

app = FastAPI()

@app.post("/products/")
async def create_product(product: Product):
    return await add_product(product)

@app.post("/users/")
async def create_user(user: User):
    result = await add_user(user)
    return {"message": "User inserted", "user_id": str(result.inserted_id)}


@app.post("/reviews/")
async def create_review(review: Review):
    return await add_review(review)

@app.post("/returns/")
async def create_return(return_obj: Return):
    return await add_return(return_obj)

@app.post("/providers/")
async def create_provider(provider: Provider):
    return await add_provider(provider)

@app.post("/recommendations/")
async def create_recommendation(rec: Recommendation):
    return await add_recommendation(rec)
