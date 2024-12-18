from fastapi import FastAPI, Depends, HTTPException
from . import models, schemas
from core_db.db_utils import get_db
from sqlalchemy.orm import Session
from datetime import date

app = FastAPI()

@app.post("/assets/", response_model=schemas.Asset)
def create_asset(asset: schemas.AssetCreate, db: Session = Depends(get_db)):
    db_asset = models.Asset(**asset.dict())
    return db.create(db_asset)

@app.get("/assets/", response_model=list[schemas.Asset])
def get_assets(db: Session = Depends(get_db)):
    return db.query(models.Asset).all()

@app.get("/assets/{asset_id}", response_model=schemas.Asset)
def get_asset(asset_id: int, db: Session = Depends(get_db)):
    db_asset = db.query(models.Asset).filter(models.Asset.id == asset_id).first()
    if not db_asset:
        raise HTTPException(status_code=404, detail="Asset not found")
    return db_asset

@app.put("/assets/{asset_id}", response_model=schemas.Asset)
def update_asset(asset_id: int, asset: schemas.AssetCreate, db: Session = Depends(get_db)):
    db_asset = db.query(models.Asset).filter(models.Asset.id == asset_id).first()
    if not db_asset:
        raise HTTPException(status_code=404, detail="Asset not found")
    for key, value in asset.dict().items():
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

@app.get("/assets/depreciation-schedule/{asset_id}", response_model=list[dict])
def get_depreciation_schedule(asset_id: int, db: Session = Depends(get_db)):
    db_asset = db.query(models.Asset).filter(models.Asset.id == asset_id).first()
    if not db_asset:
        raise HTTPException(status_code=404, detail="Asset not found")
    
    if not db_asset.depreciation_rate or not db_asset.purchase_date:
        return []

    schedule = []
    current_value = db_asset.initial_value
    current_date = db_asset.purchase_date
    while current_value > 0:
        depreciation_amount = current_value * db_asset.depreciation_rate / 100
        current_value -= depreciation_amount
        current_date = current_date.replace(year=current_date.year + 1)
        schedule.append({
            "year": current_date.year,
            "depreciation_amount": round(depreciation_amount, 2),
            "current_value": round(current_value, 2)
        })
    return schedule
