def solution(scores):
    
    sorted_scores = sorted(scores[1:], key=lambda x: (-x[0], x[1]))
    
    target_score = scores[0]
    total_score = sum(target_score)
    max_score = -1
    answer = 1
    for score in sorted_scores:
        if score[0] > target_score[0] and score[1] > target_score[1]:
            return -1
        if score[1] >= max_score:
            max_score = score[1]
            if sum(score) > total_score:
                answer += 1
        
    return answer