def yigindisi(N):
    yig = 0
    for i in range(1, N+1):
        if i % 2 != 0:
            yig += i
    return yig

N = int(input("N ni kiriting: "))
print(yigindisi(N))