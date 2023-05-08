# 走左斜線
# 走右斜線
# 如果len(mat) is odd
# sum = sum - duplicated (center of the matrix)
# 
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        mat_len = len(mat)
        sum = 0
        for i in range(mat_len):
            sum += (mat[i][i] + mat[i][mat_len-1-i])

        if mat_len%2==1:
            sum = sum - mat[mat_len//2][mat_len//2]

        return sum
