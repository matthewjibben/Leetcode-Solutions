# 986. Interval List Intersections
# https://leetcode.com/problems/interval-list-intersections/description/

# Solutions:
# Solution A: O(n) time and space
#   loop until we have reached the end of both lists
#   Find if the current two lists overlap (the top of one of them comes after the bottom of the other)
#     if so, the range either partially contains the other, or fully encapsulates it. range = [max(firstBot, secondBot), min(firstTop, secondTop)]
#   iterate on the list with the lower range (use the top of the range to determine this)

class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        if(firstList==[] or secondList==[]):
            return []
        
        i = 0
        j = 0
        answer = []
        while(i < len(firstList) and j < len(secondList)):
            rangeA = firstList[i]
            rangeB = secondList[j]

            if(rangeA[0] > rangeB[1] or rangeB[0] > rangeA[1]):
                # ranges do not overlap, go next 
                pass
            elif(rangeA[1] > rangeB[0] or rangeB[1] > rangeA[0]):
                # print("values= ", [rangeA[0], rangeA[1]], [rangeB[0], rangeB[1]])
                # print("range= ", [max(rangeA[0], rangeB[0]), min(rangeA[1], rangeB[1])])
                # print(rangeA[1], ">", rangeB[0], " or ", rangeB[1], ">", rangeA[0])
                answer.append([max(rangeA[0], rangeB[0]), min(rangeA[1], rangeB[1])])
            
            if(rangeA[1] <= rangeB[1]):
                i += 1
            else:
                j += 1
        
        return answer


        




if __name__ == '__main__':
    firstList  = [[0,2],[5,10],[13,23],[24,25]]
    secondList = [[1,5],[8,12],[15,24],[25,26]]
    s = Solution()
    # test = s.intervalIntersection(firstList, secondList)
    # print("solution =", test)

    firstList = [[14,16]]
    secondList = [[7,13],[16,20]]
    test = s.intervalIntersection(firstList, secondList)
    print("solution =", test)