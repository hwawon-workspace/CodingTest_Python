# bfs?
from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    q = deque([(begin, 0)])
    while q:
        curr, cnt = q.popleft()
        if curr == target:
            return cnt
        
        for word in words:
            diff = 0
            for i in range(len(word)):
                if word[i] != curr[i]:
                    diff +=  1
            if diff == 1:
                q.append((word, cnt+1))

    return 0