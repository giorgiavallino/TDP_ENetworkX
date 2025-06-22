from math import cos
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

# Si può aggiungere ciò che si vuole come nodo di un grafo
grafo2.add_node(1)
grafo2.add_node("Due")
grafo2.add_node(Voto(24, "TdP"))
grafo2.add_node(cos)

print(grafo2.nodes)
grafo2.add_edge("Due", 1, arbitraryAttr=0.9) # indicare il nodo iniziale e il nodo finale (se il
# grafo non avesse direzioni negli archi, è indifferente l'ordine di aggiunta dei due nodi)
# L'attributo arbitraryAttr indica il peso dell'arco (l'attributo può avere qualsiasi nome)
print(grafo2.edges)

# Come si aggiunge un insieme di nodi senza dover aggiungere un nodo alla volta?
nbunch = [1, 2, 3, 4, 5, 6, 7, 8, 9]
grafo2.add_nodes_from(nbunch)
print(grafo2.nodes)

# Come si aggiungono diversi archi di un grafo senza doverli aggiungere uno alla volta?
ebunch = [(4, 6), (8, 1), (11, 9)] #nonostante 11 non fosse inizialmente inizializzato, dato che è un vertice di un
# arco viene aggiunto automaticamente tra i nodi
grafo2.add_edges_from(ebunch)
print(grafo2.nodes)
print(grafo2.edges)

print(grafo2.get_edge_data("Due", 1)) # attraverso questa funzione, si ottengono i dati relativi all'arco
# collegante i due nodi citati (come, ad esempio, il peso dell'arco)

# Come si accede al grafo? Considerandolo come un dizionario di dizionari,...
print(grafo2["Due"])
print(grafo2["Due"][1])