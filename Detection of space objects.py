import math

class SpaceObject:
    def __init__(self, name, position):
        self.name = name
        self.position = position
    
    def distance_to(self, other_object):
        x1, y1, z1 = self.position
        x2, y2, z2 = other_object.position
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
        return distance

def main():
    print("Welcome to Space Object Detection Simulator!")
    object_name = input("Enter the name of the space object: ")
    x = float(input("Enter the x-coordinate of the object's position: "))
    y = float(input("Enter the y-coordinate of the object's position: "))
    z = float(input("Enter the z-coordinate of the object's position: "))
    
    space_object = SpaceObject(object_name, (x, y, z))
    
    while True:
        print("\nOptions:")
        print("1. Add another space object")
        print("2. Detect nearby objects")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            object_name = input("Enter the name of the space object: ")
            x = float(input("Enter the x-coordinate of the object's position: "))
            y = float(input("Enter the y-coordinate of the object's position: "))
            z = float(input("Enter the z-coordinate of the object's position: "))
            new_space_object = SpaceObject(object_name, (x, y, z))
            print("Space object added.")
        elif choice == '2':
            radius = float(input("Enter the detection radius (in meters): "))
            print("Space objects within the detection radius:")
            for obj in [space_object, new_space_object]:
                distance = space_object.distance_to(obj)
                if distance <= radius:
                    print(f"{obj.name} (Distance: {distance} meters)")
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()