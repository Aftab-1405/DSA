# Leet-code 167

from typing import List

class Solution:
    def twoSumBrute(self, numbers: List[int], target: int) -> List[int]:
        """
        Brute force approach: Check all possible pairs
        Time Complexity: O(n²) - nested loops
        Space Complexity: O(1) - only using constant extra space
        """
        # Outer loop: select first number of the pair
        for i in range(len(numbers)):
            # Inner loop: select second number of the pair
            for j in range(i + 1, len(numbers)):
                # Check if current pair sums to target
                if numbers[i] + numbers[j] == target:
                    # Return 1-based indices as required
                    return [i + 1, j + 1]
        
        # Problem guarantees exactly one solution exists
        return []
    
    def twoSumBetter(self, numbers: List[int], target: int) -> List[int]:
        """
        This is better approach to solve the same problem using hashmap, here i am using complement so that i can find the required elements in min steps.
        """
        seen = {}
        for i, num in enumerate(numbers):
            complement = target - num
            if complement in seen:
                return [seen[complement] + 1, i + 1]
            seen[num] = i

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        This is an optimal solution with two ponters approach which will allow us to solve the same problem with TC as O(n).
        """
        beg = 0
        end = len(numbers) - 1

        while beg < end:
            if numbers[beg] + numbers[end] == target:
                return [beg + 1, end + 1]
            if numbers[beg] + numbers[end] > target:
                end -= 1
            else:
                beg += 1
