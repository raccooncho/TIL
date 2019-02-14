# 알고리즘

( 배우는 과정에서 	문제를 풀 때 내장함수, 라이브러리를 사용하지 않고 해결하도록 노력한다. )

### APS 기본 - 자료구조 (자료 저장 및 처리)

### APS 응용 - 알고리즘 설계 (최적화(optimization problem) - 최대 혹은 최소가 되는 경우를 찾는다.)



#### intermediate -> 정확성

#### advanced -> 완전탐색



완전검색 -> DP, 백트래킹, 분할정복

시간복잡도 -> 실제 걸리는 시간을 측정

​		   -> 실행되는 명령문의 개수를 계산



버블 소트

for 문 두번 써서 큰수를 계속 뒤로 미룬다



카운팅 정렬

각 정수를 인덱스에 맞춰 넣고

카운트만큼 맞춰 넣는다..

```python
K = 4
arr = [0, 4, 1, 3, 1, 2, 4, 1]
cnt = [0] * (K + 1)
sorts = [0] * len(arr)

for val in arr:
    cnt[val] += 1
print(cnt)  # [1, 3, 1, 1, 2] -> 각 인덱스의 갯수

for i in range(1, K + 1):
    cnt[i] = cnt[i - 1] + cnt[i]
print(cnt)  # [1, 4, 5, 6, 8] -> 누적 카운팅...

for i in range(len(arr) - 1, -1, -1):
    cnt[arr[i]] -= 1
    sorts[cnt[arr[i]]] = arr[i]
print(sorts)  # [0, 1, 1, 1, 2, 3, 4, 4] -> 그렇게 sort한 리스트///
```





stdin -> keyboard

stdout -> console

stderr -> console