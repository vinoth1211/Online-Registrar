from pymongo import MongoClient
from models.models import CertificateRequestModel, MarriageApplicationModel

client = MongoClient("mongodb+srv://admin:admin123@cluster0.rdqdkga.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
) 

db = client.data_db

collection_name_certificate = db["data_collection"]
collection_name_marraige = db["marraige_collection"]


def create_certificate_request(request_data: CertificateRequestModel):
    request_dict = request_data.dict(by_alias=True)
    collection_name_certificate.insert_one(request_dict)
    return request_data

def create_marriage_application(data: MarriageApplicationModel):
    data_dict = data.dict(by_alias=True)
    collection_name_marraige.insert_one(data_dict)
    return data