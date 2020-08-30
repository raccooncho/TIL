# a = [2,1,4,5,6,7,8,2,3,5,6,11, 3, 2, 4, 5, 1, 77, 1, 5, 2, 3, 4, 6, 1]
# b = [i for i in a]
# for i in list(range(1, len(a))):
#     key = a[i]
#     j = i - 1
#     while j >= 0 and a[j] > key :
#         a[j+1] = a[j]
#         j = j - 1
#     a[j + 1] = key
# print(list(range(2, len(a))))
# print(len(a))
# print(a)
# for i in list(range(1, len(b))):
#     key = b[i]
#     j = i + 1
#     while j > 0 and b[j] < key:
#         b[j + 1] = b[j]
#         j = j - 1
#     b[j + 1] = key
# print(b)
# # 연습문제 2.1-1 : 그림 2.2를 모델로 이용해 수열 A = <31, 41, 59, 26, 41, 58>이 입력으로 주어질 때 Insertion-sort의 동작을 설명하라
#
# # 연습문제 2.1-2 : 수열을 오름차순 대신 내림차순으로 정렬하도록 Insertion-sort 프로시저를 재작성하라
#
def restoreString(s: str, indices: list):
    d = {}

    def sortt(a):
        for i in list(range(1, len(a))):
            key = a[i]
            j = i - 1
            while j >= 0 and a[j] > key:
                a[j + 1] = a[j]
                j = j - 1
            a[j + 1] = key
        return a

    ind = sortt(indices)
    for i in list(range(len(indices))):
        d[indices[i]] = s[i]
    ans = ""
    for i in ind:
        ans += d[i]
    print(ans)
    return ans

restoreString("codeleet",[4,5,6,7,0,2,1,3])