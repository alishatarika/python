from fastapi import FastAPI
import numpy as np
from sklearn.linear_model import LinearRegression, LogisticRegression

app = FastAPI()

# -----------------------
# LINEAR REGRESSION DATA
# -----------------------
X = np.array([[1000,2],[1500,3],[2000,4]])
y = np.array([2000000,3500000,5000000])

model = LinearRegression()
model.fit(X, y)

# -----------------------
# LOGISTIC REGRESSION DATA (CLASSIFICATION)
# -----------------------
# 0 = Low price, 1 = High price
y_class = np.array([0, 1, 1])

model1 = LogisticRegression()
model1.fit(X, y_class)

# -----------------------
# ROUTES
# -----------------------

@app.get("/")
def home():
    return {"message": "API Running 🚀"}

# LINEAR REGRESSION
@app.post("/predict")
def predict(size: int, rooms: int):
    prediction = model.predict([[size, rooms]])
    return {"predicted_price": float(prediction[0])}

# LOGISTIC REGRESSION
@app.post("/predict-class")
def predict_class(size: int, rooms: int):
    prediction = model1.predict([[size, rooms]])[0]
    probability = model1.predict_proba([[size, rooms]])[0][1]

    return {
        "class": "High Price" if prediction == 1 else "Low Price",
        "probability": float(probability)
    }