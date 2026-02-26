import math

def solution(clothes):
    
    clothes_dict = {}
    
    for c, t in clothes:
        if t not in clothes_dict:
            clothes_dict[t] = 2 # (a+1)(b+1)(c+1)... 일테니까
        else:
            clothes_dict[t] += 1
    
    answer = math.prod(clothes_dict.values()) - 1
    
    return answer