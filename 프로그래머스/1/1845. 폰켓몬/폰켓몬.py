from collections import Counter
def solution(nums):
    n = len(nums) // 2
    print(f'n')
    nums.sort()
    counts = list(Counter(nums).values())
    counts.sort()
    print(counts)
    if len(counts) >= n:
        return n
    else:
        return(len(counts))