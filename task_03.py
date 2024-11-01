import heapq 

#Функція для створення графа
def create_graph():
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }
    return graph

#Алгоритм Дейкстри
def dijkstra(graph, start):
    
    distances = {node: float('inf') for node in graph}
    distances[start] = 0  
    
    priority_queue = [(0, start)] 
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                
    return distances


graph = create_graph()
start_node = 'A'
shortest_paths = dijkstra(graph, start_node)

print("Найкоротші відстані від вершини", start_node)
for node, distance in shortest_paths.items():
    print(f"Відстань до {node}: {distance}")
