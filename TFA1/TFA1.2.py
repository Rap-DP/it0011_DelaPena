f_name = input("Enter your first name: ")
l_name = input("Enter your last name: ")
full_name = f_name + " " + l_name
up_full_name = f_name.upper() + " " + l_name.upper()
low_full_name = f_name.lower() + " " + l_name.lower()
length = len(full_name)
print("Full Name:", full_name)
print("Full Name (Upper Case):", up_full_name)
print("Full Name (Lower Case):", low_full_name)
print("Length of Full Name:", length)

