import heapq
import math

class Graph:
    def __init__(self):
        self.adjacency = {}  

    def add_edge(self, u, v, weight, bidirectional=True):
        self.adjacency.setdefault(u, []).append((v, weight))
        if bidirectional:
            self.adjacency.setdefault(v, []).append((u, weight))

def dijkstra(graph, start, end):
    pq = [(0, start)]
    distances = {node: math.inf for node in graph.adjacency}
    distances[start] = 0
    parent = {start: None}

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        if current_node == end:
            break

        for neighbor, weight in graph.adjacency.get(current_node, []):
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                parent[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    path = []
    node = end
    while node:
        path.append(node)
        node = parent.get(node)
    path.reverse()

    return distances[end], path

graph = Graph()
graph.add_edge("A", "B", 4)
graph.add_edge("A", "C", 2)
graph.add_edge("B", "C", 1)
graph.add_edge("B", "D", 5)
graph.add_edge("C", "D", 8)
graph.add_edge("C", "E", 10)
graph.add_edge("D", "E", 2)
graph.add_edge("D", "Z", 6)
graph.add_edge("E", "Z", 3)

coords = {
    "A": (0, 0),
    "B": (1, 2),
    "C": (2, 1),
    "D": (3, 3),
    "E": (5, 2),
    "Z": (6, 0)
}

print("Dijkstra →", dijkstra(graph, "A", "Z"))
