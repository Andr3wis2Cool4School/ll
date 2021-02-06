import pandas as pd 
import numpy as np


l = [[0, 2, 1, 0], [0, 1, 0, 1]]

df = pd.DataFrame(l)

print(df)

def pondSize(land):
    if len(land) == 0:
        return 0

    n = len(land)
    m = len(land[0])

    res = []
    def dfs(i, j):
        land[i][j] = 0
        area = 1
        for (dx, dy) in [(i+1, j), (i-1, j), (i, j+1), (i, j-1), (i+1, j+1), (i+1, j-1), (i-1, j+1), (i-1, j-1)]:
            if dx>=0 and  dx<n and dy>=0 and dy<m and land[dx][dy] == 0:
                area += dfs(dx,dy)
        return area

    for i in range(n):
        for j in range(m):
            if land[i][j] == 0:
                res.append(dfs(i, j))

    res.sort()
#    res = res.sort()
    return res

       
print(pondSize(l))
