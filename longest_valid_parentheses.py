# Longest Valid Parentheses

# https://leetcode.com/problems/longest-valid-parentheses/

# Given a string containing just the characters '(' and ')', return the length of the 
# longest valid (well-formed) parentheses substring.

# Example 1:
# Input: s = "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()".

# Example 2:
# Input: s = ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()".

# Example 3:
# Input: s = ""
# Output: 0
 

# Constraints:
# 0 <= s.length <= 3 * 10^4
# s[i] is '(', or ')'.

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left, right = 0, 0
        max_len = 0

        # check for left to right
        for i in range(len(s)):
            if s[i] == '(':
                left += 1
            else:
                right += 1

            if left == right:
                max_len = max(max_len, 2 * left)
            elif right > left:
                left, right = 0, 0

        left, right = 0, 0
        # check for right to left too
        for i in range(len(s)-1, 0, -1):
            if s[i] == '(':
                left += 1
            else:
                right += 1

            if left == right:
                max_len = max(max_len, 2 * left)
            elif left > right:
                left, right = 0, 0

        return max_len


if __name__ == "__main__":
    s = "(()"
    print (Solution().longestValidParentheses(s))

    s = ")()())"
    print (Solution().longestValidParentheses(s))

    s = ""
    print (Solution().longestValidParentheses(s))
