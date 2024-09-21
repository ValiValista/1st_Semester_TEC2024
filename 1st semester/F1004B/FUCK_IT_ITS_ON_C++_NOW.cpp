#include <iostream>
#include <cmath>
#include <vector>
#include <random>
#include <matplotlibcpp.h>

namespace plt = matplotlibcpp;

// Constants
const double g = 9.81;  // Gravity, m/s^2

// Function to simulate projectile motion
std::pair<std::vector<double>, std::vector<double>> projectile_motion(double func_angle, double func_v0, double func_mass,
                                                                      double func_diameter, double func_Cd, double rho_air,
                                                                      double time_step = 0.01, bool air_resistance = true) {
    // Convert angle to radians
    double theta = func_angle * M_PI / 180.0;

    // Initial conditions
    double x = 0, y = 0;  // Initial position
    double vx = func_v0 * cos(theta), vy = func_v0 * sin(theta);  // Initial velocity components
    double A = M_PI * pow(func_diameter / 2, 2);  // Cross-sectional area of the projectile
    double t = 0;  // Time

    std::vector<double> x_positions;
    std::vector<double> y_positions;

    while (y >= 0) {  // Loop until the projectile hits the ground
        x_positions.push_back(x);
        y_positions.push_back(y);

        // Velocity magnitude
        double v = sqrt(vx * vx + vy * vy);

        double F_drag_x = 0, F_drag_y = 0;
        if (air_resistance) {
            // Air resistance force
            double F_drag = 0.5 * func_Cd * A * rho_air * v * v;
            F_drag_x = F_drag * (vx / v);
            F_drag_y = F_drag * (vy / v);
        }

        // Accelerations
        double ax = -F_drag_x / func_mass;
        double ay = -g - (F_drag_y / func_mass);

        // Update velocity and position
        vx += ax * time_step;
        vy += ay * time_step;
        x += vx * time_step;
        y += vy * time_step;
        t += time_step;
    }

    return std::make_pair(x_positions, y_positions);
}

int main() {
    // Initialize random number generator
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<> diameter_dist(0.002, 0.1);  // Random diameter in meters
    std::uniform_real_distribution<> v0_dist(10, 150);           // Random initial speed in m/s
    std::uniform_real_distribution<> mass_dist(0.001, 0.1);      // Random mass in kg

    // Parameters
    std::vector<int> angles = {5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85};  // Launch angles
    double original_rho_air = 1.225;  // Air density in kg/m^3
    double Cd = 0.47;  // Drag coefficient for a sphere

    int iter1 = 0;
    while (iter1 < 2) {
        // Random generation of parameters
        double diameter = diameter_dist(gen);
        double v0 = v0_dist(gen);
        double mass = mass_dist(gen);

        for (bool with_resistance : {true, false}) {
            // Adjust rho_air based on the air resistance flag
            double rho_air = with_resistance ? original_rho_air : 0;
            std::string resistance_label = with_resistance ? "With Air Resistance" : "No Air Resistance";

            // Plotting
            plt::figure_size(1000, 600);
            for (int angle : angles) {
                auto [x, y] = projectile_motion(angle, v0, mass, diameter, Cd, rho_air, 0.01, with_resistance);
                plt::plot(x, y, {{"label", "Angle " + std::to_string(angle) + "°"}});
            }

            // Plot formatting
            plt::title("Projectile Motion " + resistance_label + " (v0=" + std::to_string(v0) +
                       " m/s, mass=" + std::to_string(mass) + " kg, diameter=" + std::to_string(diameter) + " m)");
            plt::xlabel("Distance (m)");
            plt::ylabel("Height (m)");
            plt::legend();
            plt::grid(true);
            plt::show();
        }

        iter1++;
    }

    return 0;
}
