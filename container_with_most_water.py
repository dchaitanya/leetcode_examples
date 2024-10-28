# Container With Most Water

# https://leetcode.com/problems/container-with-most-water/description/
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

# Example 1:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: 
# The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
# In this case, the max area of water (blue section) the container can contain is 49.

# Example 2:

# Input: height = [1,1]
# Output: 1

# Constraints:
# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104


class Solution:
    def maxArea(self, height: list[int]) -> int:
        """
        Returns the maximum area of water that can be trapped between two lines.
        
        :param height: A list of non-negative integers representing line heights.
        :return: The maximum area of water.
        """

        # Initialize two pointers, one at the beginning and one at the end
        left = 0
        right = len(height) - 1
        
        # Initialize the maximum area
        max_area = 0
        
        # Loop until the pointers meet
        while left < right:
            # Calculate the width of the current container
            width = right - left
            
            # Calculate the height of the current container (minimum of two lines)
            container_height = min(height[left], height[right])
            
            # Calculate the current area
            area = width * container_height
            
            # Update the maximum area if necessary
            max_area = max(max_area, area)
            
            # Move the pointer of the shorter line towards the other pointer
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
    
        return max_area



if __name__ == "__main__":
    # Test the function
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    s = Solution()
    print(s.maxArea(height))  # Output: 49
