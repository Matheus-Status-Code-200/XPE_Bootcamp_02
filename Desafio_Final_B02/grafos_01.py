class Grafo:
    def __init__(self):
        self.vertices = {}
        self.arestas = []
    def adicionar_vertice(self, vertice):
        self.vertices[vertice] = {}
    def adicionar_aresta(self, origem, destino, peso):
        self.arestas.append((origem, destino, peso))
        self.vertices[origem][destino] = peso
        self.vertices[destino][origem] = peso
    def obter_vertices(self):
        return self.vertices.keys()
    def obter_arestas(self):
        return self.arestas
g = Grafo()
# Adicionar vértices
g.adicionar_vertice("A")
g.adicionar_vertice("B")
g.adicionar_vertice("C")
g.adicionar_vertice("D")
# Adicionar arestas
g.adicionar_aresta("A", "B", 1)
g.adicionar_aresta("A", "C", 2)
g.adicionar_aresta("B", "D", 3)
g.adicionar_aresta("C", "D", 4)
# Obter vértices
print ("vérteces: ", g.obter_vertices())
# Obter arestas
print ("arestas: ", g.obter_arestas())