# 전체 경우의 수 구해야 함 -> Bottom-up, for문
def solution(n, money):
    MOD = 1000000007
    
    dp = [0] * (n+1) # 0원~ n원까지 만들 수 있는 경우의 수

    # 현재 있는 동전으로 만들 수 있는 모든 금액의 경우의 수
    dp[0] = 1
    for m in money:
        for price in range(m, n+1):
            dp[price] += dp[price-m]
            dp[price] %= MOD
    
    return dp[n]