class Solution:
    def __init__(self, w: List[int]):
        for i in range(1, len(w)): w[i] += w[i-1]
        self.w = w

    def pickIndex(self) -> int:
        x = random.randint(1, self.w[-1])   
        return bisect.bisect_left(self.w, x)
