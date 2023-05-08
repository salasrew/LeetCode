# 2133. Check if Every Row and Column Contains All Numbers

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        # Problem solving ideas
        # 1.Count every number of row and store in Dict 
        # 2.if max(dic.values()) > i+1 means there's a duplicated number
        # 3.Make all the element zero in dict 
        # 4.Count every number of column and store in Dict 
        # goto 2 again and if false then True
        
        dic = {}
        matLen = len(matrix)

        for i in range(1,matLen+1):
            dic[i] = 0
        for i in range(matLen):
            for j in range(matLen):
                dic[matrix[i][j]] +=1
            if max(dic.values())==i+1:
                pass
            else:
                return False
        for i in range(1,matLen+1):
            dic[i] = 0
        # 
        for i in range(matLen):
            for j in range(matLen):
                dic[matrix[j][i]] +=1
            if max(dic.values())==i+1:
                pass
            else:
                return False

        return True
