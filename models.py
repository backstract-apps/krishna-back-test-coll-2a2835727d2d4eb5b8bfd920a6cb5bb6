from sqlalchemy import Column, Integer, String, Boolean, DateTime, Time, Float, Text, ForeignKey, JSON, Numeric, Date, TIMESTAMP, UUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class OtpLog(Base):
    __tablename__ = 'otp_log'
    id = Column(UUID, primary_key=True)
    created_at = Column(Time, primary_key=False)
    email = Column(String, primary_key=False)
    ip = Column(String, primary_key=False)
    type = Column(String, primary_key=False)
    attempts = Column(String, primary_key=False)
    updated_at = Column(Time, primary_key=False)

class DemoInquiry(Base):
    __tablename__ = 'demo_inquiry'
    created_at = Column(Time, primary_key=False)
    name = Column(String, primary_key=False)
    email = Column(String, primary_key=False)
    phone = Column(String, primary_key=False)
    profession = Column(String, primary_key=False)
    desc = Column(String, primary_key=False)
    status = Column(String, primary_key=False)
    updated_at = Column(Time, primary_key=False)
    reapply_count = Column(String, primary_key=False)
    id = Column(UUID, primary_key=True)

class Founder(Base):
    __tablename__ = 'founder'
    id = Column(Integer, primary_key=True)
    name = Column(String, primary_key=False)
    email = Column(String, primary_key=False)
    linkedin_url = Column(String, primary_key=False)
    is_technical = Column(String, primary_key=False)
    age = Column(String, primary_key=False)
    gender = Column(String, primary_key=False)
    question_contribution = Column(String, primary_key=False)
    question_meet = Column(String, primary_key=False)
    invites = Column(String, primary_key=False)
    founder_video = Column(String, primary_key=False)
    company_id = Column(Integer, primary_key=False)
    createdAt = Column(Time, primary_key=False)
    updatedAt = Column(Time, primary_key=False)

class SupportInquiry(Base):
    __tablename__ = 'support_inquiry'
    id = Column(UUID, primary_key=True)
    created_at = Column(Time, primary_key=False)
    status = Column(String, primary_key=False)
    phone = Column(String, primary_key=False)
    email = Column(String, primary_key=False)
    desc = Column(String, primary_key=False)
    name = Column(String, primary_key=False)
    updated_at = Column(Time, primary_key=False)
    reapply_count = Column(String, primary_key=False)
    alternative_email = Column(String, primary_key=False)
    app_user = Column(Boolean, primary_key=False)

class Company(Base):
    __tablename__ = 'company'
    id = Column(Integer, primary_key=True)
    name = Column(String, primary_key=False)
    about = Column(String, primary_key=False)
    company_url = Column(String, primary_key=False)
    product_demo_video = Column(String, primary_key=False)
    product_url = Column(String, primary_key=False)
    why_apply_here = Column(String, primary_key=False)
    createdAt = Column(Time, primary_key=False)
    updatedAt = Column(Time, primary_key=False)

