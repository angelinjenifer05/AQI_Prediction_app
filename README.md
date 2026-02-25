# 🌫️ AQI Prediction Web Application

## 📌 Project Overview

The **AQI Prediction App** is a web-based application developed using **Python and Streamlit** that allows users to analyze Air Quality Index (AQI) data based on State, Area, and Prominent Pollutants.

This project focuses on presenting air quality monitoring data in a simple, user-friendly, and human-understandable format.

---

## 🎯 Objective

The main objective of this project is to:

- Analyze air quality data
- Display prominent pollutants in human-readable format
- Show total number of monitoring stations
- Predict AQI category based on AQI value
- Provide an interactive and visually appealing dashboard

---

## 🛠️ Technologies Used

- **Python**
- **Streamlit**
- **Pandas**
- **HTML & CSS (for UI customization)**

---

## 📊 Dataset Details

The dataset contains:

- State
- Area
- Prominent Pollutants
- AQI Value
- Air Quality Status
- Number of Monitoring Stations

Column names were cleaned and standardized using:
- Lowercase conversion
- Removing extra spaces
- Replacing spaces with underscores

---

## 🚀 Key Features

### ✅ 1. Dynamic State & Area Selection
- Selecting a state filters corresponding areas.
- Selecting an area filters related pollutant data.

### ✅ 2. Human-Readable Pollutant Mapping
Technical pollutant codes like:
- `PM2.5`
- `PM10`
- `O3`
- `CO`
- `SO2`

Are converted into user-friendly names like:
- Fine Dust
- Coarse Dust
- Ozone Gas
- Carbon Monoxide
- Sulphur Dioxide

### ✅ 3. Monitoring Station Display
- Automatically fetches total number of monitoring stations from dataset.
- Displays in a non-editable text field.

### ✅ 4. AQI Category Prediction Logic

AQI value is categorized into:

| AQI Range  | Category               |
|------------|------------------------|
| 0–50       | Good 😊               |
| 51–100     | Satisfactory 🙂       |
| 101–200    | Moderate 😐           |
| 201–300    | Poor 😷               |
| 300+       | Very Poor / Severe ☠️ |


---

## 🧠 Data Processing & Logic

- Cleaned column names using Pandas.
- Applied dynamic pollutant mapping function.
- Used filtering logic based on user selection.
- Applied conditional logic to determine AQI category.

---

## 🧠 Future improvements


- Deploy on Streamlit Cloud

- Add AQI trend visualization charts

- Integrate real-time AQI API

- Add user authentication system

- Add downloadable report feature
---
## ▶️ How to Run the Project

### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
streamlit run app.py

---

