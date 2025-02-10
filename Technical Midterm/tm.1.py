txt_file = 'numbers.txt'

try:
    with open(txt_file, 'r') as file:
        lines = file.readlines()
except FileNotFoundError:
    print(f"Error: The file '{txt_file}' does not exist.")
    lines = []

for i, line in enumerate(lines):
    try:
        numbers = list(map(int, line.strip().split(',')))
        total_sum = sum(numbers)
        if str(total_sum) == str(total_sum)[::-1]:
            print(f"Line {i+1}: {line.strip()} (sum {total_sum}) - Palindrome")
        else:
            print(f"Line {i+1}: {line.strip()} (sum {total_sum}) - Not a palindrome")
    except ValueError:
        print(f"Line {i+1}: {line.strip()} - Error: Non-integer value found")
