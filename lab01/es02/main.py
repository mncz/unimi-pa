alkaline_earth_metals = [
    ("barium", 56), 
    ("beryllium", 4), 
    ("calcium", 20), 
    ("magnesium", 12), 
    ("radium", 88), 
    ("strontium", 38)
]

# Write a one-liner that returns the highest atomic number in 
# alkaline_earth_metals
print(sorted(alkaline_earth_metals, key=lambda a: a[1])[-1])

# Using one of the list methods, sort alkaline_earth_metals in ascending order 
# (from the lightest to the heaviest).
print(sorted(alkaline_earth_metals, key=lambda a: a[1]))

# Transform the alkaline_earth_metals into a dictionary using the name of the 
# metals as the dictionary's key.
alkaline_earth_metals = {k: v for k, v in alkaline_earth_metals}

# Create a second dictionary containing the noble gases -- helium (2), 
# neon (10), argon (18), krypton (36), xenon (54), and radon (86) -- and store 
# it in the variable noble_gases.
noble_gases = {
    "helium": 2,
    "neon": 10,
    "argon": 18,
    "krypton": 36,
    "xenon": 54,
    "radon": 86
}

# Merge the two dictionaries and print the result as couples (name, 
# atomic number) sorted in ascending order on the element names.
alkaline_earth_metals.update(noble_gases)
print(sorted([(k, alkaline_earth_metals[k]) for k in alkaline_earth_metals]))