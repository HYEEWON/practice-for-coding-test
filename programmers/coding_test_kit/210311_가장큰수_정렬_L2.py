def solution(numbers):
    numbers = list(map(str, numbers))
    #for i in range(len(numbers)):
    #    numbers[i] = str(numbers[i])
    numbers = sorted(numbers, key=lambda x: x*3, reverse=True)
    # 3번 정렬 -> 숫자가 1000 이하이기 때문
    return str(int(''.join(numbers)))

print(solution([3, 30, 34, 5, 9]))
#print(solution([0, 0, 0, 0, 0]))