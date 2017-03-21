
n = int(raw_input().strip())

A = [[0 for x in range(n)] for y in range(n)]
B = [[0 for x in range(n)] for y in range(n)]

for x in range(0, n):
  for y in range(0, n):
    A[x][y] = int(raw_input().strip())

for x in range(0, n):
  for y in range(0, n):
    B[x][y] = int(raw_input().strip())


print A[0][0]

result = []
for x in range(n):

  row = []
  for y in range(n):
    product = 0
    for p in range(len(A[x])):
      product += A[x][p] * B[p][y]

    row.append(product)

  result.append(row)


print result
