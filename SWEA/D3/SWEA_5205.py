def lomuto(low, high):
    def partition(low, high):
        pivot = a[high]
        left = low

        for right in range(low, high):
            if a[right] < pivot:
                a[right], a[left] = a[left], a[right]
                left += 1

        a[left], a[high] = a[high], a[left]

        return left

    if low < high:
        pivot = partition(low, high)
        lomuto(low, pivot-1)
        lomuto(pivot+1, high)

testcase = int(input())
for tc in range(1, testcase+1):
    N = int(input())
    a = list(map(int, input().split()))
    lomuto(0, N-1)
    print(f'#{tc} {a[N//2]}')
