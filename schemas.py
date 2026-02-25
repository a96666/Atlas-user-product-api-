from pydantic import BaseModel, Field
from typing import Optional


class UserCreate(BaseModel):
    name: str = Field(..., description="User name")
    email: str = Field(..., description="User email address")
    phone: Optional[str] = Field(None, description="User phone number")
    address: Optional[str] = Field(None, description="User address")


class UserResponse(BaseModel):
    name: str
    email: str
    phone: Optional[str] = None
    address: Optional[str] = None


class ProductCreate(BaseModel):
    sku: str = Field(..., description="Product SKU")
    name: str = Field(..., description="Product name")
    price: float = Field(..., description="Product price")
    stock: int = Field(..., description="Product stock quantity")
    description: Optional[str] = Field(None, description="Product description")


class ProductResponse(BaseModel):
    sku: str
    name: str
    price: float
    stock: int
    description: Optional[str] = None
