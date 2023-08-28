def dijkstra(n, v, cost):
    visited = [False] * (n + 2)
    distance = [float('inf')] * (n + 2)
    path = [[] for _ in range(n + 2)]
    
    distance[v] = 0
    path[v] = [v]
    
    for _ in range(n):
        u = min((i for i in range(1, n + 1) if not visited[i]), key=lambda i: distance[i])
        visited[u] = True
        
        for w in range(1, n + 1):
            if not visited[w] and (d := distance[u] + cost[u][w]) < distance[w]:
                distance[w], path[w] = d, path[u] + [w]
    
    return distance, path

def main():
    n = int(input("Enter the number of vertices: "))
    cost = [[float('inf')] * (n + 2) for _ in range(n + 2)]
    for i in range(1, n + 1):
        cost[i][1:n + 1] = map(int, input().split())

    v = int(input("Enter the source vertex: "))
    distance, shortest_paths = dijkstra(n, v, cost)

    print(f"Shortest paths from source {v} to the remaining vertices:")
    for i in range(1, n + 1):
        if i != v:
            print(f"{v} -> {' -> '.join(map(str, shortest_paths[i][1:]))} = {distance[i]}")

if __name__ == "__main__":
    main()
