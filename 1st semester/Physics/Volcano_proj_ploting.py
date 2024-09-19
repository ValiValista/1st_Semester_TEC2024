import numpy as np
import matplotlib.pyplot as plt
import random

# Constants
g = 9.81  # Gravity, m/s^2


def projectile_motion(func_angle, func_v0, func_mass, func_diameter, func_Cd, rho_air, time_step=0.01,
                      air_resistance=True):
    """
    Simulates the projectile motion with or without air resistance for a given launch angle and initial speed.

    Parameters:
    func_angle (float): Launch angle in degrees
    func_v0 (float): Initial speed in m/s
    func_mass (float): Mass of the projectile in kg
    func_diameter (float): Diameter of the projectile in meters
    func_Cd (float): Drag coefficient
    rho_air (float): Air density in kg/m^3
    time_step (float): Time step for the simulation in seconds
    air_resistance (bool): Enable or disable air resistance

    Returns:
    np.array: Arrays of x and y positions over time
    """
    # Convert angle to radians
    theta = np.radians(func_angle)

    # Initial conditions
    x, y = 0, 0  # Initial position
    vx, vy = func_v0 * np.cos(theta), func_v0 * np.sin(theta)  # Initial velocity components

    A = np.pi * (func_diameter / 2) ** 2  # Cross-sectional area of the projectile
    t = 0  # Time

    x_positions = []
    y_positions = []

    while y >= 0:  # Loop until the projectile hits the ground
        x_positions.append(x)
        y_positions.append(y)

        # Velocity magnitude
        v = np.sqrt(vx ** 2 + vy ** 2)

        if air_resistance:
            # Air resistance force
            F_drag = 0.5 * func_Cd * A * rho_air * v ** 2
            F_drag_x = F_drag * (vx / v)
            F_drag_y = F_drag * (vy / v)
        else:
            F_drag_x = 0
            F_drag_y = 0

        # Accelerations
        ax = -F_drag_x / func_mass
        ay = -g - (F_drag_y / func_mass)

        # Update velocity and position
        vx += ax * time_step
        vy += ay * time_step
        x += vx * time_step
        y += vy * time_step
        t += time_step

    return np.array(x_positions), np.array(y_positions)


def main():
    iter1 = 0

    # Parameters
    angles = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]  # List of launch angles to simulate
    original_rho_air = 1.225  # Air density in kg/m^3
    Cd = 0.47  # Drag coefficient for a sphere

    while iter1 < 2:  # Adjust the number of iterations as needed
        # Random generation of parameters
        diameter = random.randint(2, 100) / 1000  # Random diameter in meters
        v0 = random.randint(10, 150)  # Random initial speed in m/s
        mass = random.randint(1, 100) / 1000  # Random mass in kg

        for with_resistance in [True, False]:  # One simulation with and one without air resistance
            # Reset rho_air based on the air resistance flag
            rho_air = original_rho_air if with_resistance else 0

            resistance_label = "With Air Resistance" if with_resistance else "No Air Resistance"

            # Plotting
            plt.figure(figsize=(10, 6))
            for angle in angles:
                x, y = projectile_motion(angle, v0, mass, diameter, Cd, rho_air, air_resistance=with_resistance)
                plt.plot(x, y, label=f'Angle {angle}°')

            # Plot formatting
            plt.title(f'Projectile Motion {resistance_label} (v0={v0} m/s, mass={mass} kg, diameter={diameter} m)')
            plt.xlabel('Distance (m)')
            plt.ylabel('Height (m)')
            plt.legend()
            plt.grid(True)
            plt.show()

        iter1 += 1


main()
