import numpy as np
import matplotlib.pyplot as plt
import random

# Constants
g = 9.81  # Gravity, m/s^2


def projectile_motion(func_angle, func_v0, func_mass, func_diameter, func_Cd, rho_air, theta_terrain, fun_initHeight,
                      time_step=0.01,
                      air_resistance=True):
    """
    Simulates the projectile motion with or without air resistance, including variable terrain height.

    Parameters:
    func_angle (float): Launch angle in degrees
    func_v0 (float): Initial speed in m/s
    func_mass (float): Mass of the projectile in kg
    func_diameter (float): Diameter of the projectile in meters
    func_Cd (float): Drag coefficient
    rho_air (float): Air density in kg/m^3
    theta_terrain (float): Terrain slope angle in degrees
    fun_initHeight (float): Initial height of the projectile
    time_step (float): Time step for the simulation in seconds
    air_resistance (bool): Enable or disable air resistance

    Returns:
    np.array: Arrays of x and y positions over time
    """
    # Convert angles to radians
    theta = np.radians(func_angle)
    theta_terrain_rad = np.radians(theta_terrain)

    # Initial conditions
    x, y = 0, fun_initHeight  # Initial position (y starts at initial height)
    vx, vy = func_v0 * np.cos(theta), func_v0 * np.sin(theta)  # Initial velocity components

    A = np.pi * (func_diameter / 2) ** 2  # Cross-sectional area of the projectile
    t = 0  # Time

    x_positions = []
    y_positions = []

    # Loop until the projectile hits the descending ground
    while y >= (fun_initHeight - x * np.tan(theta_terrain_rad)):
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
        t += time_step
        vx += ax * time_step
        vy += ay * time_step
        x += vx * time_step
        y += vy * time_step

    return np.array(x_positions), np.array(y_positions)


def main():
    # Create a simple menu to choose simulation settings
    print("Projectile Motion Simulation Menu:")

    # Select number of plot iterations
    iter1 = int(input("Enter the number of iterations (number of plot sets): "))

    # Select air resistance mode
    print("Select air resistance mode:")
    print("1 - Both (with and without air resistance)")
    print("2 - Only with air resistance")
    print("3 - Only without air resistance")
    resistance_mode = int(input("Enter your choice (1, 2, or 3): "))

    # Parameters
    angles = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]  # List of launch angles to simulate
    initHeight = 1500  # Initial height, m
    theta_terrain = 45  # Terrain slope angle, adjustable
    original_rho_air = 1.225  # Air density in kg/m^3
    Cd = 0.47  # Drag coefficient for a sphere

    for i in range(iter1):
        # Random generation of parameters
        diameter = random.randint(2, 100) / 1000  # Random diameter in meters
        v0 = random.randint(10, 150)  # Random initial speed in m/s
        mass = random.randint(1, 100) / 1000  # Random mass in kg

        # Define which scenarios to simulate based on user choice
        if resistance_mode == 1:
            simulate_with_resistance = [True, False]  # Both with and without air resistance
        elif resistance_mode == 2:
            simulate_with_resistance = [True]  # Only with air resistance
        elif resistance_mode == 3:
            simulate_with_resistance = [False]  # Only without air resistance
        else:
            print("Invalid selection. Defaulting to both.")
            simulate_with_resistance = [True, False]

        for with_resistance in simulate_with_resistance:  # One simulation with and one without air resistance
            # Reset rho_air based on the air resistance flag
            rho_air = original_rho_air if with_resistance else 0

            resistance_label = "With Air Resistance" if with_resistance else "No Air Resistance"

            # Plotting
            plt.figure(figsize=(12, 8))  # Increased figure size for better spacing
            for angle in angles:
                x, y = projectile_motion(angle, v0, mass, diameter, Cd, rho_air, theta_terrain, initHeight,
                                         air_resistance=with_resistance)
                plt.plot(x, y, label=f'Angle {angle}°')

            # Plot formatting
            plt.title(f'Projectile Motion {resistance_label}\n(v0={v0} m/s, mass={mass} kg, diameter={diameter} m)',
                      fontsize=16)
            plt.xlabel('Distance (m)', fontsize=14)
            plt.ylabel('Height (m)', fontsize=14)
            plt.legend(loc='upper right', bbox_to_anchor=(1.25, 1))  # Adjusted legend position
            plt.grid(True)

            # Plot the descending terrain line (thicker line)
            x_terrain = np.linspace(0, max(x), 100)
            y_terrain = initHeight - x_terrain * np.tan(np.radians(theta_terrain))  # Terrain height decreases with x
            plt.plot(x_terrain, y_terrain, 'r--', linewidth=3, label=f'Terrain (slope={theta_terrain}°')  # Thicker terrain line

            # Adjust layout to avoid overlap between elements
            plt.tight_layout(rect=[0, 0, 0.85, 1])  # Adjust the layout to accommodate the legend and text

            # Show the plot
            plt.show()


main()
