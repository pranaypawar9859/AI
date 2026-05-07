from collections import deque 
 
# Undirected graph 
graph = { 
    'A': ['B', 'C'], 
    'B': ['A', 'D', 'E'], 
    'C': ['A', 'E'], 
    'D': ['B'], 
    'E': ['B', 'C'] 
} 
 
# DFS (Recursive) 
def dfs(graph, node, visited=None): 
    if visited is None: 
        visited = set() 
 
    visited.add(node) 
    print(node, end=" ") 
 
    for neighbor in graph[node]: 
        if neighbor not in visited: 
            dfs(graph, neighbor, visited) 
 
# BFS (Queue) 
def bfs(graph, start): 
    visited = set([start]) 
    queue = deque([start]) 
 
    while queue: 
        node = queue.popleft() 
        print(node, end=" ") 
 
        for neighbor in graph[node]: 
            if neighbor not in visited: 
                visited.add(neighbor) 
                queue.append(neighbor) 
 
print("DFS Traversal:") 
dfs(graph, 'A') 
print("\n")  
print("\nBFS Traversal:") 
bfs(graph, 'A')
