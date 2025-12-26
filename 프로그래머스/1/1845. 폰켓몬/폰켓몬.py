from collections import Counter

def solution(nums):
    n = len(nums) // 2
    counts = list(Counter(nums).values())
    if len(counts) >= n:
        return n
    else:
        return(len(counts))
