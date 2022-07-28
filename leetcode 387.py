class Solution:
    def firstUniqChar(self, s: str) -> int:
        # quantity
        dic = {}
        # index
        dic2 = {} 
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = 0 
            if s[i] not in dic2:
                dic2[s[i]] = i
            dic[s[i]] +=1
        for i in dic:
            if dic[i]==1:
                return dic2[i]
        return -1
