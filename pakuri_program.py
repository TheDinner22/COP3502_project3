from pakudex import Pakudex

def error(msg):
    raise Exception(msg)

def print_menu():
    print("Pakudex Main Menu")
    print("-----------------")
    print("1. List Pakuri")
    print("2. Show Pakuri")
    print("3. Add Pakuri")
    print("4. Evolve Pakuri")
    print("5. Sort Pakuri")
    print("6. Exit")

def get_capacity():
    try:
        user_input = input("Enter max capacity of the Pakudex: ")
        return int(user_input)
    except Exception:
        error("capacity of the Pakudex must be an int")

def menu_input():
    try:
        user_input = int(input("What would you like to do?"))

        if user_input < 1 or user_input > 6:
            error("this error will exit the try block")

        return user_input
    except Exception:
        error("menu choices must be of type: int AND must be between 1-6 inclusive")

def main():
    # welcome message and get capacity
    print("Welcome to Pakudex: Tracker Extraordinaire!")
    capacity = get_capacity()
    print(f"The Pakudex can hold {str(capacity)} species of Pakuri.")

    # create the pakudex
    dex = Pakudex(capacity)

    while True:
        print_menu()

        user_choice = menu_input()

        # List Pakuri
        if user_choice == 1:
            if len(dex.critters_list) == 0:
                print("No Pakuri in Pakudex yet!")
            else:
                for i in range(len(dex.critters_list)):
                    name = dex.critters_list[i].species
                    print(f"{str(i + 1)}. {name}")

        # Show Pakuri
        elif user_choice == 2:
            pass

        # Add Pakuri
        elif user_choice == 3:
            pass

        # Evolve Pakuri
        elif user_choice == 4:
            pass

        # Sort Pakuri
        elif user_choice == 5:
            pass

        # Exit
        elif user_choice == 6:
            print("Thanks for using Pakudex! Bye!")
            return

        else:
            error("unreachable")

if __name__ == "__main__":
    main()
