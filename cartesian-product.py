a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a <= b:
  x = list(range(a, b + 1))
else:
  x = list(range(a, b - 1, -1))

if c <= d:
  y = list(range(c, d + 1))
else:
  y = list(range(c, d - 1, -1))

for i in range(len(x)):
  for j in range(len(y)):
    pair = "(" + str(x[i]) + ", " + str(y[j]) + ")"
    if j == len(y) - 1:
      print(pair)
    else:
      print(pair, end="")
