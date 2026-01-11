# 1.  deque, popleft 활용한 직관적 풀이
from collections import deque

def solution(progresses, speeds):
    progresses = deque(progresses)
    speeds = deque(speeds)
    dist = []
    
    while len(progresses) != 0:
        # progresses = [p + s for p, s in zip(progresses, speeds)] # 이렇게 할 경우  deque 계속 다시해줘야 함
        for  i in range(len(progresses):
            progresses[i] += speeds[i]
            
        cnt = 0
        while len(progresses)!= 0 and progresses[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            cnt += 1
            
        if cnt != 0:
            dist.append(cnt)
        
    return dist


# 2. "시간" 위주 계산한 압축형 풀이
def solution(progresses, speeds):
    Q=[] # Q: [[배포일, 배포될 개수],...,[]]
    for p, s in zip(progresses, speeds):
        if len(Q) == 0 or Q[-1][0] < -((p-100)//s): # 현재 p의 배포일이 앞 작업의 배포일보다 늦을 경우
            Q.append([-((p-100)//s),1]) # Q에 새로 추가
        else:
            Q[-1][1]+=1 # 현재 p의 배포일이 앞 작업의 배포일보다 이르거나 같을 경우, 같은 리스트에 배포 개수를 추가
    return [q[1] for q in Q]
