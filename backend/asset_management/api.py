from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core_db.db_utils import get_db, create
from . import models, schemas

app = APIRouter()

# --- Assets ---

@app.post("/assets/", response_model=schemas.Asset)
def create_asset(asset: schemas.AssetCreate, db: Session = Depends(get_db)):
    db_asset = models.Asset(**asset.dict())
    return create(db, db_asset)

@app.get("/assets/", response_model=List[schemas.Asset])
def get_assets(db: Session = Depends(get_db)):
    return db.query(models.Asset).all()

@app.get("/assets/{asset_id}", response_model=schemas.Asset)
def get_asset(asset_id: int, db: Session = Depends(get_db)):
    db_asset = db.query(models.Asset).filter(models.Asset.id == asset_id).first()
    if not db_asset:
        raise HTTPException(status_code=404, detail="Asset not found")
    return db_asset

@app.put("/assets/{asset_id}", response_model=schemas.Asset)
def update_asset(asset_id: int, asset: schemas.AssetUpdate, db: Session = Depends(get_db)):
    db_asset = db.query(models.Asset).filter(models.Asset.id == asset_id).first()
    if not db_asset:
        raise HTTPException(status_code=404, detail="Asset not found")
    for key, value in asset.dict(exclude_unset=True).items():
        setattr(db_asset, key, value)
    db.commit()
    db.refresh(db_asset)
    return db_asset

@app.delete("/assets/{asset_id}")
def delete_asset(asset_id: int, db: Session = Depends(get_db)):
    db_asset = db.query(models.Asset).filter(models.Asset.id == asset_id).first()
    if not db_asset:
        raise HTTPException(status_code=404, detail="Asset not found")
    db.delete(db_asset)
    db.commit()
    return {"message": "Asset deleted successfully"}

# --- Asset Disposals ---

@app.post("/asset-disposals/", response_model=schemas.AssetDisposal)
def create_asset_disposal(disposal: schemas.AssetDisposalCreate, db: Session = Depends(get_db)):
    db_disposal = models.AssetDisposal(**disposal.dict())
    return create(db, db_disposal)

@app.get("/asset-disposals/", response_model=List[schemas.AssetDisposal])
def get_asset_disposals(db: Session = Depends(get_db)):
    return db.query(models.AssetDisposal).all()

@app.get("/asset-disposals/{disposal_id}", response_model=schemas.AssetDisposal)
def get_asset_disposal(disposal_id: int, db: Session = Depends(get_db)):
    db_disposal = db.query(models.AssetDisposal).filter(models.AssetDisposal.id == disposal_id).first()
    if not db_disposal:
        raise HTTPException(status_code=404, detail="Asset disposal not found")
    return db_disposal

@app.put("/asset-disposals/{disposal_id}", response_model=schemas.AssetDisposal)
def update_asset_disposal(disposal_id: int, disposal: schemas.AssetDisposalUpdate, db: Session = Depends(get_db)):
    db_disposal = db.query(models.AssetDisposal).filter(models.AssetDisposal.id == disposal_id).first()
    if not db_disposal:
        raise HTTPException(status_code=404, detail="Asset disposal not found")
    for key, value in disposal.dict(exclude_unset=True).items():
        setattr(db_disposal, key, value)
    db.commit()
    db.refresh(db_disposal)
    return db_disposal

@app.delete("/asset-disposals/{disposal_id}")
def delete_asset_disposal(disposal_id: int, db: Session = Depends(get_db)):
    db_disposal = db.query(models.AssetDisposal).filter(models.AssetDisposal.id == disposal_id).first()
    if not db_disposal:
        raise HTTPException(status_code=404, detail="Asset disposal not found")
    db.delete(db_disposal)
    db.commit()
    return {"message": "Asset disposal deleted successfully"}
