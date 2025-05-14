import numpy as np
import matplotlib.pyplot as plt

# Physical constants and parameters
mass = 0.5  # kg
velocity = 50  # m/s
area = 0.01  # m^2
stf_thickness = 0.02  # meters
density = 1200  # kg/m^3 (STF)
viscosity_base = 0.5  # baseline viscosity
hardening_coefficient = 3.0  # how much viscosity increases with shear rate

# Shear thickening response function
def shear_viscosity(shear_rate):
    return viscosity_base * (1 + hardening_coefficient * shear_rate)

# Impact simulation
def simulate_impact(time_steps=1000):
    dt = 0.0001  # time step
    velocity_local = velocity
    position = 0
    positions = []
    velocities = []

    for t in range(time_steps):
        shear_rate = abs(velocity_local / stf_thickness)
        viscosity = shear_viscosity(shear_rate)
        
        # Damping force from STF
        damping_force = -viscosity * velocity_local
        
        # Acceleration = F/m
        acceleration = damping_force / mass
        velocity_local += acceleration * dt
        position += velocity_local * dt

        positions.append(position)
        velocities.append(velocity_local)

        # Stop if almost zero velocity
        if abs(velocity_local) < 0.01:
            break

    return positions, velocities

# Run and visualize the simulation
if __name__ == "__main__":
    positions, velocities = simulate_impact()

    fig, ax1 = plt.subplots()

    color = 'tab:blue'
    ax1.set_xlabel('Time Step')
    ax1.set_ylabel('Position (m)', color=color)
    ax1.plot(positions, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()
    color = 'tab:red'
    ax2.set_ylabel('Velocity (m/s)', color=color)
    ax2.plot(velocities, color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()
    plt.title("STF Impact Simulation")
    plt.show()
