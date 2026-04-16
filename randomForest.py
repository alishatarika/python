from sklearn.ensemble import RandomForestClassifier

# Sample dataset
X = [
    [6, 60, 7],   # Study, Attendance, Sleep
    [2, 50, 5],
    [8, 90, 6],
    [1, 40, 4]
]

y = ["Pass", "Fail", "Pass", "Fail"]

# Create model
model = RandomForestClassifier(n_estimators=3)

# Train
model.fit(X, y)

# Predict
prediction = model.predict([[6, 60, 7]])

print(prediction)