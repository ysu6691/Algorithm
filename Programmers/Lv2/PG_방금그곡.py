def solution(m, musicinfos):
    max_time = -1
    answer = '(None)'
    
    for musicinfo in musicinfos:
        # 음악 정보 저장
        start, end, music, original = musicinfo.split(',')
        start_hour = int(start[:2])
        start_minute = int(start[3:])
        end_hour = int(end[:2])
        end_minute = int(end[3:])

        # 라디오에서 재생된 시간 저장
        total_time = (end_hour - start_hour) * 60
        if end_minute - start_minute < 0:
            total_time -= start_minute - end_minute
        else:
            total_time += end_minute - start_minute

        # 라디오에서 실제로 재생된 멜로디를 리스트로 저장
        original_list = []
        idx = 0
        while idx < len(original):
            original_list.append(original[idx])
            # '#'을 만나면 한 음으로 처리
            if idx + 1 < len(original) and original[idx+1] == '#':
                original_list[-1] += '#'
                idx += 1
            idx += 1
        # 재생된 시간만큼 반복되도록 다시 저장
        original_list = original_list * (total_time // len(original_list)) + original_list[:total_time % len(original_list)]
        # 다시 문자열로
        original = ''.join(original_list)

        # 완전탐색
        for i in range(len(original)):
            # 첫 음이 같으면 while문 실행
            if original[i] == m[0]:
                j = 0
                flag = False
                while i + j < len(original):
                    # 음이 달라지면 break
                    if original[i+j] != m[j]:
                        break
                    j += 1
                    # 찾던 멜로디를 찾았다면,
                    if j == len(m):
                        # 끝이 '#'이 아닌데 '#'으로 끝나지는 않는지 확인
                        if i + j < len(original) and original[i + j] == '#':
                            break
                        flag = True
                        break
                # 가장 긴 재생 시간 중 가장 먼저 찾은 멜로디를 저장
                if flag and total_time > max_time:
                    max_time = total_time
                    answer = music
                    break

    return answer
