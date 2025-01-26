import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
from graph import G

num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degrees = dict(G.degree())

df_degrees = pd.DataFrame(degrees.items(), columns=["Station", "Degree"])

analysis_results = {
    "Number of Stations (Nodes)": num_nodes,
    "Number of Connections (Edges)": num_edges,
}

print("Distribution of Station Degrees:\n ", df_degrees)
print("Analysis Results:", analysis_results)


plt.figure(figsize=(8, 6))
plt.title("City Transportation Network")
nx.draw(
    G,
    with_labels=True,
    node_color="pink",
    edge_color="gray",
    node_size=2000,
    font_size=12,
)
plt.show()
