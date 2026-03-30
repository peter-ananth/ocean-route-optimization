import streamlit as st
import folium
from streamlit_folium import folium_static

from routes import generate_routes
from optimizer import evaluate_route

# example ports
ports = {
    "Chennai": (13.0827, 80.2707),
    "Singapore": (1.3521, 103.8198)
}

st.title("Sea Route Optimization using ML")

start_port = st.selectbox("Start Port", ports.keys())
end_port = st.selectbox("End Port", ports.keys())

if st.button("Find Best Route"):

    start = ports[start_port]
    end = ports[end_port]

    routes = generate_routes(start, end)

    best_route = None
    best_score = 999

    for route in routes:

        score = evaluate_route(route)

        if score < best_score:

            best_score = score
            best_route = route

    st.write("Best Route Risk Score:", best_score)

    map = folium.Map(location=start, zoom_start=4)

    for point in best_route:

        folium.Marker(point).add_to(map)

    folium_static(map)
