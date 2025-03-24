def divide(a, b):
    if b == 0:
        return None
    return a / b

def exponentiate(a, b):
    return a ** b

def remainder(a, b):
    if b == 0:
        return None
    return a % b

def summation(a, b):
    if a > b:
        return None
    return sum(range(a, b + 1))

def main():
    while True:
        print("==============================")
        print("Choose an operation:")
        print("[D] - Divide")
        print("[E] - Exponentiation")
        print("[R] - Remainder")
        print("[F] - Summation")
        print("[Q] - Quit")
        print("==============================\n")
        choice = input("Enter your choice: ").upper()
        
        if choice == 'Q':
            break
        
        if choice in ['D', 'E', 'R', 'F']:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue
            
            if choice == 'D':
                result = divide(num1, num2)
            elif choice == 'E':
                result = exponentiate(num1, num2)
            elif choice == 'R':
                result = remainder(num1, num2)
            elif choice == 'F':
                result = summation(int(num1), int(num2))
            
            if result is None:
                print("Invalid operation.")
            else:
                print(f"The result is: {result}")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()