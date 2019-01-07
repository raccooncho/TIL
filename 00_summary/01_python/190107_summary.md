# 190107 summary_python



### 0. 아침 문제풀이

* 달력 만들기

```python
for i in range(1, 13):
    print(f'{i} 월\n 일 월 화 수 목 금 토 ')
    if i in [1, 3, 5, 7, 8, 10, 12]:  # list로 만들어서 안에 있는 값을 찾으니까 됨.
        n = 31
    elif i in [2]:    
        n = 28
    else:
        n = 30
    for d in range(1, n + 1):
        if d < 10:
            if d == 7:
                print(f' {d}  ')
            else:
                print(f' {d} ', end='')
        elif d == n:
            print(f'{d} \n')
        elif d % 7:
            print(f'{d} ', end='')
        else:
            print(f'{d}  ')
```

```python
months_end = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}

weeks = [' 일 ', ' 월 ', ' 화 ', ' 수 ', ' 목 ', ' 금 ', ' 토 ']
count_blank = ''
count = 0

for month, end_date in months_end.items():
    print(month, '월')
    print('|', end='')
    for yoil in weeks:
        print(yoil, end=' | ')
    print()
    print('------------------------------------------------')
    
    print(count_blank, end='')
    for day in range(1, end_date + 1):
        if day < 10:
            day = f' {day}'
        print(f'  {day} | ', end='')
        count += 1
        if day == end_date:
            print()
            if count >= 7:
                count = count - 7
            count_blank = '     | ' * count
        elif count == 7:
            print()
            count = 0
```





### 1. 재귀 함수 (recursive_function)

* 재귀함수는 함수 내부에서 자기 자신을 호출하는 함수이다.
* 예제1 : 팩토리얼 계산
  * 팩토리얼을 계산하는 함수 fact(n)을 작성해 봅시다.
  * n은 1보다 큰 정수라고 가정하고, 팩토리얼을 계산한 값을 반환합니다.

```python
def fact(n):
    f = 1
    for i in range(1, n+1):
        f = f * i
    return f
```

```python
def fact(n):  # 교수님 답안
    f = 1
    while n > 1:  # n이 1보다 크다는 조건을 입력하기 위해서 while문을 사용함.
        f = f * n
        n -= 1
    return f
```

* 예제2 : 재귀를 이용한 팩토리얼 계산

```python
def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)
```

* 재귀 함수는 기본적으로 같은 문제이지만 점점 범위가 줄어드는 문제를 푼다.
* 재귀 함수에는 반드시 base case가 존재한다.
* base case는 점점 범위가 줄어들어 반복되지 않는 최종장소로 도달하는 곳이다.



* * 재귀를 이용한 팩토리얼 계산에서의 base case는 n이 1일때, 함수가 아닌 정수 반환하는 것이다.

* 자기 자신을 호출하는 재귀함수는 알고리즘 구현 시 많이 사용된다.

* 코드가 더 직관적이고 이해하기 쉬운 경우가 있지만 만들기는 어렵다.

* 함수가 호출될 때마다 메모리 공간에 쌓인다. 

  * 그러면 메모리 스택이 넘치거나(stack overflow), 프로그램 실행속도가 느려지기 때문에 1000번이 넘어가면 더이상 함수를 호출하지 않고 종료된다.

* 예제3 : 피보나치 수열

  * 피보나치 수열은 다음과 같은 점화식이 있다.

  ```
  F0 = F1 = 1
  Fn = Fn-1 + Fn-2
  
  1) fib(n) : 재귀함수
  2) fib_loop(n) : 반복문을 활용한 함수
  ```

  ```python
  def fib(n):  # 재귀함수를 이용한 피보나치 수열  # 내답
      if n == 1 or n == 0: 
          return 1
      else:
          return fib(n-1) + fib(n-2)
  ```

  ```python
  def fib(n): # 교수님답
      if n in (0, 1):  # 짧게 정렬하는 습관...
          return 1
      elif n > 1:  # 음수는 배제하도록 합시다.
          return fib(n-1) + fib(n-2)
  ```

  ```python
  def fib_loop(n):  # 반복문을 이용한 피보나치 수열  # 내답
      result_1 = 0
      result_2 = 0
      for i in range(0, n + 1):
          if i == 1:
              result_2 = 1
              return result_2
          elif i == 0:
              result_1 = 1
              return result_1
          elif i % 2:
              result_1 = result_1 + result_2
              if i == n:
                  return result_1
          else:
              result_2 = result_1 + result_2
              if i == n:
                  return result_2
  ```

  ```python
  def fib_loop(n):  # 교수님답
      result = [1, 1]  # 리스트로 append시키면 훨씬 간단해짐!!!!
      for i in range(1, n):
          result.append(result[-1] + result[-2])
      return result[-1]
  ```

* 반복문과 재귀함수의 차이

```python
fib(33) # 5702887
# 연산 속도가 느림
```

```python
fib_loop(3300) # ㅁ ㅐ ㅇ ㅜ ㅋ ㅡ ㄴ ㅅ ㅜ
# 연산이 빠름
```

* 예제 4 : chicken coupon
  * ex) 치킨쿠폰 3장을 모으면 한마리를 줍니다. 한마리를 시키면 한장을 줍니다. n장이 있을 때, 몇 마리까지 먹을 수 있을 까요? ex) 10장: 7장 + 1장 => 5장 + 1장 =>....

```python
def chicken_coupon(n, base):
    c = n // base
    if n < base:
        return c
    else:
        c = c + chicken_coupon(c + n%base, base)  # 뒤의 base도 입력해줘야함.
        return c
```



* 예제 : 하노이의 탑
  * 한번에 한개의 층만을 다른 기둥으로 옮길 수 있다.
  * 옮기려는 기둥에는 아무것도 없거나 옮기려는 층보다 큰 층이 있을 경우에만 옮길 수 있다.
  * 옮기려는 기둥에 옮기려는 층보다 작은 층이 이미 있을 경우 그 기둥으로 옮길 수 없다.
  * 가능한 적은 횟수로 전체 탑을 다른 기둥으로 옮긴다.

```python

```

