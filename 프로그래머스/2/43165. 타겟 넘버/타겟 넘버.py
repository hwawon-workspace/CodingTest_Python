# recursion 풀이
def solution(numbers, target):
    def dfs(cnt, current_sum):
        if cnt == len(numbers):
            if current_sum == target:
                return 1
            else:
                return 0

        return dfs(cnt + 1, current_sum + numbers[cnt]) + dfs(cnt + 1, current_sum - numbers[cnt])

    return dfs(0, 0)

# map, product 활용 풀이
from itertools import product

def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)
