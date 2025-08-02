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
    
    def sortedSquaresOptimal(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums) - 1
        k = len(nums) - 1
        result = [0] * len(nums)

        while i <= j:
            if abs(nums[i]) < abs(nums[j]):
                result[k] = nums[j] ** 2
                j -= 1
            else:
                result[k] = nums[i] ** 2
                i += 1
            k -= 1
        
        return result
    
nums = [-4,-1,0,3,10]

s = Solution()
print ( s.sortedSquaresOptimal(nums))