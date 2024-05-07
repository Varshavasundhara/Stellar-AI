import math

# Function to calculate escape velocity
def calculate_escape_velocity(mass, radius):
    # Gravitational constant in m^3 kg^-1 s^-2
    G = 6.67430e-11
    # Escape velocity formula
    escape_velocity = math.sqrt(2 * G * mass / radius)
    return escape_velocity

# Function to get user input and calculate escape velocity
def get_user_input_and_calculate():
    try:
        mass = float(input("Enter the mass of the celestial body (in kilograms): "))
        radius = float(input("Enter the radius of the celestial body (in meters): "))
        # Call the function to calculate escape velocity
        escape_velocity = calculate_escape_velocity(mass, radius)
        print("Escape velocity:", escape_velocity, "m/s")
    except ValueError:
        print("Please enter valid numbers.")

# Call the function to get user input and calculate escape velocity
get_user_input_and_calculate()

