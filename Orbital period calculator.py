import math

# Define a function to calculate the orbital period
def calculate_orbital_period(semi_major_axis):
    # Gravitational constant in m^3 kg^-1 s^-2
    G = 6.67430e-11
    # Mass of the Earth in kg
    M = 5.972e24
    # Orbital period formula
    T = 2 * math.pi * math.sqrt(semi_major_axis**3 / (G * M))
    return T

# Function to get user input and calculate the orbital period
def get_user_input_and_calculate():
    try:
        semi_major_axis = float(input("Enter the semi-major axis of the orbit in meters: "))
        # Call the function to calculate the orbital period
        orbital_period = calculate_orbital_period(semi_major_axis)
        print("Orbital period:", orbital_period, "seconds")
    except ValueError:
        print("Please enter a valid number.")

# Call the function to get user input and calculate the orbital period
get_user_input_and_calculate()

