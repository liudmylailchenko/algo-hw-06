import networkx as nx

G = nx.Graph()

stations = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

edges = [
    ("A", "B"),
    ("A", "C"),
    ("B", "D"),
    ("C", "D"),
    ("C", "E"),
    ("D", "F"),
    ("E", "G"),
    ("F", "H"),
    ("G", "I"),
    ("H", "J"),
    ("I", "J"),
    ("B", "E"),
    ("D", "G"),
    ("F", "I"),
]

G.add_nodes_from(stations)
G.add_edges_from(edges)
