# 오른쪽부터 왼쪽으로 가면서 0 찾기
# 0 찾으면 1로 바꾸고 다시 왼쪽으로 가면서 1찾기
# 1찾으면 0으로 바꾸기
# 0이 없다면 모두 1이므로, 맨 왼쪽에 한자리 추가하고 두자리를 '10'으로 바꾸기

def solution(numbers):
    
    # 이진수로 변환
    def convert_to_binary(number):
        if number < 2:
            return str(number)
        if number % 2:
            return convert_to_binary(number // 2) + '1'
        else:
            return convert_to_binary(number // 2) + '0'
    
    # 십진수로 변환
    def convert_to_decimal(number):
        if len(number) == 1:
            return int(number)
        if number[0] == '1':
            return convert_to_decimal(number[1:]) + 2 ** (len(number)-1)
        return convert_to_decimal(number[1:])
        
    answer = []
    for number in numbers:
        binary = list(convert_to_binary(number))
        
        for i in range(len(binary)-1, -1, -1):
            if binary[i] == '0':
                binary[i] = '1'
                for j in range(i+1, len(binary)):
                    if binary[j] == '1':
                        binary[j] = '0'
                        break
                break
        else:
            binary = ['1', '0'] + ['1'] * (len(binary) - 1)
            
        str_binary = ''.join(binary)
        new_number = convert_to_decimal(str_binary)
        answer.append(new_number)
        
    return answer