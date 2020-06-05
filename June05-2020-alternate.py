class Solution:
    def __init__(self, w: List[int]):
        self.sum=sum(w)
        for i in range(1, len(w)): w[i] += w[i-1]
        self.w = w

    def pickIndex(self) -> int:
        x = self.sum*random.random() 
        return bisect.bisect_left(self.w, x)
