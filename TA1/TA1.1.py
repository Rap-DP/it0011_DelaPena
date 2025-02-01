vowels = "aeiouAEIOU"
num_vowels = 0
num_consonants = 0
num_spaces = 0
num_others = 0

input_string = input("Enter a string: ")

for char in input_string:
    if char in vowels:
        num_vowels += 1
    elif char.isalpha():
        num_consonants += 1
    elif char.isspace():
        num_spaces += 1
    else:
        num_others += 1

print("-----------------------------")
print("String inputted: ", input_string)
print("Vowels: ", num_vowels)
print("Consonants: ", num_consonants)
print("Spaces: ", num_spaces)
print("Other characters: ", num_others)