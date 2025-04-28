import math
from dataclasses import dataclass

import networkx as nx


@dataclass
class Voto:
    punti: int
    nome: str

    def __hash__(self):
        return hash((self.punti, self.nome))

    def __eq__(self, other):
        return self.nome == other.nome


grafo = nx.Graph()  # Grafo semplice
grafo2 = nx.DiGraph()  # Grafo diretto

grafo2.add_node(1)
grafo2.add_node("Due")
grafo2.add_node(Voto(24, "TdP"))
grafo2.add_node(math.cos)

print(grafo2.nodes)
grafo2.add_edge("Due", 1, arbitaryAttr=0.9)
print(grafo2.edges)

nbunch = [1, 2, 3, 4, 5, 6, 7, 8, 9]
grafo2.add_nodes_from(nbunch)
print(grafo2.nodes)

ebunch = [(4, 6), (8, 1), (11, 9)]
grafo2.add_edges_from(ebunch)
print(grafo2.nodes)
print(grafo2.edges)

print(grafo2.get_edge_data("Due", 1))

print(grafo2["Due"])
print(grafo2["Due"][1])