# Add Two Numbers

# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 
# Example 1:

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
 
# Constraints:

# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.


# Definition for singly-linked list.
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Adds two numbers represented as linked lists.

        Args:
        l1 (Optional[ListNode]): The first number.
        l2 (Optional[ListNode]): The second number.

        Returns:
        Optional[ListNode]: The sum of the two numbers.
        """
        
        # Initialize a dummy node to simplify some corner cases such as a list with only one node, 
        # or removing the head of the list.
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        # Traverse both linked lists
        while l1 or l2 or carry:
            # Calculate the sum of the current nodes' values and the carry
            x1 = l1.val if l1 else 0
            x2 = l2.val if l2 else 0
            sum = carry + x1 + x2
            
            # Update the carry
            carry = sum // 10
            
            # Create a new node with the digit value of the sum
            current.next = ListNode(sum % 10)
            
            # Move to the next nodes
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        # Return the next node of the dummy node, which is the head of the result list
        return dummy.next



# Example Use Case:
if __name__ == "__main__":

    # Create linked lists: 2 -> 4 -> 3 and 5 -> 6 -> 4
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    # Add the two numbers
    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)

    # Print the result: 7 -> 0 -> 8
    while result:
        print(result.val, end=" -> " if result.next else "\n")
        result = result.next
