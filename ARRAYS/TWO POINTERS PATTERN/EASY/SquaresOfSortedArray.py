from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Brute force solution with TC n(logn)
        i = 0
        result = []

        while i < len(nums):
            result.append(nums[i] ** 2)
            i += 1
        
        return sorted(result)
    
nums = [-4,-1,0,3,10]

s = Solution()
print ( s.sortedSquares(nums))