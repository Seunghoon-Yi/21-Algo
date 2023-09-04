import sys
from collections import deque
input = sys.stdin.readline

# Cases
N_cases = int(input())

# dx and dy
dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

# BFS to search
def BFS(graph, r1, c1, r2, c2, N_chess):
    search_queue = deque()
    search_queue.append((r1, c1))
    graph[r1][c1] = 0

    while search_queue:
        x_prev, y_prev = search_queue.popleft()
        if (x_prev, y_prev) == (r2, c2):
            return graph[x_prev][y_prev]
        for i in range(8):
            x_next, y_next = x_prev+dx[i], y_prev+dy[i]
            if (0<=x_next) and (x_next < N_chess) and (0<=y_next) and (y_next < N_chess):   # 범위 만족하고
                if graph[x_next][y_next] == -1 :                                # 순회 안했으면
                    search_queue.append((x_next, y_next))
                    graph[x_next][y_next] = graph[x_prev][y_prev]+1

    return -1

trials = []
for cases in range(N_cases):
    N_chess = int(input())
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    graph = [[-1]*N_chess for _ in range(N_chess)]      # store depths

    trials.append(BFS(graph, r1, c1, r2, c2, N_chess))

for t in trials:
    print(t)



