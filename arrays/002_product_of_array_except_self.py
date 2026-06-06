from typing import List


"""
LeetCode 238. Product of Array Except Self

Given an integer array nums, return an array answer such that
answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed
to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time
and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Approaches
----------
1. Brute Force
2. Better (Prefix & Suffix Arrays)
3. Optimal (Prefix + Suffix using Output Array)
"""


class Solution:

    @staticmethod
    def brute_force(nums: List[int]) -> List[int]:
        """
        Approach 1: Brute Force

        Time Complexity: O(n²)
        Space Complexity: O(1)
        """
        n = len(nums)
        result = []

        for i in range(n):
            product = 1

            for j in range(n):
                if i != j:
                    product *= nums[j]

            result.append(product)

        return result

    @staticmethod
    def better(nums: List[int]) -> List[int]:
        """
        Approach 2: Prefix & Suffix Arrays

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        n = len(nums)

        prefix = [1] * n
        suffix = [1] * n

        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        result = [1] * n

        for i in range(n):
            result[i] = prefix[i] * suffix[i]

        return result

    @staticmethod
    def optimal(nums: List[int]) -> List[int]:
        """
        Approach 3: Prefix + Suffix Using Output Array

        Time Complexity: O(n)
        Space Complexity: O(1)
        (excluding output array)

        Optimal Solution
        """
        n = len(nums)

        result = [1] * n

        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result


if __name__ == "__main__":
    test_nums = [1, 2, 3, 4]

    print("Brute Force :", Solution.brute_force(test_nums))
    print("Better      :", Solution.better(test_nums))
    print("Optimal     :", Solution.optimal(test_nums))

