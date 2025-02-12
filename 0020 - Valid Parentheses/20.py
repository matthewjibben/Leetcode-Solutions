class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        
        for c in s:
            if c in ["(", "[", "{"]:
                stack.append(c)
            else:
                if len(stack)==0:
                    return False
                open_paren = stack.pop()
                if open_paren+c not in ["()", "[]", "{}"]:
                    return False
        
        return len(stack)==0
        



if __name__ == '__main__':
    s = Solution()
    print(s.isValid("()"))
    print(s.isValid("()[]{}"))
    print(s.isValid("(}"))
    print(s.isValid("(()"))
    print(s.isValid(")"))

