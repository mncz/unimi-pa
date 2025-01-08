class Animal:
    species = 'Unknown'

    @classmethod
    def set_species(cls, species):
        cls.species = species

class Dog(Animal):
    pass
    

def main():
    print(Dog.species)
    Dog.set_species('Canis lupus')
    print(Dog.species)
    print(Animal.species)

if __name__ == '__main__':
    main()