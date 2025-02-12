# 215. Kth Largest Element in an Array
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/


# Solution A: O(n log n) time, O(n) space
#   Sort the list and then choose the kth element
# Solution B: 
#   Create a min heap, and add 

from heapq import heappush, heappop
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        minHeap = []
        for x in nums:
            heappush(minHeap, x)
            if len(minHeap) > k:
                heappop(minHeap)
        
        return minHeap[0]



if __name__ == '__main__':
    s = Solution()

    nums = [3,2,1,5,6,4]
    test = s.findKthLargest(nums, 2)
    print("solution =", test)