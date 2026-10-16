a = [1, 3, 4]
b = "abc"

X = list(zip(a, b))

print(X)

Y, Z = zip(*X)

print(Y)
print(Z)
