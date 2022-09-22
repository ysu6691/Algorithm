def solution(n, k):

    def transform(n, result):
        if n < k:
            return str(n) + result

        else:
            for i in range(k):
                if n % k == i:
                    return transform(n // k, str(i) + result)

    def isPrimeNumber(n):
        for i in range(2, int(n**(1/2)+1)):
            if n % i == 0:
                return False
        return True

    text = transform(n, '')
    num_list = []
    start = 0
    end = 1

    if len(text) == 1 and text != '1':
        num_list.append(int(text))

    while end < len(text):
        if text[end] == '0':
            if '0' not in text[start+1:end] and text[start:end] != '1' and int(text[start:end]) != 0:
                num_list.append(int(text[start:end]))
            start = end + 1
            end += 1
        end += 1
        if end == len(text):
            if int(text[start:]) != 1 and int(text[start:]) != 0:
                num_list.append(int(text[start:]))

    answer = 0
    for num in num_list:
        if isPrimeNumber(num):
            answer += 1

    return answer