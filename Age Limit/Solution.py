# cook your dish here
T = int(input())

for _ in range(T):
    X, Y, A = input().split()
    X = int(X)
    Y = int(Y)
    A = int(A)

    if A >= X and A < Y:
        print("YES")
    else:
        print("NO")
    