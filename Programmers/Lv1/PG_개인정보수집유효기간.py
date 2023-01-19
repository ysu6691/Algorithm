def solution(today, terms, privacies):
    
    # 오늘 정보 저장
    today_year = int(today[:4])
    today_month = int(today[5:7])
    today_day = int(today[8:])
    
    # 약관마다 유효기간 저장
    term_dict = dict()
    for term in terms:
        term_dict[term[0]] = int(term[2:])
        
    answer = []
    for idx in range(len(privacies)):
        # 수집된 개인정보의 수집일자와 약관 저장
        privacy = privacies[idx]
        privacy_year = int(privacy[:4])
        privacy_month = int(privacy[5:7])
        privacy_day = int(privacy[8:10])
        privacy_term = privacy[-1]
        
        # 해당 약관만큼 날짜 더하기
        privacy_month += term_dict[privacy_term]
        privacy_year += (privacy_month-1) // 12
        privacy_month %= 12
        if not privacy_month:
            privacy_month = 12
        
        # 유효기간 지난 개인정보만 저장
        if today_year > privacy_year:
            answer.append(idx+1)
            continue
        elif today_year == privacy_year:
            if today_month > privacy_month:
                answer.append(idx+1)
                continue
            elif today_month == privacy_month:
                if today_day > privacy_day - 1:
                    answer.append(idx+1)
        
    return answer