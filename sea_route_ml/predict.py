import joblib

# load model
model = joblib.load("model/marine_model.pkl")

def predict_risk(wind, wave, pressure, current, visibility):

    features = [[
        wind,
        wave,
        pressure,
        current,
        visibility
    ]]

    probability = model.predict_proba(features)[0][1]

    return probability
