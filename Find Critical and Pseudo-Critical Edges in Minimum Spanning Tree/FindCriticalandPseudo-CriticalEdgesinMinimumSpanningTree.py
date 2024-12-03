from typing import List

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        arestas_indexadas = [(u, v, peso, i) for i, (u, v, peso) in enumerate(edges)]
        arestas_indexadas.sort(key=lambda x: x[2])

        class UnionFind:
            def __init__(self, n):
                self.pai = list(range(n))
                self.rank = [0] * n
                
            def encontrar(self, x):
                if self.pai[x] != x:
                    self.pai[x] = self.encontrar(self.pai[x])
                return self.pai[x]
            
            def unir(self, x, y):
                raizX = self.encontrar(x)
                raizY = self.encontrar(y)
                if raizX != raizY:
                    if self.rank[raizX] > self.rank[raizY]:
                        self.pai[raizY] = raizX
                    elif self.rank[raizX] < self.rank[raizY]:
                        self.pai[raizX] = raizY
                    else:
                        self.pai[raizY] = raizX
                        self.rank[raizX] += 1
                
        def kruskal(n, arestas, excluir_aresta=-1, forcar_aresta=-1):
            uf = UnionFind(n)
            peso_mst = 0
            arestas_usadas = 0

            if forcar_aresta != -1:
                u, v, peso, _ = arestas[forcar_aresta]
                if uf.encontrar(u) != uf.encontrar(v):
                    uf.unir(u, v)
                    peso_mst += peso
                    arestas_usadas += 1

            for i, (u, v, peso, _) in enumerate(arestas):
                if i == excluir_aresta:
                    continue
                if uf.encontrar(u) != uf.encontrar(v):
                    uf.unir(u, v)
                    peso_mst += peso
                    arestas_usadas += 1

            if arestas_usadas == n - 1:
                return peso_mst
            else:
                return float('inf')

        peso_original = kruskal(n, arestas_indexadas)

        criticas = []
        pseudocriticas = []

        for i in range(len(arestas_indexadas)):
            if kruskal(n, arestas_indexadas, excluir_aresta=i) > peso_original:
                criticas.append(arestas_indexadas[i][3])
            elif kruskal(n, arestas_indexadas, forcar_aresta=i) == peso_original:
                pseudocriticas.append(arestas_indexadas[i][3])

        return [criticas, pseudocriticas]

# Testes
sol = Solution()

# Caso de teste 1
n1 = 5
edges1 = [[0,1,1],[1,2,2],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
print(sol.findCriticalAndPseudoCriticalEdges(n1, edges1))  # Saída esperada: [[0, 1], [2, 3, 4, 5]]

# Caso de teste 2
n2 = 4
edges2 = [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]
print(sol.findCriticalAndPseudoCriticalEdges(n2, edges2))  # Saída esperada: [[], [0, 1, 2, 3]]
