# <space>fw map(lambda ...)
# it does not return a list and i assumed that it did so whenever you call an index
# method that will error
# lsp errors should find that for you so just fix it there and should be good

from pakudex import Pakudex

def error(msg):
    raise Exception(msg)

def print_menu():
    print("")
    print("Pakudex Main Menu")
    print("-----------------")
    print("1. List Pakuri")
    print("2. Show Pakuri")
    print("3. Add Pakuri")
    print("4. Evolve Pakuri")
    print("5. Sort Pakuri")
    print("6. Exit")
    print("")

def get_capacity():
    while True:
        try:
            user_input = int(input("Enter max capacity of the Pakudex: "))

            # if its negative error out of the try block
            if user_input < 0:
                assert 1 == 2, "I could have used another print statement and continue but this works too"
    
            return user_input
        except Exception:
            print("Please enter a valid size.")

def main():
    # welcome message and get capacity
    print("Welcome to Pakudex: Tracker Extraordinaire!")
    capacity = get_capacity()
    print(f"The Pakudex can hold {str(capacity)} species of Pakuri.")

    # create the pakudex
    dex = Pakudex(capacity)

    while True:
        print_menu()

        user_choice = input("What would you like to do? ")

        # List Pakuri
        if user_choice == "1":
            # check to see if list is empty
            if len(dex.critters_list) == 0:
                print("No Pakuri in Pakudex yet!")
            else:
                print("Pakuri In Pakudex:")
                for i in range(len(dex.critters_list)):
                    name = dex.critters_list[i].species
                    print(f"{str(i + 1)}. {name}")

        # Show Pakuri
        elif user_choice == "2":
            # prompt for species
            user_input = input("Enter the name of the species to display: ")

            if user_input in map(lambda critter: critter.species, dex.critters_list):
                # get the critter
                names_list = list(map(lambda critter: critter.species, dex.critters_list))
                critter_index = names_list.index(user_input)
                critter = dex.critters_list[critter_index]

                # print the deets!
                print("")
                print(f"Species: {critter.species}")
                print(f"Attack: {critter.attack}")
                print(f"Defense: {critter.defense}")
                print(f"Speed: {critter.speed}")
            else:
                print("Error: No such Pakuri!")

        # Add Pakuri
        elif user_choice == "3":
            # check for failure conditions
            if len(dex.critters_list) == dex.capacity:
                print("Error: Pakudex is full!")
                continue

            # prompt user for input
            species = input("Enter the name of the species to add: ")

            # check for failure conditions
            if species in map(lambda critter: critter.species, dex.critters_list):
                print("Error: Pakudex already contains this species!")
                continue

            # add the pakuri
            dex.add_pakuri(species)
            print(f"Pakuri species {species} successfully added!")

        # Evolve Pakuri
        elif user_choice == "4":
            # prompt user for input
            species = input("Enter the name of the species to evolve: ")

            # check for failure conditions
            if not ( species in map(lambda critter: critter.species, dex.critters_list) ):
                print("Error: No such Pakuri!")
                continue

            # evolve it and print the message
            dex.evolve_species(species)
            print(f"{species} has evolved!")

        # Sort Pakuri
        elif user_choice == "5":
            dex.sort_pakuri()
            print("Pakuri have been sorted!")

        # Exit
        elif user_choice == "6":
            print("Thanks for using Pakudex! Bye!")
            return

        else:
            print("Unrecognized menu selection!")

if __name__ == "__main__":
    main()
