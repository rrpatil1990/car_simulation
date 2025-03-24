def rotate_left(direction):
    """Rotate 90 degrees left"""
    directions = ['N', 'E', 'S', 'W']
    current_index = directions.index(direction)
    return directions[(current_index - 1) % 4]


def rotate_right(direction):
    """Rotate 90 degrees right"""
    directions = ['N', 'E', 'S', 'W']
    current_index = directions.index(direction)
    return directions[(current_index + 1) % 4]


def move_forward(x, y, direction, width, height):
    """Move the car forward """
    moves = {
        'N': (0, 1),
        'E': (1, 0),
        'S': (0, -1),
        'W': (-1, 0)
    }
    dx, dy = moves[direction]
    new_x = x + dx
    new_y = y + dy

    if 0 <= new_x < width and 0 <= new_y < height:
        return new_x, new_y
    return x, y


def run_commands(car, width, height):
    """Execute the commands for a car"""
    name, x, y, direction, commands = car
    for command in commands:
        if command == 'L':
            direction = rotate_left(direction)
        elif command == 'R':
            direction = rotate_right(direction)
        elif command == 'F':
            x, y = move_forward(x, y, direction, width, height)
    return x, y, direction


def display_cars(cars):
    """Display the list of cars"""
    if not cars:
        print("No cars have been added to the simulation.")
    else:
        print("Your current list of cars are:")
        for car in cars:
            print(f"- {car[0]}, ({car[1]}, {car[2]}) {car[3]}, {car[4]}")


def main():
    print("Welcome to Auto Driving Car Simulation!")

    width, height = map(int, input("Please enter the width and height of the simulation field in x y format: ").split())
    print(f"You have created a field of {width} x {height}.\n")

    cars = []  # List to store cars

    while True:
        print("\nPlease choose from the following options:")
        print("[1] Add a car to field")
        print("[2] Run simulation")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            name = input("Please enter the name of the car: ").strip()

            while True:
                try:
                    x, y, direction = input(
                        f"Please enter initial position of car {name} in x y Direction format: ").split()
                    x, y = int(x), int(y)
                    if direction not in ['N', 'S', 'E', 'W']:
                        raise ValueError("Invalid direction. Please enter one of N, S, E, W.")
                    break
                except ValueError as e:
                    print(e)

            commands = input(f"Please enter the commands for car {name}: ").strip().upper()

            cars.append((name, x, y, direction, commands))

            display_cars(cars)

        elif choice == '2':
            print("\nRunning simulation...\n")
            for i, car in enumerate(cars):
                print(i, car)
                name, x, y, direction, commands = car
                x, y, direction = run_commands(car, width, height)
                cars[i] = (name, x, y, direction, commands)
                print(f"{name} has moved to ({x}, {y}) facing {direction}.")

            print("\nFinal positions of cars after simulation:")
            display_cars(cars)

        else:
            print("Invalid choice. Please enter 1 or 2.")

        cont = input("\nDo you want to continue? (y/n): ").strip().lower()
        if cont != 'y':
            print("Exiting the simulation. Goodbye!")
            break


if __name__ == "__main__":
    main()
