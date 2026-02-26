from itertools import combinations
import math

def solution(clothes): 
    # 옷 종류별 분류
    clothes_dict = {}
    for cloth in clothes:
        c_name = cloth[0]
        c_type = cloth[1]
        if c_type not in clothes_dict.keys():
            clothes_dict[c_type] = []
        clothes_dict[c_type].append(c_name)
    
    # 종류별 옷 개수
    length = [len(v) for v in clothes_dict.values()]

    # 옷 조합
    answer = 1
    for l in length:
        answer *= (l + 1)
    answer -= 1
        
    # for r in range(1, len(length)+1):
    #     for comb in combinations(length, r):
    #         answer += math.prod(comb)
    return answer