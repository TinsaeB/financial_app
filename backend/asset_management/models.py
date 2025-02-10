from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float
from sqlalchemy.orm import relationship
from core_db.db_utils import Base

class Asset(Base):
    __tablename__ = "assets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    asset_type = Column(String)
    acquisition_date = Column(Date)
    acquisition_cost = Column(Float)
    location = Column(String)
    depreciation_method = Column(String)
    depreciation_rate = Column(Float)
    
    disposals = relationship("AssetDisposal", back_populates="asset")

class AssetDisposal(Base):
    __tablename__ = "asset_disposals"

    id = Column(Integer, primary_key=True, index=True)
    asset_id = Column(Integer, ForeignKey("assets.id"))
    disposal_date = Column(Date)
    disposal_proceeds = Column(Float)
    
    asset = relationship("Asset", back_populates="disposals")
