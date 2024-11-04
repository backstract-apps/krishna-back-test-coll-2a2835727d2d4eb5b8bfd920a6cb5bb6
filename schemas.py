from pydantic import BaseModel

import datetime

import uuid

from typing import Any, Dict, List, Tuple

class OtpLog(BaseModel):
    id: uuid.UUID
    created_at: datetime.time
    email: str
    ip: str
    type: str
    attempts: float
    updated_at: datetime.time


class ReadOtpLog(BaseModel):
    id: uuid.UUID
    created_at: datetime.time
    email: str
    ip: str
    type: str
    attempts: float
    updated_at: datetime.time
    class Config:
        from_attributes = True


class DemoInquiry(BaseModel):
    created_at: datetime.time
    name: str
    email: str
    phone: str
    profession: float
    desc: str
    status: float
    updated_at: datetime.time
    reapply_count: float
    id: uuid.UUID


class ReadDemoInquiry(BaseModel):
    created_at: datetime.time
    name: str
    email: str
    phone: str
    profession: float
    desc: str
    status: float
    updated_at: datetime.time
    reapply_count: float
    id: uuid.UUID
    class Config:
        from_attributes = True


class Founder(BaseModel):
    id: int
    name: str
    email: str
    linkedin_url: str
    is_technical: str
    age: str
    gender: str
    question_contribution: str
    question_meet: str
    invites: str
    founder_video: str
    company_id: int
    createdAt: datetime.time
    updatedAt: datetime.time


class ReadFounder(BaseModel):
    id: int
    name: str
    email: str
    linkedin_url: str
    is_technical: str
    age: str
    gender: str
    question_contribution: str
    question_meet: str
    invites: str
    founder_video: str
    company_id: int
    createdAt: datetime.time
    updatedAt: datetime.time
    class Config:
        from_attributes = True


class SupportInquiry(BaseModel):
    id: uuid.UUID
    created_at: datetime.time
    status: float
    phone: str
    email: str
    desc: str
    name: str
    updated_at: datetime.time
    reapply_count: float
    alternative_email: str
    app_user: bool


class ReadSupportInquiry(BaseModel):
    id: uuid.UUID
    created_at: datetime.time
    status: float
    phone: str
    email: str
    desc: str
    name: str
    updated_at: datetime.time
    reapply_count: float
    alternative_email: str
    app_user: bool
    class Config:
        from_attributes = True


class Company(BaseModel):
    id: int
    name: str
    about: str
    company_url: str
    product_demo_video: str
    product_url: str
    why_apply_here: str
    createdAt: datetime.time
    updatedAt: datetime.time


class ReadCompany(BaseModel):
    id: int
    name: str
    about: str
    company_url: str
    product_demo_video: str
    product_url: str
    why_apply_here: str
    createdAt: datetime.time
    updatedAt: datetime.time
    class Config:
        from_attributes = True


