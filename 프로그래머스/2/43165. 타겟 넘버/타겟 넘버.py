# 모든 경우의 수 -> DFS
def solution(numbers, target):
    sums = []
    
    def dfs(idx, current_sum):
        if idx == len(numbers):
            sums.append(current_sum)
            return

        dfs(idx+1, current_sum + numbers[idx])
        dfs(idx+1, current_sum - numbers[idx])
    
    dfs(0, 0)
    return sums.count(target)