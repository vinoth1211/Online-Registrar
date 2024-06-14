from pydantic import BaseModel, Field, EmailStr
from bson import ObjectId
from typing import Optional

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

    @classmethod
    def __get_pydantic_json_schema__(cls, schema, field):
        schema.update(type="string")

class CertificateRequestModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    phone: str
    nic: str
    email: EmailStr

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class MarriageApplicationModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    applicantName: str
    applicantAddress: str
    marriageType: str
    maleFullName: str
    femaleFullName: str
    registrarName: Optional[str] = None
    registrarOffice: Optional[str] = None
    registrationDivision: Optional[str] = None
    placeSolemnized: Optional[str] = None
    ministerName: Optional[str] = None
    churchSituation: Optional[str] = None
    district: str
    marriageDate: Optional[str] = None
    searchPeriod: Optional[str] = None
    applicantSignature: str
    
    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}