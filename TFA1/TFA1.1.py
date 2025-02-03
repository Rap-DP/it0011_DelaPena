f_name = input("Enter your first name: ")
l_name = input("Enter your last name: ")
age = input("Enter your age: ")
sliced_name = f_name[:3]
print("Sliced Name: ", sliced_name)
print("Full Name:", f_name+" "+l_name)
print("Greeting Message: Hello,",sliced_name," Welcome. You are ", age ," years old.")