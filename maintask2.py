N = 5     # N * N chessboard

row = [2, 1, -1, -2, -2, -1, 1, 2, 2]
col = [1, 2, 2, 1, -1, -2, -2, -1, 1]


def isValid(x, y):
    return not (x < 0 or y < 0 or x >= N or y >= N)


def knightTour(visited, x, y, pos):
    visited[x][y] = pos
    
    if pos >= N * N:
        print('\n'.join([str(r) for r in visited]), end='\n\n')
        visited[x][y] = 0
        return None


    for k in range(8):
        newX = x + row[k]
        newY = y + col[k]

        if isValid(newX, newY) and visited[newX][newY] == 0:
            knightTour(visited, newX, newY, pos + 1)

    visited[x][y] = 0


visited = [[0 for x in range(N)] for y in range(N)]
pos = 1


knightTour(visited, 0, 0, pos)