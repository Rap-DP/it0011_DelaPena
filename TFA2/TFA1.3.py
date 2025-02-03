l_name = input("Enter your last name: ")
f_name = input("Enter your first name: ")
age = input("Enter your age: ")
contact = input("Enter your contact number: ")
course = input("Enter your course: ")

f = open("TFA2\\students.txt", "a")
f.write("Last Name: " + l_name +"\n")
f.write("First Name: " + f_name +"\n")
f.write("Age: "+ age +"\n")
f.write("Contact Number: " + contact +"\n")
f.write("Course: " + course +"\n")
    
print("Student information has been saved to students.txt")
