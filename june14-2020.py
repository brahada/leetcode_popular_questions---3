class Solution:
    import math
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        dist = [math.inf]*n
        dist[src] = 0
        for _ in range(K+1):
            olddist = dist[:]
            for f in flights:
                dist[f[1]] = min(dist[f[1]], olddist[f[0]] + f[2])
        return dist[dst] if dist[dst] < math.inf else -1
