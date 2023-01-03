def solution(survey, choices):
    score_dict = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    answer = ''
    
    # 점수 매기기
    for idx in range(len(survey)):
        # 매우 비동의, 비동의, 약간 비동의
        if choices[idx] < 4:
            score_dict[survey[idx][0]] += 4 - choices[idx]
        # 약간 동의, 동의, 매우 동의
        elif choices[idx] > 4:
            score_dict[survey[idx][1]] += choices[idx] - 4
    
    # 점수 비교(점수 같으면 사전 순)
    if score_dict['R'] >= score_dict['T']:
        answer += 'R'
    else:
        answer += 'T'
    if score_dict['C'] >= score_dict['F']:
        answer += 'C'
    else:
        answer += 'F'
    if score_dict['J'] >= score_dict['M']:
        answer += 'J'
    else:
        answer += 'M'
    if score_dict['A'] >= score_dict['N']:
        answer += 'A'
    else:
        answer += 'N'

    return answer