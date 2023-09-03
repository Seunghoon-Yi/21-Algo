from collections import deque
# index starts from 1
n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

# initialization
for _ in range(m):
    from_, to_ = map(int, input().split())
    graph[from_].append(to_)
    # if undirected graph
    graph[to_].append(from_)
for i in range(1, n+1):
    graph[i].sort()

# DFS algorithm
def dfs(graph, start_node):
    visited[start_node] =True
    print(start_node, end=' ')

    for adj_node in graph[start_node]:
        if not visited[adj_node]:
            dfs(graph, adj_node)

dfs(graph, v)
print()

# BFS algorithm
# Initialize visited list
visited = [False] * (n+1)

def bfs(graph, start_node):
    search_queue = deque()
    search_queue.append(start_node)
    while search_queue:
        search_node = search_queue.popleft()
        if not visited[search_node]:
            visited[search_node] = True
            print(search_node, end=' ')

            for adj_node in graph[search_node]:
                search_queue.append(adj_node)

bfs(graph, v)