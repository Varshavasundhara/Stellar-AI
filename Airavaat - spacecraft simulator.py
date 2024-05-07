import time

class Spacecraft:
    def __init__(self, name, crew):
        self.name = name
        self.crew = crew
        self.position = (0, 0, 0)
    
    def move(self, direction, distance):
        if direction == 'forward':
            self.position = (self.position[0] + distance, self.position[1], self.position[2])
        elif direction == 'backward':
            self.position = (self.position[0] - distance, self.position[1], self.position[2])
        elif direction == 'up':
            self.position = (self.position[0], self.position[1] + distance, self.position[2])
        elif direction == 'down':
            self.position = (self.position[0], self.position[1] - distance, self.position[2])
        elif direction == 'right':
            self.position = (self.position[0], self.position[1], self.position[2] + distance)
        elif direction == 'left':
            self.position = (self.position[0], self.position[1], self.position[2] - distance)
    
    def display_position(self):
        print(f"{self.name} is currently at position: {self.position}")

def main():
    print("Welcome to Space Exploration Simulator!")
    spacecraft_name = input("Enter the name of your spacecraft: ")
    crew_size = int(input("Enter the number of crew members: "))
    crew = []
    for i in range(crew_size):
        crew.append(input(f"Enter the name of crew member {i+1}: "))
    
    spacecraft = Spacecraft(spacecraft_name, crew)
    print("Spacecraft initialized.")
    time.sleep(1)
    
    while True:
        print("\nOptions:")
        print("1. Move spacecraft")
        print("2. Display current position")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            direction = input("Enter direction (forward, backward, up, down, right, left): ")
            distance = float(input("Enter distance (in meters): "))
            spacecraft.move(direction, distance)
            print("Spacecraft moved.")
        elif choice == '2':
            spacecraft.display_position()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
