import sys

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # the time complexity of the solution must be O(log(m+n))
        # the naive solutions: 
        #  - binary insert all the elements into a new array, then get the middle element: O(n * (log n + cost of inserts))
        #  - loop n times where n = len(nums1 + nums2)/2. store indices at the start of both lists, and increment the pointer to the lower of the two values: O(n/2)
        
        # better solution: O(log(min(M, N)))
        #  make 2 cuts such that nums1 = [... L1|R1 ...], nums2 = [... L2|R2 ...] and we must ensure that: L1 <= R1 && L1 <= R2 && L2 <= R1 && L2 <= R2
        #  L1 <= R1 and L2 <= R2 are guaranteed because nums1 and nums2 are sorted, so we must only make sure that L1 <= R2 and L2 <= R1
        #  Use binary search to find the right cut

        # for simplicity, nums1 will always point to the smaller of the two lists
        if len(nums2)<len(nums1):
            nums1, nums2 = nums2, nums1
        
        n1 = len(nums1)
        n2 = len(nums2)

        l, r = 0, n1
        while l <= r:
            cut1 = (l + r)//2
            cut2 = (n1 + n2)//2 - cut1 # the second cut can be found based on the first cut

            # for the edge case where the cut is at the end of the list, we must use sys.maxint
            l1 = -sys.maxsize-1 if cut1 == 0 else nums1[cut1-1]
            l2 = -sys.maxsize-1 if cut2 == 0 else nums2[cut2-1]
            r1 = sys.maxsize if cut1 == n1 else nums1[cut1]
            r2 = sys.maxsize if cut2 == n2 else nums2[cut2]

            # perform the binary search
            if l1 > r2: r = cut1-1
            elif l2 > r1: l = cut1+1
            else:
                # print("({}, {}) + ({}, {})/2.0".format(l1, l2, r1, r2))
                # print(n1 + n2 % 2)
                if (n1+n2) % 2 == 1:
                    return min(r1, r2)
                else:
                    return (max(l1, l2) + min(r1, r2))/2.0
        


        return -1

            

            

            



if __name__ == '__main__':
    s = Solution()
    # test = s.findMedianSortedArrays([1, 3, 4, 5, 19], [2, 6, 10])
    test = s.findMedianSortedArrays([1, 2], [1,2,3])

    print(test)