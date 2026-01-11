from collections import deque

def solution(progresses, speeds):
    dist = []
    
    while len(progresses) != 0:
        progresses = [p + s for p, s in zip(progresses, speeds)]
        progresses = deque(progresses)
        speeds = deque(speeds)
        cnt = 0
        
        while len(progresses)!= 0 and progresses[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            cnt += 1
        if cnt != 0:
            dist.append(cnt)
        
    return dist