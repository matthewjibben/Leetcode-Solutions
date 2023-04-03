class Solution(object):
    # def lengthOfLongestSubstring(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
    #     # naive solution: loop through each character in the string, and then make a substring moving forward until you cannot anymore
    #     # do this for every character: O(n^2)
    #     # to make this slightly better: skip letters. When you find a repeated letter, skip loops until after the first instance
    #     #  because it is impossible to have a longer substring until after that

    #     i = 0
    #     maximum = 0
    #     while i < len(s):
    #         print("Start:", s[i])
    #         substring_hm = {}
    #         for c in s[i:]:
    #             if c not in substring_hm:
    #                 substring_hm[c] = 1
    #             else:
    #                 # if there is a repeated character, skip all characters until after the first instance 
    #                 skip = s.find(c, i)
    #                 i += skip - i
    #                 break
    #         maximum = max(maximum, len(substring_hm))

    #         i += 1
            

    #     return maximum
    
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # better solution: use a sliding window to only loop through the string one time. use a hashmap to have O(1) lookups 
        # loop through each character, creating a "right" side of the window. increase the right side until we find a character already in the window
        # then, move the left side (removing characters as you do) until the character is removed. Return the largest length of the window
        charset = set()
        maximum = 0
        left = 0
        for right in range(len(s)):
            if s[right] not in charset:
                charset.add(s[right])
                maximum = max(maximum, right - left + 1)
            else:
                # move the sliding window until we have removed the repeated character
                while s[right] in charset:
                    charset.remove(s[left])
                    left += 1
                charset.add(s[right])
                maximum = max(maximum, right - left + 1)
        
        return maximum
                





if __name__ == '__main__':
    s = Solution()
    test = s.lengthOfLongestSubstring("pwwkew") # ("bbtablud")
    print(test)