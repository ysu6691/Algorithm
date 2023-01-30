def solution(s):
    idx_dict = dict()
    answer = []
    
    for idx in range(len(s)):
        char = s[idx]
        if char not in idx_dict:
            idx_dict[char] = idx
            answer.append(-1)
        else:
            answer.append(idx - idx_dict[char])
            idx_dict[char] = idx
            
    return answer