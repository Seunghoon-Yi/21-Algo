import sys
from collections import deque
input = sys.stdin.readline

# Graph init
N = int(input())
graph = [[-1]*N for _ in range(N)] # store depths
r1, c1, r2, c2 = map(int, input().split())

# dx and dy
dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

# BFS to search
def BFS(graph, r1, c1, r2, c2):
    search_queue = deque()
    search_queue.append((r1, c1))
    graph[r1][c1] = 0

    while search_queue:
        x_prev, y_prev = search_queue.popleft()
        if (x_prev, y_prev) == (r2, c2):
            return graph[x_prev][y_prev]
        for i in range(6):
            x_next, y_next = x_prev+dx[i], y_prev+dy[i]
            if (0<=x_next) and (x_next < N) and (0<=y_next) and (y_next < N):   # 범위 만족하고
                if graph[x_next][y_next] == -1 :                                # 순회 안했으면
                    search_queue.append((x_next, y_next))
                    graph[x_next][y_next] = graph[x_prev][y_prev]+1

    return -1

print(BFS(graph, r1, c1, r2, c2))
