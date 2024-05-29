from volume_calculator import VolumeCalculator

def main():
    while True:
        print("\nVolume Calculator")
        print("1. Cube")
        print("2. Sphere")
        print("3. Cylinder")
        print("4. Cone")
        print("5. Exit")

        choice = input("Choose a shape to calculate its volume (1-5): ")

        if choice == '1':
            side_length = float(input("Enter the side length of the cube: "))
            try:
                volume = VolumeCalculator.cube(side_length)
                print(f"The volume of the cube is: {volume}")
            except ValueError as e:
                print(e)
        elif choice == '2':
            radius = float(input("Enter the radius of the sphere: "))
            try:
                volume = VolumeCalculator.sphere(radius)
                print(f"The volume of the sphere is: {volume}")
            except ValueError as e:
                print(e)
        elif choice == '3':
            radius = float(input("Enter the radius of the cylinder: "))
            height = float(input("Enter the height of the cylinder: "))
            try:
                volume = VolumeCalculator.cylinder(radius, height)
                print(f"The volume of the cylinder is: {volume}")
            except ValueError as e:
                print(e)
        elif choice == '4':
            radius = float(input("Enter the radius of the cone: "))
            height = float(input("Enter the height of the cone: "))
            try:
                volume = VolumeCalculator.cone(radius, height)
                print(f"The volume of the cone is: {volume}")
            except ValueError as e:
                print(e)
        elif choice == '5':
            print("Exiting the volume calculator. Goodbye!")
            break
        else:
            print("Invalid choice, please select a valid option (1-5).")

if __name__ == "__main__":
    main()
