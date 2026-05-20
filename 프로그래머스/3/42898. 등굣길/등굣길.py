# Bottom-up 방식
def solution(m, n, puddles):
    dp = [[0]*m for _ in range(n)]
    for y, x in puddles:
        dp[x-1][y-1] = -1
    
    dp[0][0] = 1
    
    for i in range(n):
        for j in range(m):
            if dp[i][j] == -1:
                dp[i][j] =0
                continue
            
            if i == 0 and j == 0:
                continue
            
            from_up = dp[i-1][j] if i > 0 else 0
            from_left = dp[i][j-1] if j > 0 else 0
            
            dp[i][j] = (from_up + from_left) % 1000000007
    return dp[n-1][m-1]