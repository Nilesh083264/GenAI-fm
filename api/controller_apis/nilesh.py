from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class DataReq(BaseModel):
    name: str
    phone_number: int

@router.post("/pydantic")
async def hello_nilesh(req: DataReq):
    try:
        data = req.dict()
        print("data:", data)
        return {"Nilesh": data}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid JSON: {str(e)}")
