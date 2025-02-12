# 268. Missing Number
# https://leetcode.com/problems/missing-number/description/


# Solution A: O(n) time, O(1) space
#   we know that each list contains distinct numbers in a range, where only one is missing. Therefore, we can use cyclic sort
#   swap each element in the list to its proper location (value = index)
#   then, loop one more time until we find the missing element
# Solution B: O(n) time, O(1) space
#   return the expected sum of the range - the sum of the list
#   much simpler and better than solution A, but I want to practice cyclic sort problems
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i=0
        while(i < len(nums)):
            val = nums[i]
            if(nums[i] != i and nums[i] < len(nums)):
                # print(nums[i], nums[nums[i]])
                # print(nums)
                
                nums[i], nums[val] = nums[val], nums[i]
            else:
                 i += 1
        
        # print(nums)
        
        # loop through the sorted array until you find the missing element
        for i in range(0, len(nums)):
            if(nums[i] != i):
                return i
        
        return len(nums)


if __name__ == '__main__':
    s = Solution()

    nums = [9,6,4,2,3,5,7,0,1]
    test = s.missingNumber(nums)
    print("solution =", test)