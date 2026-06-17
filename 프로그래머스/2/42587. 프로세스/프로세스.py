from collections import deque

def solution(priorities, location):
    # location 추적하려면 순서와 값 튜플 형태로 묶어주기
    queue = deque([(p,i) for i, p in enumerate(priorities)])
    cnt = 0
    
    # 큐 있는 동안 반복
    while queue:
        # 비교할 현재의 pop값
        priority, idx = queue.popleft()
        if any(priority < p for p,_ in queue):
            queue.append((priority, idx))
        else:
            cnt += 1
            if idx == location:
                return cnt