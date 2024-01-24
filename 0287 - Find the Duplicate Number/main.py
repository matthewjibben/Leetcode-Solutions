# 287. Find the Duplicate Number
# https://leetcode.com/problems/find-the-duplicate-number/description/

# Solutions:
# Solution A: O(n log n + n) 
#   sort the array, and then loop through it until you find two equal elements right next to each other
#   (does not meet the requirements to not modify the array. We could make a copy, but then it would not use constant space)
# Solution B: O(n) time, O(n) space
#   Use a Hashmap. Loop through the list and insert each element into a hashmap. When a duplicate is found, return it.
#   (does not meet the requirements to use constant space)
# Solution C: O(n) time, O(1) space
#   (near duplicate of problem #142)
#   View the list as a linked list. Each element points to the element at the index of its value.
#   Example: [1,3,4,2,2] = start -> 1 -> 3 -> 2 -> 4 -> 2 -> 4 ...
#   Because the list contains n+1 elements, and each element is in the range [1, n], there must be a cycle
#   via Floyd's Cycle Algorithm, we can initialize a fast and slow pointer, the element at the start of the cycle is the repeated element 
#   Which we can find by:
#     The slow pointer moves 1 index at a time, fast moves 2. 
#     once they meet we are guaranteed to be in the cycle. If slow has moved x times, then fast has moved 2x
#     return one of the pointers back to 0, then move both pointers by a speed of 1.
#     via Floyd's cycle algorithm, they will always meet at the start of the cycle

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = nums[0]
        fast = nums[nums[0]]

        while(fast != slow):
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        slow = 0
        while(fast != slow):
            slow = nums[slow]
            fast = nums[fast]

        return slow



if __name__ == '__main__':
    s = Solution()
    test = s.findDuplicate([1,3,4,2,2])
    print("solution =", test)
    test = s.findDuplicate([3,1,3,4,2])
    print("solution =", test)