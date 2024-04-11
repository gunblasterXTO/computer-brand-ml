from joblib import load

from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from pandas import DataFrame

from app.models import (
    DevicePredictorRequest,
    DevicePredictorResponse,
    ErrorResponse
)
from utils.numerical_to_cat import credit_to_cat, salary_to_cat


app = FastAPI(title="Asus or Sony predictor", version="0.1.0")
model_registry = load("model/grid_search_model.pkl")


@app.post("/predict")
def predict_device(
    request: DevicePredictorRequest,
    model=model_registry
) -> JSONResponse:
    try:
        ml_model = model.get("model")
        boundary = model.get("utils", {}).get("boundary", {})

        credit_cat = credit_to_cat(request.credit, boundary.get("credit"))
        salary_cat = salary_to_cat(request.salary, boundary.get("salary"))

        input_df = DataFrame({
            "salary": [salary_cat],
            "age": [request.age],
            "elevel": [request.elevel],
            "car": [request.car],
            "zipcode": [request.zipcode],
            "credit": [credit_cat]
        })
        brand_cat = ml_model.predict(input_df)

        return JSONResponse(
            content=DevicePredictorResponse(brand=brand_cat).model_dump(),
            status_code=status.HTTP_200_OK
        )
    except Exception as err:
        return JSONResponse(
            content=ErrorResponse(detail=f"{err}").model_dump(),
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
