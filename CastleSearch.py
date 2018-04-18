#!/bin/python3

import sys

def minimumMoves(grid, startX, startY, goalX, goalY):
    n = len(grid)
    visited = set()
    visited.add((startX, startY))
    def helper(originalX, originalY):
        directly_reachable = []
        x = originalX
        y = originalY
        for i in range(x + 1, n):
            if grid[i][y] == ".":
                directly_reachable.append((i,y))
            else:
                break
        for i in range(x - 1, -1, -1):
            if grid[i][y] == ".":
                directly_reachable.append((i, y))
            else:
                break
        for j in range(y - 1, -1, -1):
            if grid[x][j] == ".":
                directly_reachable.append((x, j))
            else:
                break
        for j in range(y + 1, n):
            if grid[x][j] == ".":
                directly_reachable.append((x, j))
            else:
                break
        return directly_reachable

    estimated = [[2 << 30] * n for x in range(n)]
    estimated[startX][startY] = 0

    frontier = set(helper(startX, startY))

    step = 1
    while frontier:
        new_frontier = set()
        for node in frontier:
            visited.add(node)
        for node in frontier:
            estimated[node[0]][node[1]] = step
            for nbr in set(helper(node[0], node[1])):
                if nbr not in visited:
                    new_frontier.add(nbr)
        frontier = new_frontier
        step += 1
    return estimated[goalX][goalY]

if __name__ == "__main__":
    n = int(input().strip())
    grid = []
    for i in range(n):
        grid.append([x for x in input().strip()])
    startX, startY, goalX, goalY = input().strip().split(' ')
    startX, startY, goalX, goalY = [int(startX), int(startY), int(goalX), int(goalY)]
    result = minimumMoves(grid, startX, startY, goalX, goalY)
    print(result)