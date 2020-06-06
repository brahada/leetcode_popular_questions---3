class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people=sorted(people,reverse=True)
        res=[]
        for x,y in people:
            res.insert(y,[x,y])
        return res
            
