class Solution:
    def sortColors(self, A: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #nums=nums.sort()
        n=len(A)
        f=[0]*n
        for i in A:
            f[i]=f[i]+1
        k=0
        for i in range(len(f)):
            while f[i]>0:
                A[k]=i
                f[i]=f[i]-1
                k=k+1
                
