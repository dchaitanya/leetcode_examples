# Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/description/

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# Example 4:
# Input: s = "([])"
# Output: true


# Constraints:
# 1 <= s.length <= 10**4
# s consists of parentheses only '()[]{}'



class Solution:
    def isValid(self, s: str) -> bool:
        """
        Checks if parentheses in a string are valid.

        Args:
        s (str): Input string containing parentheses.

        Returns:
        bool: True if parentheses are valid, False otherwise.
        """

        stack = []
        parentheses_map = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in parentheses_map.values():
                stack.append(char)
            elif char in parentheses_map.keys():
                if not stack or parentheses_map[char] != stack.pop():
                    return False

        return not stack


if __name__ == '__main__':
    s = Solution()
    print(s.isValid("()"))  # Output: True
    print(s.isValid("()[]{}"))  # Output: True
    print(s.isValid("(]"))  # Output: False
    print(s.isValid("([)]"))  # Output: False
    print(s.isValid("{[]}"))  # Output: True
    print(s.isValid("{"))  # Output: True
    print(s.isValid("]"))  # Output: True

