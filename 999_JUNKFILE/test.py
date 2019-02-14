import sys
sys.stdin = open('input (6).txt', 'r')

number = int(input())
for i in range(number):
    problem = input()
    problem = problem.lstrip('0')
    if not len(problem):
        print(f'#{i+1} 0')
    else:
        answer = problem[0]
        if len(problem) > 1:
            for s in range(1, len(problem)):
                if problem[s] != problem[s-1]:
                    answer += problem[s]
            result = len(answer)
            print(f'#{i+1} {result}')
        else:
            print(f'#{i+1} 1')