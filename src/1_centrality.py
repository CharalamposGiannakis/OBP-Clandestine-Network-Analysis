import networkx as nx
from scipy.io import mmread
import os

def calculate_network_max_depth():
    file_path = "data/clandestine_network_example.mtx"
    
    if not os.path.exists(file_path):
        print("FOUT: Bestand niet gevonden op " + file_path)
        return


    G = nx.Graph(mmread(file_path))
    print(f"Netwerk geladen met {G.number_of_nodes()} leden.")


    if nx.is_connected(G):
        diameter = nx.diameter(G)
        print(f"Het netwerk is volledig verbonden.")
        print(f"De maximale afstand (Diameter) is: {diameter}")
    else:
        components = sorted(nx.connected_components(G), key=len, reverse=True)
        largest_component = G.subgraph(components[0])
        
        diameter = nx.diameter(largest_component)
        print(f"Het netwerk bestaat uit {len(components)} losse groepen.")
        print(f"De grootste groep bevat {largest_component.number_of_nodes()} leden.")
        print(f"De maximale afstand binnen deze groep is: {diameter}")

if __name__ == "__main__":
    calculate_network_max_depth()