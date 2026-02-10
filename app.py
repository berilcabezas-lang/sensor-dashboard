import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Industrial Sensor Dashboard")

# simulate sensor data
n = st.slider("Number of samples", 50, 500, 200)

t = np.linspace(0, 10, n)
signal = np.sin(t) + np.random.normal(0, 0.1, n)

# anomaly injection
if st.checkbox("Inject anomaly"):
    idx = np.random.randint(10, n-10)
    signal[idx:idx+5] += 2

# anomaly score (simple std)
anomaly_score = float(np.std(signal))

st.write(f"Anomaly score: {anomaly_score:.3f}")

# plot
fig, ax = plt.subplots()
ax.plot(signal)
ax.set_title("Sensor Signal")
st.pyplot(fig)