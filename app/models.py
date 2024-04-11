from pydantic import BaseModel


class DevicePredictorRequest(BaseModel):
    salary: float
    credit: float
    elevel: int
    car: int
    age: int
    zipcode: int


class DevicePredictorResponse(BaseModel):
    message: str = "success"
    brand: int


class ErrorResponse(BaseModel):
    message: str = "error"
    detail: str
