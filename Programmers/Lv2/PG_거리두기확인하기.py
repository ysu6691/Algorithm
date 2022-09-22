def solution(places):
    answer = [1, 1, 1, 1, 1]

    for p in range(5):
        place = places[p]
        print(place)
        finish = False
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    if i < 4:
                        if place[i+1][j] == 'P':
                            answer[p] = 0
                            finish = True
                            break
                    if j < 4:
                        if place[i][j+1] == 'P':
                            answer[p] = 0
                            finish = True
                            break
                    if i < 4 and j > 0:
                        if place[i+1][j-1] == 'P':
                            if place[i+1][j] != 'X' or place[i][j-1] != 'X':
                                answer[p] = 0
                                finish = True
                                break
                    if i < 4 and j < 4:
                        if place[i+1][j+1] == 'P':
                            if place[i+1][j] != 'X' or place[i][j+1] != 'X':
                                answer[p] = 0
                                finish = True
                                break
                    if i < 3:
                        if place[i+2][j] == 'P' and place[i+1][j] != 'X':
                            answer[p] = 0
                            finish = True
                            break
                    if j < 3:
                        if place[i][j+2] == 'P' and place[i][j+1] != 'X':
                            answer[p] = 0
                            finish = True
                            break

            if finish:
                break

    return answer

print(solution(a))