from collections import deque

x8 = [-1, -1, 0, 1, 1, 1, 0, -1]  # surrounding coordinates of a pixel
y8 = [0, -1, -1, -1, 0, 1, 1, 1]

def bfs(mat, i, j):
    q = deque()
    q.append((i, j))
    mat[i][j] = 0
    while(len(q) != 0):
        pidx = q.popleft()
        for k in range(8):
            ci = x8[k] + pidx[0]
            cj = y8[k] + pidx[1]
            if ci >= 0 and ci < len(mat) and cj >= 0 and cj < len(mat[0]) and mat[ci][cj] == 1:
                mat[ci][cj] = 0
                q.append((ci, cj))


def countPatch(mat, N, M):
    count = 0
    for i in range(N):
        for j in range(M):
            if mat[i][j] == 1:
                bfs(mat, i, j)
                count += 1
    return count   # returns the count of number of white patches

'''
Let the input given be in the form
N, M in the first line (where N = number of rows, M = number of columns)
N lines followed having M values present in each row
'''
N, M = map(int, input().strip().split())
mat = []
for n in range(N):
    mat.append(list(map(int, input().strip().split())))
result = countPatch(mat, N, M)
print(result)