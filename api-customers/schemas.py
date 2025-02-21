from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime

class Customer(BaseModel):
    id: UUID
    email: EmailStr
    first_name: str
    last_name: str
    phone: str | None = None
    status: str = "ACTIVE"
    created_at: datetime
    updated_at: datetime
    address: str
