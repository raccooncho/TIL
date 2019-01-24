answer = [1, 2, 3, 4, 5]
def hamming(n):
    if len(answer) > n:
        return answer[n-1]
    while len(answer) <= n:
        for i in range(answer[-1] + 1, 10000000):
            a = i
            while a % 2 == 0 or a % 3 == 0 or a % 5 == 0:
                if a % 2 == 0:
                    a = a // 2
                if a % 3 == 0:
                    a = a // 3
                if a % 5 == 0:
                    a = a // 5
            if a == 1:
                answer.append(i)
    return answer[n-1]
print(hamming(5000))
print(answer)