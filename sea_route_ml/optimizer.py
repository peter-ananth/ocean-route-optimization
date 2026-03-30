from weather import get_weather
from ocean import get_ocean
from predict import predict_risk

def evaluate_route(route):

    total_risk = 0

    for lat, lon in route:

        wind, pressure, visibility = get_weather(lat, lon)

        wave, current = get_ocean(lat, lon)

        risk = predict_risk(
            wind,
            wave,
            pressure,
            current,
            visibility
        )

        total_risk += risk

    return total_risk
