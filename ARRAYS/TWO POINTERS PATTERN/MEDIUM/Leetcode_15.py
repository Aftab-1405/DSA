# Leetcode 15
# 3Sum problem

from typing import List

class Solution:
    # This is a brute force solution, where I am using 3 nested loops to find out the triplets. This approach might end up with TC as O(n)^3.
    
    def threeSumBrute(self, nums: List[int]) -> List[List[int]]:
        result = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = sorted([nums[i], nums[j], nums[k]])

                        if triplet not in result: # Avoiding duplicate triplets here.
                            result.append(triplet)
        return result