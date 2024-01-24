# 1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold

# solutions:
# Solution A (naive): O(k * n) ?
#  loop through the list with a sliding window and find the average of each subarray window
#  this requires a lot of redundant arithmetic operations
# Solution B: O(n) time and space
#  Create a new array with the sum of each (value + the sum of all values before it)
#  for example, the first input array example would look like [0, 2, 4, 6, 8, 13, 18, 23, 31]
#  then, we loop through the array and find all places where (sums[i+k] - sums[i])/k >= threshold
#  solves a lot of the redundant operations in solution A
# Solution C: O(n) time, O(1) space
#  loop through the array, keeping track of the sum of all elements in the window
#  when you iterate, add the next value to the sum, and remove the oldest value from the sum
#  count every time the sum >= k * threshold
#  this solution removes the redundant operations in solution A, and removes the need for a second array from solution B

class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        count=0
        windowSum = 0
        low = 0

        # find the sum of the first k elements
        for i in range(0, k):
            windowSum += arr[i]
        if windowSum >= k * threshold:
                count += 1
        
        # now, we begin with the first window and iterate
        for high in range(k, len(arr)):
            windowSum -= arr[low]
            windowSum += arr[high]
            if windowSum >= k * threshold:
                count += 1
            low += 1
        

        return count
        





if __name__ == '__main__':
    s = Solution()
    test = s.numOfSubarrays([11,13,17,23,29,31,7,5,2,3], 3, 5) # ([2,2,2,2,5,5,5,8], 3, 4)
    # test = s.numOfSubarrays(x_test, 50000, 2000)
    print("solution =", test)