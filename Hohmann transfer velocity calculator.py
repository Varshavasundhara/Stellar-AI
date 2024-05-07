import math

# Function to calculate Hohmann transfer velocity
def calculate_hohmann_transfer_velocity(primary_radius, secondary_radius):
    # Gravitational constant in m^3 kg^-1 s^-2
    G = 6.67430e-11
    # Delta-v for Hohmann transfer formula
    delta_v = math.sqrt(G * (2 / primary_radius - 2 / (primary_radius + secondary_radius)))
    return delta_v

# Function to get user input and calculate Hohmann transfer velocity
def get_user_input_and_calculate():
    try:
        primary_radius = float(input("Enter the radius of the primary body (in meters): "))
        secondary_radius = float(input("Enter the radius of the secondary body (in meters): "))
        # Call the function to calculate Hohmann transfer velocity
        delta_v = calculate_hohmann_transfer_velocity(primary_radius, secondary_radius)
        print("Hohmann transfer velocity:", delta_v, "m/s")
    except ValueError:
        print("Please enter valid numbers.")

# Call the function to get user input and calculate Hohmann transfer velocity
get_user_input_and_calculate()
