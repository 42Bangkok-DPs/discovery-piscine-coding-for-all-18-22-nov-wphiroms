#!/usr/bin/env python3

def main():
    try:
        # Prompt the user for input
        number = float(input("Enter a number: "))

        # Determine if the number is positive, negative, or zero
        if number < 0:
            print("This number is negative.")
        elif number > 0:
            print("This number is positive.")
        else:
            print("This number is both positive and negative.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
