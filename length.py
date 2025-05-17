# !/user/bin/env.python3
# Created By: Enoch Amedjrovi
# Created on April 2
# This program ask the user to display the area and width then calculate the length


def calculate_length(area, width):
    # Function to calculate the length of the rectangle
    return area / width


def get_valid_input():
    # Using a while true statement
    while True:
        try:
            # Converting the user's input as a float
            value = float(input())
            return value
        except ValueError:
            print("Please enter a valid input.")


def main():
    # To calculate rectangle length
    print("Welcome to Enoch's Rectangle Length Calculator")

    # Get valid area input
    print("Enter the area of the rectangle: ")
    area = get_valid_input()

    # Get valid width input, ensure it's not zero
    while True:
        print("Enter the width of the rectangle: ")
        width = get_valid_input()
        if width == 0:
            print("Width cannot be zero! Please enter a non-zero value.")
        else:
            break

    # Calculate and display the length
    length = calculate_length(area, width)
    print(f"The length of the rectangle is: {length}")


if __name__ == "__main__":
    main()
