from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import crud_service, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/otp_log/', response_model=List[schemas.OtpLog])
def get_all_otp_log(db: Session = Depends(get_db)):
    return crud_service.get_all_otp_log(db)

@router.get('/otp_log/id', response_model=schemas.OtpLog)
def get_otp_log_by_id(id: int, db: Session = Depends(get_db)):
    return crud_service.get_otp_log_by_id(db, id)

@router.post('/otp_log/', response_model=schemas.OtpLog)
def create_otp_log(id: str, created_at: str, email: str, ip: str, type: str, attempts: str, updated_at: str, db: Session = Depends(get_db)):
    return crud_service.create_otp_log(db, id, created_at, email, ip, type, attempts, updated_at)

@router.put('/otp_log/id/', response_model=schemas.OtpLog)
def update_otp_log_by_id(id: str, created_at: str, email: str, ip: str, type: str, attempts: str, updated_at: str, db: Session = Depends(get_db)):
    return crud_service.update_otp_log_by_id(db, id, created_at, email, ip, type, attempts, updated_at)

@router.delete('/otp_log/id', response_model=schemas.OtpLog)
def delete_otp_log_by_id(id: int, db: Session = Depends(get_db)):
    return crud_service.delete_otp_log_by_id(db, id)

@router.get('/demo_inquiry/', response_model=List[schemas.DemoInquiry])
def get_all_demo_inquiry(db: Session = Depends(get_db)):
    return crud_service.get_all_demo_inquiry(db)

@router.get('/demo_inquiry/id', response_model=schemas.DemoInquiry)
def get_demo_inquiry_by_id(id: int, db: Session = Depends(get_db)):
    return crud_service.get_demo_inquiry_by_id(db, id)

@router.post('/demo_inquiry/', response_model=schemas.DemoInquiry)
def create_demo_inquiry(created_at: str, name: str, email: str, phone: str, profession: str, desc: str, status: str, updated_at: str, reapply_count: str, id: str, db: Session = Depends(get_db)):
    return crud_service.create_demo_inquiry(db, created_at, name, email, phone, profession, desc, status, updated_at, reapply_count, id)

@router.put('/demo_inquiry/id/', response_model=schemas.DemoInquiry)
def update_demo_inquiry_by_created_at(created_at: str, name: str, email: str, phone: str, profession: str, desc: str, status: str, updated_at: str, reapply_count: str, id: str, db: Session = Depends(get_db)):
    return crud_service.update_demo_inquiry_by_created_at(db, created_at, name, email, phone, profession, desc, status, updated_at, reapply_count, id)

@router.delete('/demo_inquiry/id', response_model=schemas.DemoInquiry)
def delete_demo_inquiry_by_id(id: int, db: Session = Depends(get_db)):
    return crud_service.delete_demo_inquiry_by_id(db, id)

@router.get('/founder/', response_model=List[schemas.Founder])
def get_all_founder(db: Session = Depends(get_db)):
    return crud_service.get_all_founder(db)

@router.get('/founder/id', response_model=schemas.Founder)
def get_founder_by_id(id: int, db: Session = Depends(get_db)):
    return crud_service.get_founder_by_id(db, id)

@router.post('/founder/', response_model=schemas.Founder)
def create_founder(id: str, name: str, email: str, linkedin_url: str, is_technical: str, age: str, gender: str, question_contribution: str, question_meet: str, invites: str, founder_video: str, company_id: str, createdAt: str, updatedAt: str, db: Session = Depends(get_db)):
    return crud_service.create_founder(db, id, name, email, linkedin_url, is_technical, age, gender, question_contribution, question_meet, invites, founder_video, company_id, createdAt, updatedAt)

@router.put('/founder/id/', response_model=schemas.Founder)
def update_founder_by_id(id: str, name: str, email: str, linkedin_url: str, is_technical: str, age: str, gender: str, question_contribution: str, question_meet: str, invites: str, founder_video: str, company_id: str, createdAt: str, updatedAt: str, db: Session = Depends(get_db)):
    return crud_service.update_founder_by_id(db, id, name, email, linkedin_url, is_technical, age, gender, question_contribution, question_meet, invites, founder_video, company_id, createdAt, updatedAt)

@router.delete('/founder/id', response_model=schemas.Founder)
def delete_founder_by_id(id: int, db: Session = Depends(get_db)):
    return crud_service.delete_founder_by_id(db, id)

@router.get('/support_inquiry/', response_model=List[schemas.SupportInquiry])
def get_all_support_inquiry(db: Session = Depends(get_db)):
    return crud_service.get_all_support_inquiry(db)

@router.get('/support_inquiry/id', response_model=schemas.SupportInquiry)
def get_support_inquiry_by_id(id: int, db: Session = Depends(get_db)):
    return crud_service.get_support_inquiry_by_id(db, id)

@router.post('/support_inquiry/', response_model=schemas.SupportInquiry)
def create_support_inquiry(id: str, created_at: str, status: str, phone: str, email: str, desc: str, name: str, updated_at: str, reapply_count: str, alternative_email: str, app_user: str, db: Session = Depends(get_db)):
    return crud_service.create_support_inquiry(db, id, created_at, status, phone, email, desc, name, updated_at, reapply_count, alternative_email, app_user)

@router.put('/support_inquiry/id/', response_model=schemas.SupportInquiry)
def update_support_inquiry_by_id(id: str, created_at: str, status: str, phone: str, email: str, desc: str, name: str, updated_at: str, reapply_count: str, alternative_email: str, app_user: str, db: Session = Depends(get_db)):
    return crud_service.update_support_inquiry_by_id(db, id, created_at, status, phone, email, desc, name, updated_at, reapply_count, alternative_email, app_user)

@router.delete('/support_inquiry/id', response_model=schemas.SupportInquiry)
def delete_support_inquiry_by_id(id: int, db: Session = Depends(get_db)):
    return crud_service.delete_support_inquiry_by_id(db, id)

@router.get('/company/', response_model=List[schemas.Company])
def get_all_company(db: Session = Depends(get_db)):
    return crud_service.get_all_company(db)

@router.get('/company/id', response_model=schemas.Company)
def get_company_by_id(id: int, db: Session = Depends(get_db)):
    return crud_service.get_company_by_id(db, id)

@router.post('/company/', response_model=schemas.Company)
def create_company(id: str, name: str, about: str, company_url: str, product_demo_video: str, product_url: str, why_apply_here: str, createdAt: str, updatedAt: str, db: Session = Depends(get_db)):
    return crud_service.create_company(db, id, name, about, company_url, product_demo_video, product_url, why_apply_here, createdAt, updatedAt)

@router.put('/company/id/', response_model=schemas.Company)
def update_company_by_id(id: str, name: str, about: str, company_url: str, product_demo_video: str, product_url: str, why_apply_here: str, createdAt: str, updatedAt: str, db: Session = Depends(get_db)):
    return crud_service.update_company_by_id(db, id, name, about, company_url, product_demo_video, product_url, why_apply_here, createdAt, updatedAt)

@router.delete('/company/id', response_model=schemas.Company)
def delete_company_by_id(id: int, db: Session = Depends(get_db)):
    return crud_service.delete_company_by_id(db, id)

