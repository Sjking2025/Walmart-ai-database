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

# ------------- GET (Read) -------------------
@app.get("/users/{user_id}")
async def read_user(user_id: str):
    user = await get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.get("/products/{product_id}")
async def read_product(product_id: str):
    product = await get_product_by_id(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.get("/reviews/{review_id}")
async def read_review(review_id: str):
    review = await get_review_by_id(review_id)
    if not review:
        raise HTTPException(status_code=404, detail="Review not found")
    return review

# ------------- PUT (Update) -----------------
@app.put("/users/{user_id}/preferences")
async def update_preferences(user_id: str, prefs: dict):
    updated = await update_user_preferences(user_id, prefs)
    if updated:
        return {"message": "User preferences updated"}
    raise HTTPException(status_code=404, detail="User not found")

@app.put("/products/{product_id}/stock")
async def update_stock(product_id: str, stock: int):
    updated = await update_product_stock(product_id, stock)
    if updated:
        return {"message": "Stock updated"}
    raise HTTPException(status_code=404, detail="Product not found")

# ------------- DELETE ------------------------
@app.delete("/products/{product_id}")
async def remove_product(product_id: str):
    deleted = await delete_product(product_id)
    if deleted:
        return {"message": "Product deleted"}
    raise HTTPException(status_code=404, detail="Product not found")

@app.delete("/reviews/{review_id}")
async def remove_review(review_id: str):
    deleted = await delete_review(review_id)
    if deleted:
        return {"message": "Review deleted"}
    raise HTTPException(status_code=404, detail="Review not found")