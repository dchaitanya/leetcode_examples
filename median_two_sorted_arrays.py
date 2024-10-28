# Median of Two Sorted Arrays

# Given two sorted arrays nums1 and nums2 of size m and n respectively, 
# return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

 

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

# Constraints:
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:

        total = len(nums1) + len(nums2)
        mid = total // 2

        mergedArr = self.mergedArray(nums1, nums2, mid)
        if total % 2 != 0:
            return mergedArr[mid]
        else:
            return (mergedArr[mid] + mergedArr[mid-1]) / 2 

        
    def mergedArray(self, n1: list[int], n2: list[int], mid: int) -> list[int]:
        merged = []
        ptr1 = 0
        ptr2 = 0
        ptr3 = 0

        if (len(n1) == 0): 
            return n2
        if (len(n2) == 0):  
            return n1

        while (ptr1 < len(n1) and ptr2 < len(n2) and ptr3 <= mid):
            if n1[ptr1] < n2[ptr2]:
                merged.append(n1[ptr1])
                ptr1 += 1
            else:
                merged.append(n2[ptr2])
                ptr2 += 1 
            ptr3 += 1
            
        while ptr2 < len(n2) and ptr3 <= mid:
            merged.append(n2[ptr2])
            ptr3 += 1
            ptr2 += 1

        while ptr1 < len(n1) and ptr3 <= mid:
            merged.append(n1[ptr1])
            ptr3 += 1
            ptr1 += 1 

        return merged


if __name__ == "__main__":
    s = Solution()
    nums1 = [1, 3]
    nums2 = [2]
    print (s.findMedianSortedArrays(nums1, nums2))
   
    nums1 = [1, 2]
    nums2 = [3, 4]
    print (s.findMedianSortedArrays(nums1, nums2))
