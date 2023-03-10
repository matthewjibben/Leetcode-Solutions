class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        val = 0
        vdict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        i=0
        while i < len(s):
            # for each character, add the value unless the next character will use subtraction
            if i+1 <= len(s)-1:
                if s[i]=='I':
                    if s[i+1] == 'V' or s[i+1] == 'X':
                        val += vdict[s[i+1]] - vdict[s[i]]
                        i+=1
                    else:
                        val += vdict[s[i]]
                elif s[i]=='X':
                    if s[i+1] == 'L' or s[i+1] == 'C':
                        val += vdict[s[i+1]] - vdict[s[i]]
                        i+=1
                    else:
                        val += vdict[s[i]]
                elif s[i]=='C':
                    if s[i+1] == 'D' or s[i+1] == 'M':
                        val += vdict[s[i+1]] - vdict[s[i]]
                        i+=1
                    else:
                        val += vdict[s[i]]
                else:
                    val += vdict[s[i]]
            else:
                val += vdict[s[i]]
            
            i+=1
        
        return val



if __name__ == '__main__':
    s = Solution()
    test = s.romanToInt("MCMXCIV")
    print(test)