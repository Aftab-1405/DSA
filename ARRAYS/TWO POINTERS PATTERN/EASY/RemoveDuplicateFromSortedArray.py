from typing import List

# Remove Duplicates from Sorted Array (Leetcode 26)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        numsLen = len(nums)
        i = 0 
        j = 1

        while j < numsLen:
            if(nums[i] != nums[j]): # Got an unique element
                i += 1
                nums[i] = nums[j]
            j += 1
        
        return i + 1
    
s = Solution()

print (f"There are {s.removeDuplicates([0, 0, 1, 1, 1, 2, 3, 3, 4, 5, 5])} elements which are unique." )