import sys
import math
from collections import deque
input = sys.stdin.readline


primes = [1, 2]
primes_4 = []
def get_4_primes():
    for i in range(2, 10000):
        is_p = True
        for p in primes[1:]:
            if i%p == 0:
                is_p = False
        if is_p:
            primes.append(i)
            if i>1000:
                primes_4.append(i)
get_4_primes()

N_cases = int(input())

def BFS(inp, tgt):
    if tgt not in primes_4:
        return "Impossible"
    if inp == tgt:
        return 0
    search_queue = deque()
    search_queue.append((inp, 0)) # number, depth

    visited = [0 for _ in range(10000)]
    visited[inp] = 1

    while search_queue : 
        curr, depth = search_queue.popleft()
        curr = str(curr)

        for dgt in range(4):
            for nums in range(10):
                candidate = int(curr[:dgt] + str(nums) + curr[dgt+1:])
                if (candidate in primes_4) and (visited[candidate] == 0):
                    search_queue.append((candidate, depth+1))
                    visited[candidate] = 1
                    if candidate == tgt:
                        return depth+1

for _ in range(N_cases):
    inp, tgt = map(int, input().split())
    print(BFS(inp, tgt))




