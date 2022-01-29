from random import randrange

# Randomizes the matrix
def randomizer(x, matrix):
    for c in range(x):
        for r in range(x):
            matrix[c][r] = randrange(0, 2)
    return matrix


# Flood fill algorithm
def flood_fill(x, y, old, new, matrix, maxnum):
    theStack = [(x, y)]

    while len(theStack) > 0:

        x, y = theStack.pop()

        if x < 0 or x >= maxnum or y < 0 or y >= maxnum or matrix[x][y] != old:
            continue

        matrix[x][y] = new

        theStack.append((x + 1, y))

        theStack.append((x - 1, y))

        theStack.append((x, y + 1))

        theStack.append((x, y - 1))


# Conways game of life
def life(x, matrix):
    matrix_copy = matrix.copy()
    for c in range(x):
        for r in range(x):
            total = int(matrix[c, (r - 1) % x] + matrix[c, (r + 1) % x] +
                         matrix[(c - 1) % x, r] + matrix[(c + 1) % x, r] +
                         matrix[(c - 1) % x, (r - 1) % x] + matrix[(c - 1) % x, (r + 1) % x] +
                         matrix[(c + 1) % x, (r - 1) % x] + matrix[(c + 1) % x, (r + 1) % x])

            # apply Conway's rules
            if matrix[c, r] == 1:
                if (total < 2) or (total > 3):
                    matrix_copy[c, r] = 0
            else:
                if total == 3:
                    matrix_copy[c, r] = 1

    matrix[:] = matrix_copy[:]

    return matrix
