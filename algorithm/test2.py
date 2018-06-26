def h(n):
    if n <=7:
        return n
    else:
        return 2*h(n-1) + h(n-8)

y = [i for i in range(0,8)] + [0]*92

for i in range(8,100):
    y[i] = 2*y[i-1]+y[i-8]

print(y)
print(len(y))