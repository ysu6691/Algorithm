def solution(record):
    last_nickname = dict() # {user_id: 가장 마지막 닉네임}
    history = [] # [명령어, user_id]
    
    for action in record:
        if action[:5] == 'Leave':
            command, user_id = action.split()
        else:
            command, user_id, nickname = action.split()
        
        # 어떤 유저가 들어왔는지 저장하고 마지막 닉네임 기억
        if command == 'Enter':
            history.append(['enter', user_id])
            last_nickname[user_id] = nickname
            
        # 어떤 유저가 나갔는지 저장
        elif command == 'Leave':
            history.append(['leave', user_id])
        
        # 마지막 닉네임 기억
        elif command == 'Change':
            last_nickname[user_id] = nickname
            
    answer = []
    for action in history:
        user_id = action[1]
        if action[0] == 'enter':
            answer.append(f'{last_nickname[user_id]}님이 들어왔습니다.')
        elif action[0] == 'leave':
            answer.append(f'{last_nickname[user_id]}님이 나갔습니다.')
    
    return answer