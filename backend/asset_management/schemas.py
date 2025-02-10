from datetime import date
from pydantic import BaseModel
from typing import Optional

class AssetBase(BaseModel):
    name: str
    asset_type: str
    acquisition_date: date
    acquisition_cost: float
    location: str
    depreciation_method: str
    depreciation_rate: float

class AssetCreate(AssetBase):
    pass

class AssetUpdate(BaseModel):
    name: Optional[str] = None
    asset_type: Optional[str] = None
    acquisition_date: Optional[date] = None
    acquisition_cost: Optional[float] = None
    location: Optional[str] = None
    depreciation_method: Optional[str] = None
    depreciation_rate: Optional[float] = None

class Asset(AssetBase):
    id: int

    class Config:
        orm_mode = True

class AssetDisposalBase(BaseModel):
    asset_id: int
    disposal_date: date
    disposal_proceeds: float

class AssetDisposalCreate(AssetDisposalBase):
    pass

class AssetDisposalUpdate(BaseModel):
    disposal_date: Optional[date] = None
    disposal_proceeds: Optional[float] = None

class AssetDisposal(AssetDisposalBase):
    id: int

    class Config:
        orm_mode = True
