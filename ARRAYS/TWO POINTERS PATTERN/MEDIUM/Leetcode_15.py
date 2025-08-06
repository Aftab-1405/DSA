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
    
    def threeSumOptimal(self, nums: List[int]) -> List[List[int]]:
        """
        Sorting + Two Pointers: Most efficient approach
        Time Complexity: O(n²) - sorting O(n log n) + O(n²) for main logic
        Space Complexity: O(1) for algorithm + O(k) for result
        """
        nums.sort()  # Enable duplicate skipping and two-pointer technique
        result = []
        n = len(nums)
        
        for i in range(n - 2):  # Need at least 2 more elements for triplet
            # Skip duplicate values for first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Two pointers for remaining pair
            left, right = i + 1, n - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == 0:
                    # Found valid triplet
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates for second element
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    
                    # Skip duplicates for third element  
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # Move both pointers
                    left += 1
                    right -= 1
                    
                elif current_sum < 0:
                    # Sum too small, need larger number
                    left += 1
                else:
                    # Sum too large, need smaller number
                    right -= 1
        
        return result