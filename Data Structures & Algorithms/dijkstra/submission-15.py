from typing import List, Dict

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
        dist = [float('inf')] * n
        visited = [False] * n
        dist[src] = 0
        for _ in range(n):
            u = -1
            best = float('inf')
            for i in range(n):
                if not visited[i] and dist[i] < best:
                    best = dist[i]
                    u = i
            if u == -1:
                break
            visited[u] = True
            for v, weight in graph[u]:
                if not visited[v] and dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
        return {i: (dist[i] if dist[i] != float('inf') else -1) for i in range(n)}