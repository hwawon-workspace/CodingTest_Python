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