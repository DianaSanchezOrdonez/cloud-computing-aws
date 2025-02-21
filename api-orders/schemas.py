from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime
from typing import Optional

class Order(BaseModel):
    id: UUID
    cliente_id: UUID
    status: str
    total_amount: float = Field(..., gt=0)
    created_at: datetime
    updated_at: datetime

class OrderItem(BaseModel):
    order_id: UUID
    product_id: UUID
    quantity: int
    unit_price: float