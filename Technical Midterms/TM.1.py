file = open("Technical Midterms/numbers.txt", 'r')
lines = file.readlines()
file.close()

line_number = 1
for line in lines:
    numbers = line.strip().split(',')
    if all(num.isdigit() for num in numbers):
        numbers = [int(num) for num in numbers]
        total_sum = sum(numbers)
        if str(total_sum) == str(total_sum)[::-1]:
            print(f"Line {line_number}: {line.strip()} (sum {total_sum}) - Palindrome")
        else:
            print(f"Line {line_number}: {line.strip()} (sum {total_sum}) - Not a palindrome")
    line_number += 1
