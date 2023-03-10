class Solution(object):
    # def isPalindrome(self, x):
    #     """
    #     :type x: int
    #     :rtype: bool
    #     """
    #     # converting to string is not allowed
    #     if x<0:
    #         return False
        
    #     l = []
    #     while x != 0:
    #         # append the last digit, then div by 10
    #         l.append(x%10)
    #         x//=10
        
    #     for i in range(len(l)//2):
    #         if l[i] != l[len(l)-1-i]:
    #             return False
        
    #     return True
    
    def isPalindrome(self, x):
        if x<0:
            return False
        
        original = x
        reverse = 0
        while x != 0:
            reverse = reverse*10 + x%10
            x//=10
        
        return reverse==original




if __name__ == '__main__':
    s = Solution()
    test = s.isPalindrome(180081)
    print(test)