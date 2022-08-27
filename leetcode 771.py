class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dic = {}
        sums = 0
        
        for i in stones:
            dic[i] = 0
        for i in stones:
            dic[i] += 1 
        
        for i in jewels:
            if i in stones:
                sums += dic[i]
            
        return sums
