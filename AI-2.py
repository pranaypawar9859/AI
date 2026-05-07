import heapq 
 
def a_star(grid, start, end): 
    open_list = [] 
    heapq.heappush(open_list, (0, start)) 
 
    came_from = {} 
    g_cost = {start: 0} 
 
    while open_list: 
        current = heapq.heappop(open_list)[1] 
 
        if current == end: 
            path = [] 
            while current in came_from: 
                path.append(current) 
                current = came_from[current] 
            path.append(start) 
            return path[::-1] 
 
        x, y = current 
 
        for move in [(0,1), (1,0), (0,-1), (-1,0)]: 
            neighbor = (x + move[0], y + move[1]) 
 
            if not (0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0])): 
                continue 
 
            if grid[neighbor[0]][neighbor[1]] == 1: 
                continue 
 
            new_g = g_cost[current] + 1 
 
            if neighbor not in g_cost or new_g < g_cost[neighbor]: 
                g_cost[neighbor] = new_g 
 
                f = new_g + abs(neighbor[0] - end[0]) + abs(neighbor[1] - end[1]) 
 
                heapq.heappush(open_list, (f, neighbor)) 
                came_from[neighbor] = current 
 
    return None 
 
grid = [ 
    [0,0,0], 
[1,1,0], 
[0,0,0] 
] 
start = (0,0) 
end = (2,2) 
print(a_star(grid, start, end))
