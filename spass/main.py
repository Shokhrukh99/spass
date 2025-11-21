from fastapi import FastAPI, APIRouter
from pydantic import BaseModel, Field
from datetime import date, datetime
from typing import Optional, Literal, List
import uvicorn
from fastapi.responses import JSONResponse

# --- PATIENTS CLASS
class Patient(BaseModel):
    full_name: str
    phone_number: Optional[str] = Field(default='+998901234567')
    dob: date
    created_at: date = Field(default_factory=lambda: datetime.now(datetime.utcnow()))
    gender: Literal['male', 'female']

patients = []

# --- CREATE FASTAPI APP ---
app = FastAPI(title='SPASS Patients', description='Patients CRUD module', version='0.01')

router = APIRouter(prefix='/patients')

@router.get('/all/', response_model=List[Patient])
def get_all_patients():
    return patients

@router.post('/create/')
def create_patient(patient: Patient):
    patients.append(patient)
    return JSONResponse({"message": "Successfully created patient record"}, status_code=201)

app.include_router(router)

def main():
    uvicorn.run('main:app', port=8080, reload=True)


if __name__ == "__main__":
    main()