i = 1
while i <= 5:
    j = 5
    while j > i:
        print(end="")
        j -= 1
    k = 1
    while k <= i * 2 - 1:  
        print(i * 2 - 1, end="")
        k += 1
    print("")  
    i += 1