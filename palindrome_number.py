# Palindrome Number
# https://leetcode.com/problems/palindrome-number/description/

# Given an integer x, return true if x is a palindrome, and false otherwise.

 
# Example 1:
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

# Constraints:
# -231 <= x <= 231 - 1
 

class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        length = len(s)
        mid = int(length/2)

        for i in range(mid):
            if s[i] != s[length-1-i]:
                return False

        return True
    
    def isPalindromeWithoutToString(self, x: int) -> bool:
        """
        Checks if a number is a palindrome.

        Args:
        n (int): Input number.

        Returns:
        bool: True if the number is a palindrome, False otherwise.
        """

        if x < 0:  # Negative numbers cannot be palindromes
            return False

        reversed_num = 0
        original_num = x

        while x != 0:
            remainder = x % 10
            reversed_num = (reversed_num * 10) + remainder
            x = x // 10

        return original_num == reversed_num
    

if __name__ == "__main__":
    s = Solution()
    assert(s.isPalindrome(121)==True)
    assert(s.isPalindrome(123)==False)
    assert(s.isPalindrome(-121)==False)
    assert(s.isPalindrome(10)==False)

    assert(s.isPalindromeWithoutToString(121)==True)
    assert(s.isPalindromeWithoutToString(123)==False)
    assert(s.isPalindromeWithoutToString(-121)==False)
    assert(s.isPalindromeWithoutToString(10)==False)
    