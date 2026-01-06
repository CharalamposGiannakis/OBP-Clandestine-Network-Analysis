import networkx as nx
from scipy.io import mmread
import os

def calculate_network_max_depth():
    file_path = "data/clandestine_network_example.mtx"
    
    # Check if the data file exists
    if not os.path.exists(file_path):
        print("ERROR: File not found at " + file_path)
        return

    # Load the network from the Matrix Market file
    G = nx.Graph(mmread(file_path))
    print(f"Network loaded with {G.number_of_nodes()} members.")

    # Check if every node can reach every other node
    if nx.is_connected(G):
        diameter = nx.diameter(G)
        print(f"The network is fully connected.")
        print(f"The maximum distance (Diameter) is: {diameter}")
    else:
        # If disconnected, analyze the largest cluster (Component)
        components = sorted(nx.connected_components(G), key=len, reverse=True)
        largest_component = G.subgraph(components[0])
        
        diameter = nx.diameter(largest_component)
        print(f"The network consists of {len(components)} separate groups.")
        print(f"The largest group contains {largest_component.number_of_nodes()} members.")
        print(f"The maximum distance within this group is: {diameter}")

if __name__ == "__main__":
    calculate_network_max_depth()