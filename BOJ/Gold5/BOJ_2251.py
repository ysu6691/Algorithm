# 재귀함수 이용

# A, B, C 용량 저장
VA, VB, VC = map(int, input().split())
comb = set()
result = set()

def pour(A, B, C, check):
    # A가 비어있다면, 그 때의 C 저장
    if not A:
        result.add(C)

    # C에 물이 들어있고, 방금 전 재귀에서 C를 붓지 않았다면,
    if C and check != 'c':
        
        # C -> A로 물 붓기
        tmp_A = A
        tmp_C = C
        # A가 꽉 차거나 C가 바닥날 때까지
        while tmp_A < VB and tmp_C > 0:
            tmp_A += 1
            tmp_C -= 1

        # 만약 A,B,C의 물 양이 처음 찾은 조합이라면, 기억하고 다음 재귀로
        if (tmp_A, B, tmp_C) not in comb:
            comb.add((tmp_A, B, tmp_C))
            pour(tmp_A, B, tmp_C, 'c')
        else:
            pass

        # C -> B로 물 붓기
        tmp_B = B
        tmp_C = C
        while tmp_B < VB and tmp_C > 0:
            tmp_B += 1
            tmp_C -= 1
        if (A, tmp_B, tmp_C) not in comb:
            comb.add((A, tmp_B, tmp_C))
            pour(A, tmp_B, tmp_C, 'c')
        else:
            pass

    # B와 A도 마찬가지
    if B and check != 'b':
        tmp_A = A
        tmp_B = B
        while tmp_A < VA and tmp_B > 0:
            tmp_A += 1
            tmp_B -= 1
        if (tmp_A, tmp_B, C) not in comb:
            comb.add((tmp_A, tmp_B, C))
            pour(tmp_A, tmp_B, C, 'b')
        else:
            pass

        tmp_C = C
        tmp_B = B
        while tmp_C < VC and tmp_B > 0:
            tmp_C += 1
            tmp_B -= 1
        if (A, tmp_B, tmp_C) not in comb:
            comb.add((A, tmp_B, tmp_C))
            pour(A, tmp_B, tmp_C, 'b')
        else:
            pass

    if A and check != 'a':
        tmp_B = B
        tmp_A = A
        while tmp_B < VB and tmp_A > 0:
            tmp_B += 1
            tmp_A -= 1
        if (tmp_A, tmp_B, C) not in comb:
            comb.add((tmp_A, tmp_B, C))
            pour(tmp_A, tmp_B, C, 'a')
        else:
            pass

        tmp_C = C
        tmp_A = A
        while tmp_C < VC and tmp_A > 0:
            tmp_C += 1
            tmp_A -= 1
        if (tmp_A, B, tmp_C) not in comb:
            comb.add((tmp_A, B, tmp_C))
            pour(tmp_A, B, tmp_C, 'a')
        else:
            pass


pour(0, 0, VC, 0)
result = sorted(list(result))

print(' '.join(map(str, result)))
