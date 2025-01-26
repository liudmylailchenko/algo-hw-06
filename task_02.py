import networkx as nx
from collections import deque
from graph import G


import networkx as nx


def dfs_recursive(graph: nx.Graph, curr: str, goal: str, path=None, visited=None):
    if visited is None:
        visited = set()

    if path is None:
        path = []

    visited.add(curr)
    path.append(curr)

    if curr == goal:
        return path

    for neighbor in graph[curr]:
        if neighbor not in visited:
            result = dfs_recursive(graph, neighbor, goal, path, visited)
            if result:  # If goal is found, return immediately
                return result

    path.pop()  # Backtrack if the goal is not found in this path
    return None  # Return None if goal is unreachable


def bfs_recursive(graph: nx.Graph, queue: deque, goal: str, path=None, visited=None):
    if visited is None:
        visited = set()

    if path is None:
        path = []

    if not queue:
        return None

    vertex = queue.popleft()

    if not graph.has_node(vertex):
        return path

    if vertex == goal:
        path.append(vertex)
        return path

    if vertex not in visited:
        visited.add(vertex)
        path.append(vertex)
        queue.extend(neighbor for neighbor in graph[vertex] if neighbor not in visited)

    return bfs_recursive(graph, queue, goal, path, visited)


dfs_result = dfs_recursive(G, "A", "F")

print("DFS Result:", dfs_result)

bfs_result = bfs_recursive(G, deque(["A"]), "F")

print("BFS Result:", bfs_result)
