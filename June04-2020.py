class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place ins
        """
        n=len(s)-1
        i=0
        b=int((n+1)/2)
        while(b>=1):
            s[i],s[n]=s[n],s[i]
            i+=1
            n-=1
            b=b-1
