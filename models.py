from pydantic import BaseModel, Field, EmailStr
from typing import List, Dict, Optional
from datetime import datetime

# -------------------- PRODUCT --------------------
class SizeInfo(BaseModel):
    length: str
    chest: str

class Product(BaseModel):
    _id: str
    name: str
    brand: str
    category: str
    price: float
    stock: int
    image_url: str
    tags: List[str]
    return_count: int
    order_count: int
    max_return_threshold: float  # e.g. 0.3 means 30%
    size_chart: Dict[str, SizeInfo]
    provider_id: str

# -------------------- USER --------------------
class UserOrder(BaseModel):
    product_id: str
    rating: Optional[int]
    review: Optional[str]
    returned: bool

class Preferences(BaseModel):
    liked_brands: List[str]
    preferred_colors: List[str]

class User(BaseModel):
    _id: str
    name: str
    email: EmailStr
    orders: List[UserOrder]
    preferences: Preferences
    discount_tier: str

# -------------------- REVIEW --------------------
class Review(BaseModel):
    _id: str
    user_id: str
    product_id: str
    text: str
    sentiment: str  # "positive", "negative", "neutral"
    is_fake: bool

# -------------------- RETURN --------------------
class Return(BaseModel):
    _id: str
    user_id: str
    product_id: str
    reason: str
    classification: str  # "valid", "invalid"
    created_at: datetime = Field(default_factory=datetime.utcnow)

# -------------------- PROVIDER --------------------
class ReturnAlert(BaseModel):
    product_id: str
    message: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)

class Provider(BaseModel):
    _id: str
    name: str
    email: EmailStr
    products: List[str]
    return_alerts: List[ReturnAlert]

# -------------------- RECOMMENDATION (optional cache) --------------------
class Recommendation(BaseModel):
    _id: str
    user_id: str
    recommended_products: List[str]
