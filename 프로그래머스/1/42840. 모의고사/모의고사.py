# 1. 내 풀이
# 문제점: 불필요한 array 변환, 간결하지 않은 코드
import numpy as np

def solution(answers):
    score = [0, 0, 0, 0]
    st1 = [1,2,3,4,5]
    st2 = [2,1,2,3,2,4,2,5]
    st3 = [3,3,1,1,2,2,4,4,5,5]
    
    n = len(answers)
    st1_len = divmod(n, len(st1))
    st2_len = divmod(n, len(st2))
    st3_len = divmod(n, len(st3))

    st1 = st1 * st1_len[0] + st1[:st1_len[1]]
    st2 = st2 * st2_len[0] + st2[:st2_len[1]]
    st3 = st3 * st3_len[0] + st3[:st3_len[1]]

    score[1] = sum(np.array(st1) == np.array(answers))
    score[2] = sum(np.array(st2) == np.array(answers))
    score[3] = sum(np.array(st3) == np.array(answers))
    
    indexes = np.where(np.array(score) == max(np.array(score)))[0].tolist()
    
    return indexes


# 2. 간결한 풀이
def solution(answers):
    scores =  [0, 0, 0]
    st1 = [1,2,3,4,5]
    st2 = [2,1,2,3,2,4,2,5]
    st3 = [3,3,1,1,2,2,4,4,5,5]
    answer = []

    for idx, ans in enumerate(answers):
        if ans == st1[idx % len(st1)]:
            scores[0] += 1
        if ans == st2[idx % len(st2)]:
            scores[1] += 1
        if ans == st3[idx % len(st3)]:
            scores[2] += 1

    for idx, score in enumerate(scores):
        if score == max(scores):
            answer.append(idx + 1)

    return answer


# 3. cycle 활용 풀이
from itertools import cycle

def solution(answers):
    scores = [0, 0, 0]
    giveups = [ cycle([1,2,3,4,5]),
                cycle([2,1,2,3,2,4,2,5]),
                cycle([3,3,1,1,2,2,4,4,5,5])
              ]
    
    for ans in answers:
        for idx in range(len(giveups)):
            if next(giveups[idx]) == ans:
                scores[idx] += 1
                
    best = max(scores)

    return [idx+1 for idx, score in enumerate(scores) if score == best]
