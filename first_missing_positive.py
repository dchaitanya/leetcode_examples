# First Missing Positive
# https://leetcode.com/problems/first-missing-positive/description/

# Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.
# You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

# Example 1:
# Input: nums = [1,2,0]
# Output: 3
# Explanation: The numbers in the range [1,2] are all in the array.

# Example 2:
# Input: nums = [3,4,-1,1]
# Output: 2
# Explanation: 1 is in the array but 2 is missing.

# Example 3:
# Input: nums = [7,8,9,11,12]
# Output: 1
# Explanation: The smallest positive integer 1 is missing.
 

# Constraints:
# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1


class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        # sort the array
        nums = list(set(nums))
        nums.sort()

        missing_integer = 1

        for i in nums:
            if i > 0:
                if i == missing_integer:
                    missing_integer += 1
                else:
                    break
                
        return missing_integer

        
if __name__ == "__main__":
    s = Solution()
    assert(s.firstMissingPositive([1, 2, 0]) == 3)
    assert(s.firstMissingPositive([3, 4, -1, 1]) == 2)
    assert(s.firstMissingPositive([7, 8, 9, 11, 12]) == 1)
    assert(s.firstMissingPositive([0,2,2,1,1]) == 3)
