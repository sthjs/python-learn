n = int(input())
k = int(input())
primes = []

for i in range(2, n + 1):
  is_prime = True
  for d in range(2, i):
    if i % d == 0:
      is_prime = False
  if is_prime:
    primes.append(i)

result = primes[:n + 1:k]
for i in range(len(result)):
  print(result[i], end="", sep=" ")
  if i < len(result) - 1:
    print(" ", end="")
print()
