class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        nums.append(target)
        nums=sorted(nums)
        return nums.index(target)
        
        
