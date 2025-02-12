# Solution 1
# class Solution(object):
#     def longestCommonPrefix(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: str
#         """
#         prefix = ""
#         i=0
#         while True:
#             currentChar = ""
#             if len(strs[0])<=i:
#                 return prefix
#             else:
#                 currentChar = strs[0][i]
            
#             for string in strs:
#                 if len(string)<=i:
#                     return prefix
#                 else:
#                     if string[i] != currentChar:
#                         return prefix
#             prefix += currentChar
#             i+=1
#         # return prefix

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        i=0
        strs = sorted(strs)
        first = strs[0]
        last = strs[-1]
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return prefix
            else:
                prefix += first[i]


        return prefix






if __name__ == '__main__':
    s = Solution()

    print(s.longestCommonPrefix(["flower","flow","flight"]))
    print(s.longestCommonPrefix(["dog","racecar","car"]))