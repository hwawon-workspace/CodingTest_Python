from itertools import permutations

def solution(k, dungeons):
    answer = 0
    for p in permutations(dungeons, len(dungeons)): # 모든 가능한 순서
        tmp = k # 각 순서에서의 임시 피로도
        cnt = 0 # 각 순서에서의 탐험 가능 던전 수
        for need, red in p: # 순서의 던전들 탐험 시 피로도 소모 구현
            if need <= tmp:
                tmp -= red # 소모 완료 
                cnt += 1 # 던전 탐험 완료
        answer = max(answer, cnt) # 갱신
    return answer