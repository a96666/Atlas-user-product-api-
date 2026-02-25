from fastapi import FastAPI, HTTPException
from app.database import users_collection, products_collection
from app.schemas import UserCreate, UserResponse, ProductCreate, ProductResponse
from bson import ObjectId
from typing import Optional

app = FastAPI(title="Atlas User & Product Management API")


@app.post("/users", response_model=UserResponse)
async def create_user(user: UserCreate):
    existing_user = users_collection.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already exists")
    
    user_dict = user.model_dump()
    result = users_collection.insert_one(user_dict)
    
    created_user = users_collection.find_one({"_id": result.inserted_id})
    created_user["_id"] = str(created_user["_id"])
    
    return UserResponse(**created_user)


@app.get("/users/{email}", response_model=UserResponse)
async def get_user_by_email(email: str):
    user = users_collection.find_one({"email": email})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    user["_id"] = str(user["_id"])
    return UserResponse(**user)


@app.post("/products", response_model=ProductResponse)
async def create_product(product: ProductCreate):
    existing_product = products_collection.find_one({"sku": product.sku})
    if existing_product:
        raise HTTPException(status_code=400, detail="SKU already exists")
    
    product_dict = product.model_dump()
    result = products_collection.insert_one(product_dict)
    
    created_product = products_collection.find_one({"_id": result.inserted_id})
    created_product["_id"] = str(created_product["_id"])
    
    return ProductResponse(**created_product)


@app.get("/products/{sku}", response_model=ProductResponse)
async def get_product_by_sku(sku: str):
    product = products_collection.find_one({"sku": sku})
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    product["_id"] = str(product["_id"])
    return ProductResponse(**product)


@app.get("/")
async def root():
    return {"message": "Atlas User & Product Management API"}