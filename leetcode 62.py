class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 8!/(2!*6!)
        # 40320 2 720
        ans,n_ = 1,1
    
        if m < n:
            n , m = m , n

        for i in range(m+n-2,m-1,-1):
            ans *= i 
        for i in range(n-1,1,-1):
            n_ *= i            
        return int(ans / n_)
