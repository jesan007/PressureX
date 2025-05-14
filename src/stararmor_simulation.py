# File: src/stararmor_simulation.py

"""
Simulates a basic shear-thickening fluid (STF) behavior under pressure scenarios.
This is a conceptual model to demonstrate how the STF would respond to dynamic loading.
"""

import numpy as np
import matplotlib.pyplot as plt
from layer_config import STFLayerConfig

def simulate_stf_response(config, pressures):
    """
    Simulate STF viscosity change under varying pressures.
    :param config: STFLayerConfig object
    :param pressures: list or np.array of pressure values (in Pascals)
    :return: list of effective viscosities
    """
    viscosities = []
    for P in pressures:
        # Simple exponential increase based on pressure
        effective_viscosity = config.viscosity_base * (1 + config.hardening_coefficient * np.log1p(P/1e3))
        viscosities.append(effective_viscosity)
    return viscosities

if __name__ == "__main__":
    config = STFLayerConfig()

    # Simulate pressure sweep from 0 to 50,000 Pascals (approximate launch stress)
    pressures = np.linspace(0, 50000, 500)
    viscosities = simulate_stf_response(config, pressures)

    # Plotting
    plt.figure(figsize=(10, 5))
    plt.plot(pressures, viscosities, label="Effective Viscosity (Pa·s)", color='blue')
    plt.xlabel("Pressure (Pa)")
    plt.ylabel("Viscosity (Pa·s)")
    plt.title("STF Viscosity Response to Pressure")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("outputs/stf_response_plot.png")
    plt.show()
