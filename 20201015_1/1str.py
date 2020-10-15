A = input().lower()
print(len({A[i:i+2] for i in range(len(A)-1) if A[i].isalpha() and A[i+1].isalpha()}))

