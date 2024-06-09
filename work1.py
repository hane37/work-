def dfs(graph, visited, v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, visited, i) 

def cheriyan_mehlhorn_gabow():
    n = int(input())
    graph = for _ in range(n)
    for _ in range(n-1):
        u, v = map(int, input().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    
    for i in range(n):
        if not visited[i]:
            components += 1