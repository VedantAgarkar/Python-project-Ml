import pickle

model = pickle.load(open("heart_disease_model.sav", "rb"))

# Input: supposed-to-be healthy
X = [[35, 0, 3, 120, 180, 0, 0, 170, 0, 0.0, 2, 0, 1]]

print("Prediction:", model.predict(X))
