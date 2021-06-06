class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = collections.Counter(s)
        
        for i in range(0,len(s)):
            if dic[s[i]]==1:
                return i
            
        return -1
