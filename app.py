import streamlit as st
import pandas as pd
import time

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #4e73df, #1cc88a);
    }

    h1, h2, h3, h4, h5, h6, p, label {
        color: white !important;
        font-weight: 900;
    }
    /* Dropdown styling */
div[data-baseweb="select"] > div {
    background-color: white !important;
    border-radius: 8px;
}

/* Text input styling */
input {
    background-color: white !important;
    border-radius: 8px;
}

/* Button styling */
.stButton > button {
    background-color:  #1f4e79 !important;
    color:white !important ;
    font-weight: bold;
    border-radius: 8px;
    height: 45px;
    width: 180px;
    border: none;
}

.stButton > button:hover {
    background-color: #163a5f !important;
    color:white !important;
}

</style>
""",
unsafe_allow_html=True
)

# Load data
df = pd.read_csv("aqi.csv")

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

def convert_pollutant(value):
    mapping = {
        "PM2.5": "Fine Dust (PM2.5)",
        "PM10": "Dust Particles (PM10)",
        "O3": "Ozone Gas (O3)",
        "CO": "Carbon Monoxide (CO)",
        "SO2": "Sulphur Dioxide (SO2)"
    }
    
    pollutants = value.split(",")
    readable = [mapping.get(p.strip(), p) for p in pollutants]
    
    return " & ".join(readable)
df["prominent_pollutant_readable"] = df["prominent_pollutants"].apply(convert_pollutant)
st.title("AQI PREDICTION APP")

# 🔹 State dropdown
state = st.selectbox("Select State", sorted(df["state"].dropna().unique()))
filtered_state = df[df["state"] == state]

# 🔹 Area dropdown
area = st.selectbox("Select Area", sorted(filtered_state["area"].dropna().unique()))
filtered_area = filtered_state[filtered_state["area"] == area]

# 🔹 Prominent Pollutant dropdown
pollutant = st.selectbox(
    "Prominent Pollutant",
    sorted(filtered_area["prominent_pollutant_readable"].dropna().unique())
)

filtered_pollutant = filtered_area[
    filtered_area["prominent_pollutant_readable"] == pollutant
]

# 🔥 Get dataset exact value
if not filtered_pollutant.empty:
    total_stations = filtered_pollutant["number_of_monitoring_stations"].iloc[0]
else:
    total_stations = 0

# 🔥 Show in Text Box
st.text_input(
    "Total No. of Monitoring Stations",
    value=str(int(total_stations)),
      # User edit panna mudiyadhu
)

st.markdown("---")

# 🔥 Predict Button
if st.button("🔮 Predict AQI"):

    with st.spinner("Calculating AQI... Please wait ⏳"):
        time.sleep(1.5)

        filtered_pollutant = filtered_area[
            filtered_area["prominent_pollutant_readable"] == pollutant
        ]

        if not filtered_pollutant.empty:
            total_stations = int(filtered_pollutant["number_of_monitoring_stations"].iloc[0])
            aqi_value = int(filtered_area["aqi_value"].iloc[0])
            category = filtered_area["air_quality_status"].iloc[0]
            

        else:
            total_stations = 0
            aqi_value = 0
            category="No Data"

    st.success("Prediction Completed Successfully ✅")

    # 🔹 Show Monitoring Stations
    st.metric("Total Monitoring Stations", total_stations)

    # 🔹 AQI Category Logic
    if aqi_value <= 50:
        category = "Good 😊"
        color = "green"
    elif aqi_value <= 100:
        category = "Satisfactory 🙂"
        color = "lightgreen"
    elif aqi_value <= 200:
        category = "Moderate 😐"
        color = "orange"
    elif aqi_value <= 300:
        category = "Poor 😷"
        color = "red"
    else:
        category = "Very Poor / Severe ☠️"
        color = "darkred"

    # 🔥 Styled AQI Output
    st.markdown(
        f"""
        <div style="
           padding:20px;
            border-radius:10px;
            background-color:#1f4e79;
            color:white;
            text-align:center;
            font-size:22px;
            font-weight:600;">
            AQI Value: {aqi_value} <br><br>
            Category: {category}
        </div>
        """,
        unsafe_allow_html=True
    )