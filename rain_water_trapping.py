# Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/description/

# Given n non-negative integers representing an elevation map where the width of each bar is 1, 
# compute how much water it can trap after raining.

# Example 1:
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
# In this case, 6 units of rain water (blue section) are being trapped.

# Example 2:
# Input: height = [4,2,0,3,2,5]
# Output: 9
 

# Constraints:
# n == height.length
# 1 <= n <= 2 * 10**4
# 0 <= height[i] <= 10**5

class Solution:
    def trap(self, height: list[int]) -> int:
        """
        Calculates the amount of rainwater trapped.

        Args:
        height (list): Heights of bars.

        Returns:
        int: Amount of rainwater trapped.
        """
        
        length = len(height)
        left_trap = [0] * length
        right_trap = [0] * length

        # check for left side water trap
        left_trap[0] = height[0]
        for i in range(1, length):
            left_trap[i] = max(left_trap[i-1], height[i])

        # check for right side water trap
        right_trap[length-1] = height[length-1]
        for i in range(length-2, -1, -1):
            right_trap[i] = max(right_trap[i+1], height[i])

        water_trapped = 0
        for i in range(length):
            water_trapped += min(left_trap[i], right_trap[i]) - height[i]

        return water_trapped
    

if __name__ == "__main__":
    s = Solution()
    assert(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6)
    assert(s.trap([4,2,0,3,2,5]) == 9)
    