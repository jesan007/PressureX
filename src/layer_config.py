# File: src/layer_config.py

"""
This module defines tunable parameters for the STF (shear-thickening fluid) layer
that may be used by multiple simulation or modeling modules. Allows for quick adjustment
of thickness, membrane properties, and fluid dynamics settings.
"""

class STFLayerConfig:
    def __init__(self):
        # Core physical parameters
        self.stf_thickness_m = 0.02  # meters
        self.stf_density_kg_m3 = 1200  # typical for STF slurry

        # Shear-thickening model settings
        self.viscosity_base = 0.5  # Pa.s
        self.hardening_coefficient = 3.0  # Dimensionless scale-up factor

        # Membrane durability settings (idealized values for future tuning)
        self.outer_membrane_material = "titanium-alloy"
        self.inner_membrane_material = "TPU-based flex wrap"
        self.seal_integrity_rating = 9.7  # Arbitrary scale, 0-10

    def summary(self):
        return {
            "Thickness (m)": self.stf_thickness_m,
            "Density (kg/m^3)": self.stf_density_kg_m3,
            "Viscosity Base (Pa.s)": self.viscosity_base,
            "Hardening Coefficient": self.hardening_coefficient,
            "Outer Membrane": self.outer_membrane_material,
            "Inner Membrane": self.inner_membrane_material,
            "Seal Integrity Rating": self.seal_integrity_rating,
        }


# Example usage (for import elsewhere):
# from layer_config import STFLayerConfig
# config = STFLayerConfig()
# print(config.summary())
