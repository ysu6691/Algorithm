testcase = int(input())

for tc in range(1, testcase+1):
    H, W, N = map(int, input().split())
    words = list(input().split())
    answer = 0
    size = 1 # 현재 직사각형 크기

    # 최대 사이즈 나올 때까지 반복
    while True:
        current_h = size # 현재 차지하는 높이 (초기값: 직사각형의 높이)
        current_w = 0 # 현재 차지하는 너비
        flag = False

        for word in words:
            # 만약 간판의 길이보다 큰 단어가 있다면, break
            if len(word) * size > W:
                flag = True
                break

            # 현재 단어의 길이만큼 이동
            current_w += len(word) * size

            # 만약 간판의 총 너비를 넘어갔다면,
            if current_w > W:
                current_h += size # 다음 줄로 이동
                current_w = len(word) * size + size # 현재 너비는 글자 길이 + 공백

            # 아직 간판을 안 넘어갔다면,
            else:
                current_w += size # 공백 한 칸 띄우기

            # 만약 다음 줄로 이동했을 때 간판의 총 세로 길이를 넘어갔다면, break
            if current_h > H:
                flag = True
                break

        if flag:
            break
        answer += 1
        size += 1

    print(f'#{tc} {answer}')