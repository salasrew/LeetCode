class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        # dictionary for storing string 
        dic = {}
        # spilt s and save to list
        lst = s.split()

        lenPattern = len(pattern)
        lenLst = len(lst)

        if lenPattern != lenLst:
            return False

        # store word in dict
        for i in range(lenPattern):
            if pattern[i] not in dic:
                dic[pattern[i]] = lst[i]
            else:
                if dic[pattern[i]]!= lst[i]:
                    return False
        if len(set(lst)) != len(set(pattern)):
            return False

        return True
        
