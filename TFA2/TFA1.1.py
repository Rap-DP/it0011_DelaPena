f_name = input("Enter your first name: ")
l_name = input("Enter your last name: ")
age = input("Enter your age: ")
sliced_name = f_name[:3]
greeting_message = "Greeting Message: Hello, {}! Welcome. You are {} years old.".format(sliced_name, age)
print("Sliced Name:", sliced_name)
print("Full Name:", f_name + " " + l_name)
print(greeting_message)