class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        '''
            最小有可能是 mins 
            最大可能是 temp //2 
        '''
    
        dic = {"b":0,"a":0,"l":0,"o":0,"n":0}
        
        for i in text:
            if i in dic:
                dic[i]+=1
                
        temp_min = dic[min(dic, key=dic.get)]
        
        if temp_min==0:
            return 0
   
        temp = min(dic["l"],dic["o"]) //2
        
        if temp== temp_min:
            return temp
        
        return min(temp_min,temp)
        
        


        
        
        
