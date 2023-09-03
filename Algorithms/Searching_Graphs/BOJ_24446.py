from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, m, start = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
result = [0]*(n+1)
depth = [-1]*(n+1)

for _ in range(m):
    from_, to_ = map(int, input().split())
    graph[from_].append(to_)
    # if undirected graph
    graph[to_].append(from_)
for i in range(1, n+1):
    graph[i].sort()            


# BFS algorithm
curr_depth = 0
cnt = 1
def bfs(graph, start_node):
    global curr_depth
    global cnt
    search_queue = deque()
    search_queue.append((curr_depth, start_node))
    depth[start_node] = curr_depth

    while search_queue:
        curr_depth, search_node = search_queue.popleft()
        if not visited[search_node]:
            visited[search_node] = True
            depth[search_node] = curr_depth
            result[search_node] = cnt
            cnt+=1

            for adj_node in graph[search_node]:
                search_queue.append((curr_depth+1, adj_node))


bfs(graph, start)
#print(*depth[1:], sep='\n') # 24446번
sum_di_ti = 0
for i in range(1, n+1):
    sum_di_ti += result[i]*depth[i] # 24447번
print(sum_di_ti)
