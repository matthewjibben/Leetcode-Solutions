# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/description/


# Solutions
# Solution A: O(n)
#   Use two sliding pointers, and calculate the area between the lines. start at the first and last elements
#   if one leg is taller than the other, increment/decrement the smaller one (loop until impossible)
#   always save the maximum area ever found with both indices
# the area of the square is calculated using area = min(left height, right height) * (distance between lines)
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea = 0
        left = 0
        right = len(height) - 1

        while(right-left >= 1):
            # calculate the area between the lines, saving it if it is the new maximum area
            currentArea = min(height[left], height[right]) * (right-left)
            if currentArea > maxArea:
                # print("new max = ", height[left], height[right], currentArea)
                maxArea = currentArea
            
            # if one leg is taller than the other, increment/decrement the smaller one 
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        

        return maxArea
        





if __name__ == '__main__':
    s = Solution()
    # test = s.maxArea([1,8,6,2,5,4,8,3,7])
    # print("solution =", test)
    test = s.maxArea([4, 15, 8, 2, 18, 7, 12, 3, 9, 6, 14, 1, 19, 5, 11])
    print("solution =", test)