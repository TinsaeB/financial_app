from pydantic import BaseModel
from typing import Optional

class AssetCreate(BaseModel):
    name: str
    description: str
    initial_value: float
    current_value: float
    depreciation_rate: Optional[float] = None
    purchase_date: Optional[str] = None

class Asset(AssetCreate):
    id: int
