from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
result = [0]*(n+1)
depth = [-1]*(n+1)

# initialization
for _ in range(m):
    from_, to_ = map(int, input().split())
    graph[from_].append(to_)
    # if undirected graph
    graph[to_].append(from_)

for i in range(1, n+1):
    graph[i].sort()                 

# DFS algorithm
cnt = 1
def dfs(graph, start_node, curr_depth = 0):
    global cnt
    visited[start_node] =True
    result[start_node] = cnt
    cnt += 1
    depth[start_node] = curr_depth

    for adj_node in graph[start_node]:
        if not visited[adj_node]:
            dfs(graph, adj_node, curr_depth+1)

dfs(graph, v)
# print(*depth[1:], sep='\n') # 24480, 24481번
# 24482번
sum = 0
for i in range(1, n+1):
    sum+=result[i] * depth[i]
print(sum)