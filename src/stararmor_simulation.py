import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Constants
pressure_threshold = 10.0  # Pressure at which STF stiffens (arbitrary units)
max_stress = 100.0  # Maximum stress that STF can withstand

# STF material model (shear-thickening)
def stf_response(pressure, time):
    """
    Simulates the shear-thickening response of the fluid under pressure.
    Under normal conditions, the fluid is soft, but it hardens under high pressure.
    """
    # Response function (simple model for STF behavior)
    stiffness = np.where(pressure > pressure_threshold, max_stress, 0)
    return stiffness

# Time array (for simulation)
time = np.linspace(0, 10, 1000)  # Simulating over 10 arbitrary units of time
pressure = np.linspace(0, 20, 1000)  # Pressure from 0 to 20 arbitrary units

# Calculate the STF response
stiffness_response = stf_response(pressure, time)

# Plot the results: Stress vs Pressure
plt.figure(figsize=(10, 6))
plt.plot(pressure, stiffness_response, label="STF Response", color="blue")
plt.title("Shear-Thickening Fluid Response to Pressure")
plt.xlabel("Pressure (arbitrary units)")
plt.ylabel("Material Stiffness (arbitrary units)")
plt.grid(True)
plt.legend()
plt.show()
