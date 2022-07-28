class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # to store str s's char's quantity 
        dic = {}
        # to store str t's char's quantity 
        dic2 = {}
        
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = 0
            dic[s[i]] += 1
            
        for i in range(len(t)):
            if t[i] not in dic2:
                dic2[t[i]] = 0
            dic2[t[i]] += 1
            
        return dic==dic2
