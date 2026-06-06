from collections import Counter
from typing import List, Any

"""
LeetCode 169. Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

Example 2:
Input: nums = [3,2,3]
Output: 3
"""


class Solution:

    @staticmethod
    def better_hash_map(nums: List[int]) -> int | Any:
        """
        Approach: Hash Map

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        frequency = {}

        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        return max(frequency, key=frequency.get)

    @staticmethod
    def better_counter(nums: List[int]) -> int:
        """
        Approach: Counter

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        return Counter(nums).most_common(1)[0][0]

    @staticmethod
    def better_sorting(nums: List[int]) -> int:
        """
        Approach: Sorting

        Observation:
        Since the majority element appears more than n/2 times,
        it will always occupy the middle position after sorting.

        Time Complexity: O(n log n)
        Space Complexity: O(1)
        """
        nums.sort()
        return nums[len(nums) // 2]

    @staticmethod
    def optimal_boyer_moore(nums: List[int]) -> int | None:
        """
        Approach: Boyer-Moore Voting Algorithm

        Time Complexity: O(n)
        Space Complexity: O(1)

        Optimal Solution
        """
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num

            count += 1 if num == candidate else -1

        return candidate


if __name__ == "__main__":
    numbers = [3, 2, 3]

    print("Hash Map        :", Solution.better_hash_map(numbers))
    print("Counter         :", Solution.better_counter(numbers))
    print("Sorting         :", Solution.better_sorting(numbers.copy()))
    print("Boyer-Moore     :", Solution.optimal_boyer_moore(numbers))

