import sys
sys.stdin = open('input1.txt', 'r')


for testcase in range(10):
    input()
    case = list(map(int, input().split()))
    answer = 0
    for i in range(2, len(case)-2):
        high = max(case[i-1], case[i-2], case[i+1], case[i+2])
        if case[i] > high:
            answer += case[i] - high
    print(f'#{testcase+1} {answer}')
