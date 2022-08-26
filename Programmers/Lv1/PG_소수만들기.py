def solution(nums):

    def comb(idx, sidx):
        if sidx == 3:
            nums_list.append(selection[:])
            return

        if idx == len(nums):
            return

        selection[sidx] = nums[idx]
        comb(idx+1, sidx+1)
        comb(idx+1, sidx)

    check = [0] * len(nums)
    selection = [0] * 3
    nums_list = []

    comb(0, 0)
    answer = 0

    for nums in nums_list:
        acc = 0

        for num in nums:
            acc += num

        for i in range(2, acc):
            if not acc % i:
                break
        else:
            answer += 1

    return answer
