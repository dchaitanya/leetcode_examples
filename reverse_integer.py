# Reverse Integer

# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Example 1:
# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321

# Example 3:
# Input: x = 120
# Output: 21
 

# Constraints:
# -231 <= x <= 231 - 1

class Solution:
    def reverse(self, x: int) -> int:
        """
        Reverses an integer.

        Args:
        n (int): Input integer.

        Returns:
        int: Reversed integer.
        """

        sign = -1 if x < 0 else 1
        x = abs(x)

        reversed_number = 0

        while x != 0:
            remainder = x % 10
            if reversed_number > (2**31 - 1 - remainder) // 10:  # Check for overflow
                return 0
            reversed_number = (reversed_number * 10) + remainder
            x = x // 10
        
        return reversed_number * sign
    


if __name__ == "__main__":
    s = Solution()
    assert(s.reverse(123) == 321)
    assert(s.reverse(-123) == -321)
    assert(s.reverse(120) == 21)
    assert(s.reverse(1534236469) == 0)
