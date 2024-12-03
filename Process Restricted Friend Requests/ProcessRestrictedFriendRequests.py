from typing import List

class UnionFind:
    def __init__(self, n: int):
        self.pai = list(range(n))
        self.rank = [1] * n

    def encontrar(self, x: int) -> int:
        if self.pai[x] != x:
            self.pai[x] = self.encontrar(self.pai[x])
        return self.pai[x]

    def unir(self, x: int, y: int):
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

    def estao_conectados(self, x: int, y: int) -> bool:
        return self.encontrar(x) == self.encontrar(y)


class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        uf = UnionFind(n)
        resultado = []
        grafo_restricoes = {i: set() for i in range(n)}
        
        for x, y in restrictions:
            grafo_restricoes[x].add(y)
            grafo_restricoes[y].add(x)
        
        for u, v in requests:
            podem_ser_amigos = True

            if uf.estao_conectados(u, v):
                resultado.append(True)
                continue
            
            for x, y in restrictions:
                if uf.estao_conectados(u, x) and uf.estao_conectados(v, y):
                    podem_ser_amigos = False
                    break
                if uf.estao_conectados(v, x) and uf.estao_conectados(u, y):
                    podem_ser_amigos = False
                    break

            if podem_ser_amigos:
                uf.unir(u, v)
                resultado.append(True)
            else:
                resultado.append(False)
        
        return resultado

# Caso de teste
if __name__ == "__main__":
    solucao = Solution()
    n = 5
    restrictions = [[0, 1], [1, 2], [2, 3]]
    requests = [[0, 4], [1, 2], [3, 1], [3, 4]]
    resultado = solucao.friendRequests(n, restrictions, requests)
    print(resultado)  # Saída esperada: [True, False, True, False]
