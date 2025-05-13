# Testing and Evaluation

## 1. Overview

The testing phase for PressureX aims to evaluate the effectiveness of the shear-thickening fluid (STF) under various conditions relevant to spacecraft missions, including launch, orbital flight, and reentry. The following tests and simulations have been designed:

## 2. STF Hardening Test

### Objective:
To test the response of STF under varying pressure and impact conditions.

### Method:
1. Apply incremental pressure to the STF layer.
2. Measure the dynamic stiffness response using a pressure sensor and a force gauge.
3. Record the STF's behavior in real-time during pressure application.

### Expected Outcome:
The STF should progressively harden with increasing pressure, and the stiffness curve should match the theoretical model.

### Tools:
- Pressure sensor
- Force gauge
- Data logger

## 3. Micrometeoroid Impact Test

### Objective:
To simulate the effect of micrometeoroid impacts on the STF layer and assess its damping effectiveness.

### Method:
1. Propel a small object (simulating a micrometeoroid) at the STF material at various speeds.
2. Measure impact energy absorption and material response.
3. Observe any residual damage or crack propagation in the material.

### Expected Outcome:
The STF should absorb most of the impact energy and prevent damage to the underlying structure.

## 4. Simulation Data

The Python simulation in `/src/stararmor_simulation.py` models STF behavior under various conditions, and it should be compared with real-world testing results for validation.

## 5. Conclusion

Future tests will explore STF longevity, temperature tolerance, and its performance in extreme reentry conditions.
