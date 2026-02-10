import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Industrial Sensor Dashboard")

st.title("Industrial Equipment Monitoring")

# controls
n = st.slider("Number of samples", 50, 500, 200)
inject = st.checkbox("Inject anomaly")

# simulate time series
t = np.linspace(0, 10, n)

vibration = np.sin(t) + np.random.normal(0, 0.1, n)
temperature = 60 + 2*np.sin(t/2) + np.random.normal(0, 0.3, n)
pressure = 5 + 0.5*np.sin(t/3) + np.random.normal(0, 0.05, n)

# anomaly injection
if inject:
    idx = np.random.randint(10, n-10)
    vibration[idx:idx+5] += 2
    temperature[idx:idx+5] += 5
    pressure[idx:idx+5] += 1

# anomaly score (simple example)
anomaly_score = float(np.std(vibration))

# status logic
if anomaly_score < 0.8:
    status = "OK"
    color = "green"
elif anomaly_score < 1.2:
    status = "WARNING"
    color = "orange"
else:
    status = "ALARM"
    color = "red"

# display metrics
col1, col2 = st.columns(2)

with col1:
    st.metric("Anomaly Score", f"{anomaly_score:.3f}")

with col2:
    st.markdown(f"### Status: :{color}[{status}]")

# plot signals
fig, ax = plt.subplots()
ax.plot(vibration, label="Vibration")
ax.plot(temperature, label="Temperature")
ax.plot(pressure, label="Pressure")
ax.legend()
ax.set_title("Sensor Signals")

st.pyplot(fig)