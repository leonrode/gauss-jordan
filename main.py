matrix = [[1, 2, -3, 4, 12], [2, 2, -2, 3, 10], [0, 1, 1, 0, -1], [1, -1, 1, -2, -4]]

def multiply(row, value):
  return list(map(lambda x: value * x, row))

def add(row1, row2):
  return [a + b for a, b in zip(row1, row2)]

def print_matrix(matrix):
  print("\n".join(["   ".join([str(number) for number in row]) for row in matrix]))
  print("----------------")

for i, row in enumerate(matrix):
  inverse = 1 / row[i]
  matrix[i] = multiply(row, inverse)
  # now go throw each other row and add by some multiple of top row
  for j, other_row in enumerate(matrix):
    if j != i:
      value = other_row[i]
      matrix[j] = add(other_row, multiply(matrix[i], -value)) # add(other_row, row multiplied by additive inverse) to make 0
    print_matrix(matrix)
