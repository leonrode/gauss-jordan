matrix = [[1, 1, 2, 8], [-1, -2, 3, 1], [3, -7, 4, 10]]

def multiply(row, value):
  return list(map(lambda x: value * x, row))

def add(row1, row2):
  return [a + b for a, b in zip(row1, row2)]

for i, row in enumerate(matrix):
  inverse = 1 / row[i]
  matrix[i] = multiply(row, inverse)
  # now go throw each other row and add by some multiple of top row
  for j, other_row in enumerate(matrix):
    if j != i:
      value = other_row[i]
      matrix[j] = add(other_row, multiply(matrix[i], -value))

print(matrix)