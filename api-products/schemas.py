from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime
from typing import Optional

class Product(BaseModel):
    id: Optional[UUID] = None
    sku: str = Field(..., min_length=1, max_length=50)
    name: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = None
    price: float = Field(..., gt=0)
    category_id: Optional[UUID] = None
    status: str = "ACTIVE"
    created_at: Optional[datetime] = None 
    updated_at: Optional[datetime] = None