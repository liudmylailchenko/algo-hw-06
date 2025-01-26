import networkx as nx
import random
from collections import deque
from graph import G


for u, v in G.edges():
    G[u][v]["weight"] = random.randint(1, 10)


def custom_dijkstra(graph: nx.Graph, start: str, goal: str):
    queue = deque([(0, start, [])])  # (current_cost, node, path)
    visited = set()

    while queue:
        cost, node, path = queue.popleft()

        if node in visited:
            continue

        path = path + [node]
        visited.add(node)

        if node == goal:
            return path, cost

        for neighbor, data in graph[node].items():
            if neighbor not in visited:
                queue.append((cost + data["weight"], neighbor, path))

        queue = deque(sorted(queue, key=lambda x: x[0]))

    return None, float("inf")


start_node = "A"
goal_node = "F"

custom_dijkstra_result, custom_dijkstra_cost = custom_dijkstra(G, start_node, goal_node)

print(
    "Custom Dijkstra Shortest Path",
    custom_dijkstra_result,
)
print("Custom Dijkstra Cost", custom_dijkstra_cost)
