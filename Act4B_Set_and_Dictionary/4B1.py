A = {'a', 'b', 'd', 'f', 'g', 'h'}
B = {'b', 'c', 'h', 'l', 'm', 'o'}
C = {'c', 'd', 'f', 'h', 'i', 'j', 'k'}

join_ab = A.union(B)
print("Number of elements in A and B:", len(join_ab))

difference_B_A_C = B - (A | C)
print("Number of elements in B not in A and C:", len(difference_B_A_C))

print("Set operations :")
print("i.", C - (A | B))  
print("ii.", C & (A | B))  
print("iii.", B & C)  
print("iv.", A & C)  
print("v.", (B & C) - A)  
print("vi.", B - (A | C))  
