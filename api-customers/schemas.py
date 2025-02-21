from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime
from typing import Optional

class Customer(BaseModel):
    id: Optional[UUID] = None
    email: EmailStr
    first_name: str
    last_name: str
    phone: Optional[str] = None
    status: str = "ACTIVE"
    created_at: Optional[datetime] = None 
    updated_at: Optional[datetime] = None
    address: str
