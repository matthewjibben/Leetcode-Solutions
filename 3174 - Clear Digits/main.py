class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        # potential solutions:
        #  A: loop through each character and if it is a digit, create a string slice to remove it and the character before
        #     This is bad because slices are new strings, so this uses a lot of memory
        #  B: convert the string to a deque of characters, then loop through and delete the value if the next character is a digit
        #     Uses O(n) space complexity to copy the character, and O(n) time to loop through the string
        #  C: do some insane regex stuff
        #     runs into the same problem as solution A, presumably
        #  D: Or, we are massively overcomplicating this. 
        #     loop over the original string, and add characters to a list as you go. If it is a digit, pop the last element in the list
        #     Uses O(n) space and O(n) time

        digits = "0123456789"
        result = []
        for i in s:
            # print(i)
            if i not in digits:
                result += i
            else:
                if len(result) > 0:
                    result.pop()
        
        return ''.join(result)




if __name__ == '__main__':
    s = Solution()

    print("s =", s.clearDigits("abc"))
    print("s =", s.clearDigits("cbrt34323121"))