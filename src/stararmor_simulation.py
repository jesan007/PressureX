import matplotlib.pyplot as plt
import numpy as np

def simulate_stf_response(pressure_values):
    """Simulates the STF hardening response to varying pressure levels."""
    stiffness = []
    for p in pressure_values:
        # Shear-thickening modeled with exponential response
        s = 1 + 4 * np.tanh(p - 0.5)
        stiffness.append(s)
    return stiffness

if __name__ == "__main__":
    pressures = np.linspace(0, 2, 100)  # Simulated pressure from 0 to 2 arbitrary units
    stiffness_response = simulate_stf_response(pressures)

    plt.plot(pressures, stiffness_response, label="STF Stiffness")
    plt.xlabel("Applied Pressure")
    plt.ylabel("Material Stiffness")
    plt.title("STF Hardening Response Simulation")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("stf_response_plot.png")
    plt.show()
