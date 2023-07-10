t = int(input())

while t > 0:
    n, m = input().split()
    n = int(n)
    m = int(m)

    if n < m:
        print(0)
    else:
        print(n - m)

    t -= 1
