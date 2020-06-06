class Solution:
		def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
			res = []     
			people.sort(key=lambda x:(-x[0],x[1]))
			for x,y in people:
				res.insert(y,[x,y])        
			return res
        
