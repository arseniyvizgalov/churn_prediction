from fastapi import FastAPI, Request, Form
import joblib
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import pandas as pd

app = FastAPI()
templates = Jinja2Templates(directory="scripts/templates")
model = joblib.load('models/model.pkl')

@app.get('/', response_class=HTMLResponse)
def form(request: Request):
    return templates.TemplateResponse('form.html', {"request": request})

@app.post("/predict", response_class=HTMLResponse)
def predict(request: Request,
            credit_score: int = Form(...),
            country: str = Form(...),
            gender: str = Form(...),
            age: int = Form(...),
            tenure: int = Form(...),
            balance: float = Form(...),
            products_number: int = Form(...),
            credit_card: int = Form(...),
            active_member: int = Form(...),
            estimated_salary: float = Form(...),
            ):

    input_data = pd.DataFrame([[
        credit_score,
        country,
        gender,
        age,
        tenure,
        balance,
        products_number,
        credit_card,
        active_member,
        estimated_salary
    ]], columns=[
        "credit_score",
        "country",
        "gender",
        "age",
        "tenure",
        "balance",
        "products_number",
        "credit_card",
        "active_member",
        "estimated_salary"
    ])

    prediction = model.predict(input_data)[0]

    return templates.TemplateResponse("result.html", {
        "request": request,
        "prediction": f'The customer {"has churned" if prediction == 1 else "has not churned"}'
    })