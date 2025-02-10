from fastapi import FastAPI, Depends, HTTPException
from . import models, llm_utils
from core_db.db_utils import get_db
from sqlalchemy.orm import Session
from pydantic import BaseModel

app = FastAPI()

class AdviceRequest(BaseModel):
    prompt: str
    model_name: str = "llama3.2"

@app.post("/financial-advice/", response_model=dict)
async def get_financial_advice(request: AdviceRequest, db: Session = Depends(get_db)):
    
    # For now, just pass the prompt to the LLM
    result = llm_utils.query_ollama(request.model_name, request.prompt)
    
    # Create a new advice record
    advice = models.FinancialAdvice(
        prompt = request.prompt,
        response = result["response"]
    )
    db.create(advice)
    
    return {
        "advice_id": advice.id,
        "response": result["response"]
    }

@app.get("/financial-advice/{advice_id}", response_model=dict)
def get_advice(advice_id: int, db: Session = Depends(get_db)):
    advice = db.query(models.FinancialAdvice).filter(models.FinancialAdvice.id == advice_id).first()
    if not advice:
        raise HTTPException(status_code=404, detail="Advice not found")
    return {
        "advice_id": advice.id,
        "prompt": advice.prompt,
        "response": advice.response
    }
