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