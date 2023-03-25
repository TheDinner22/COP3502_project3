from pakuri import Pakuri;

class Pakudex:
    # Initializes this object to contain exactly capacity objects when completely full. The default capacity for the
    # pakudex should be 20
    def __init__(self, capacity=20):
        self.capacity = capacity
        self.critters_list = [] # this is a list of Pakuri objects, not strings

    # Returns the number of critters currently being stored in the pakudex
    def get_size(self):
        return len(self.critters_list)

    # Returns the number of critters that the pakudex has the capacity to hold at most
    def get_capacity(self):
        return self.capacity

    # Returns a string list containing the species of the critters as ordered in the pakudex; if there are no species
    # added yet, this method should return # None
    def get_species_array(self):
        return None if len(self.critters_list) == 0 else list(map(lambda pakuri: pakuri.species, self.critters_list))

    # Returns an int list containing the attack, defense, and speed statistics of species at indices 0, 1, and 2
    # respectively; if species is not in the pakudex, returns # None
    #
    # the implementation of this function assumes that there are no dupelicate items in
    # self.critters_list
    def get_stats(self, species):
        names_list = list( map(lambda critter: critter.species, self.critters_list) )

        try:
            critter_index = names_list.index(species)
            critter = self.critters_list[critter_index]
            return [critter.attack, critter.defense, critter.speed]
        except Exception:
            return None

    # Sorts the pakuri objects in this pakudex according to Python standard lexicographical ordering of species name
    def sort_pakuri(self):
        self.critters_list.sort(key=lambda critter: critter.species)

    # Adds species to the pakudex; if successful, return True, and False otherwise
    #
    # this can fail if the pakudex is full or if the species is a dupelicate
    def add_pakuri(self, species):
        # check for failure conditions
        if len(self.critters_list) == self.capacity:
            return False

        if species in map(lambda critter: critter.species, self.critters_list):
            return False

        # add the species
        self.critters_list.append( Pakuri(species) )

        return True

    # Attempts to evolve species within the pakudex; if successful, return True, and False otherwise
    #
    # only fails if the species is not in the pakudex
    def evolve_species(self, species):
        # if the species is not in the pakudex, return false
        if not ( species in map(lambda critter: critter.species, self.critters_list) ):
            return False

        # evolve and return true
        names_list = list( map(lambda critter: critter.species, self.critters_list) )
        critter_index = names_list.index(species)
        critter = self.critters_list[critter_index]
        critter.evolve() # does this work????

        return True

