from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, m, start = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
result = [0]*(n+1)

for _ in range(m):
    from_, to_ = map(int, input().split())
    graph[from_].append(to_)
    # if undirected graph
    graph[to_].append(from_)
for i in range(1, n+1):
    graph[i].sort()             # 24444번
    graph[i].sort(reverse=True) # 24445번

# BFS algorithm
cnt = 1
def bfs(graph, start_node):
    global cnt
    search_queue = deque()
    search_queue.append(start_node)
    while search_queue:
        search_node = search_queue.popleft()
        if not visited[search_node]:
            visited[search_node] = True
            result[search_node] = cnt
            cnt += 1
            for adj_node in graph[search_node]:
                search_queue.append(adj_node)

bfs(graph, start)
print(*result[1:], sep='\n')
