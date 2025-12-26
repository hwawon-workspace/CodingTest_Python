from collections import Counter
# def solution(participant, completion):
#     notcom = participant.copy()
#     for c in completion:
#         if c in notcom:
#             notcom.remove(c)
#     answer = notcom.pop()
#     return answer

def solution(participant, completion):
    answer = list((Counter(participant) - Counter(completion)).keys())[0]
    return answer