# LeetCode #88: Merge Sorted Array
# Problem: Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 
# as one sorted array in-place. nums1 has size m+n where the last n elements are 0s.

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merges two sorted arrays in-place using two-pointer technique from the end.
        
        Logic Overview:
        - Start from the end of both arrays to avoid overwriting unprocessed elements
        - Compare elements and place the larger one at the current position
        - Handle remaining elements from nums2 if any
        
        Time Complexity: O(m + n) - single pass through both arrays
        Space Complexity: O(1) - only using constant extra space for pointers
        
        Args:
            nums1: First sorted array with extra space (size m+n)
            m: Number of actual elements in nums1
            nums2: Second sorted array (size n)  
            n: Number of elements in nums2
        """
        
        # Initialize pointers at the last valid elements of both arrays
        nums1Ptr = m - 1  # Last actual element in nums1
        nums2Ptr = n - 1  # Last element in nums2
        pos = len(nums1) - 1  # Position to fill (rightmost in nums1)
        
        # Main merge loop: compare and place larger elements from right to left
        while nums2Ptr >= 0 and nums1Ptr >= 0:
            # Compare current elements and place the larger one at current position
            if nums1[nums1Ptr] > nums2[nums2Ptr]:
                nums1[pos] = nums1[nums1Ptr]  # Place nums1 element
                nums1Ptr -= 1  # Move nums1 pointer left
            else:
                nums1[pos] = nums2[nums2Ptr]  # Place nums2 element
                nums2Ptr -= 1  # Move nums2 pointer left
            
            pos -= 1  # Move to next position to fill
        
        # Handle remaining elements from nums2 (if nums1 is exhausted first)
        # Note: If nums2 is exhausted first, remaining nums1 elements are already in place
        while nums2Ptr >= 0:
            nums1[pos] = nums2[nums2Ptr]
            nums2Ptr -= 1
            pos -= 1

# Test execution
s1 = Solution()

# Test case: nums1=[1,2,3,0,0,0], nums2=[2,5,6], m=3, n=3
# Expected result: [1,2,2,3,5,6]
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m = 3
n = 3

s1.merge(nums1, m, nums2, n)
print(f"Merged array: {nums1}")

# Time Complexity Analysis:
# - Single pass through both arrays: O(m + n)
# - Each element is processed exactly once
#
# Space Complexity Analysis:  
# - Only using constant extra variables (pointers): O(1)
# - In-place modification of nums1