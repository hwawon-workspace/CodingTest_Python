import numpy as np

def solution(arr):
    diffs = np.diff(arr) # 다음 값과 차이
    # print(arr)
    # print(diffs)
    idx = list(np.where(diffs != 0)[0]) # 차이가 0 아닌(다음 값과 다른) 인덱스 저장
    idx.append(-1) # 배열의 마지막 값은 비교할 값 X
    # print(idx)
    answer = []
    for i in idx:
        answer.append(arr[i]) # arr에서 idx 추출
    return answer