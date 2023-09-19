from collections import deque
import sys

N, M = map(int, input().split())

mat = []
for i in range(N) : 
    rawstring = input()
    row = []
    for _ in range(M):
        row.append(int(rawstring[_]))
    mat.append(row)

n_steps = [[0]*M for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#print(mat, n_steps)
def BFS(graph, N_, M_):
    x0, y0 = 0, 0
    search_queue = deque()
    search_queue.append((x0, y0))
    n_steps[x0][y0] = 1

    while search_queue:
        #print(search_queue)
        #print(n_steps)
        x_prev, y_prev = search_queue.popleft()
        if (x_prev, y_prev) == (N_-1, M_-1):
            return n_steps[N_-1][M_-1]
        for i in range(4):
            x_next, y_next = x_prev+dx[i], y_prev+dy[i]
            if (0<=x_next) and (x_next<N_) and (0<=y_next) and (y_next<M_):
                if (mat[x_next][y_next] == 1) and (n_steps[x_next][y_next] == 0):
                    search_queue.append((x_next, y_next))
                    n_steps[x_next][y_next] = n_steps[x_prev][y_prev]+1
    return -1
print(BFS(mat, N, M))

