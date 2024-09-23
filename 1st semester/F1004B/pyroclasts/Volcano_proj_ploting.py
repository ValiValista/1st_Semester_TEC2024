import numpy as np
import matplotlib.pyplot as plt
import random
import pandas as pd
import os

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
    original_rho_air = 1.225  # Air density in kg/m^3
    output_directory = r'C:\nonprivilegedprogramfiles\plotting'  # Output directory for CSV


    # Prompt the user for input choice
    use_custom_values = input(
        "Do you want to input custom values for initial speed, mass, and diameter? (yes/no): ").strip().lower()
    randomization_choice = input("Do you want to randomize initHeight, theta_terrain, and Cd for every iteration? (yes/no): ").strip().lower()

    if randomization_choice == 'yes':
        randomize = True
    else:
        randomize = False

    if use_custom_values == 'yes':
        v0 = float(input("Enter the initial speed (m/s): "))
        mass = float(input("Enter the mass (kg): "))
        diameter = float(input("Enter the diameter (m): "))
        Cd = float(input("Enter the drag coefficient: "))  # Drag coefficient input

        # Select initial height and terrain slope angle
        initHeight = int(input("Enter the initial height of the projectile: "))  # Initial height of the projectile
        theta_terrain = int(input("Enter the terrain slope angle in degrees: "))  # Terrain slope angle, adjustable

    else:
        # Random generation of parameters
        diameter = random.randint(2, 100) / 1000  # Random diameter in meters
        v0 = random.randint(10, 150)  # Random initial speed in m/s
        mass = random.randint(1, 100) / 1000  # Random mass in kg
        Cd = random.randint(1, 100) / 100  # Random drag coefficient
        initHeight = random.randint(0,2000)  # Initial height of the projectile
        theta_terrain = random.randint(0, 90)  # Terrain slope angle in degrees




    results = []  # Store results for CSV

    for i in range(iter1):

        if randomize:
            # Random generation of parameters
            initHeight = random.randint(0, 2000)
            theta_terrain = random.randint(0, 90)
            Cd = random.randint(1, 100) / 100  # Random drag coefficient
        elif not randomize:
            initHeight = initHeight
            theta_terrain = theta_terrain
            Cd = Cd
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
                iteration_num = i + 1
                plt.plot(x, y, label=f'Angle {angle}°')
                # Store results for CSV
                for x_pos, y_pos in zip(x, y):
                    results.append({
                        'Angle': angle,
                        'V0 (m/s)': v0,
                        'Mass (kg)': mass,
                        'Diameter (m)': diameter,
                        'Cd': Cd,
                        'Terrain Slope (°)': theta_terrain,
                        'Initial Height (m)': initHeight,
                        'With Air Resistance': with_resistance,
                        'X Position (m)': x_pos,
                        'Y Position (m)': y_pos,
                        'Iteration': iteration_num
                    })
            # Plot formatting
            plt.title(f'Projectile Motion {resistance_label}\n(v0={v0} m/s, mass={mass} kg, diameter={diameter} m, Terrain slope={theta_terrain}°, Initial height={initHeight} m, Cd={Cd}, Iteration #{iteration_num})',
                      fontsize=12)
            plt.xlabel('Distance (m)', fontsize=14)
            plt.ylabel('Height (m)', fontsize=14)
            plt.legend(loc='upper right', bbox_to_anchor=(1.25, 1))  # Adjusted legend position
            plt.grid(True)

            # Plot the descending terrain line (thicker line)
            x_terrain = np.linspace(0, max(x), 100)
            y_terrain = initHeight - x_terrain * np.tan(np.radians(theta_terrain))  # Terrain height decreases with x
            plt.plot(x_terrain, y_terrain, 'r--', linewidth=3, label=f'Terrain (slope={theta_terrain}°')  # Thicker terrain line

            # Adjust layout to avoid overlap between elements
            plt.tight_layout(rect=[0.1, 0.02, 0.8, 1])  # Adjust the layout to accommodate the legend and text

            # Show the plot
            plt.show()
    # Create a DataFrame from results and export to CSV
    df = pd.DataFrame(results)
    # Create the directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    df.to_csv('projectile_motion_results.csv', index=False)


    print("Results exported to 'projectile_motion_results.csv'.")

main()
