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
    print(' ', end='')
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
def chicken_coupon(n):  # 기본형
    c = n // 3
    if n < 3:
        return c
    else:
        c = c + chicken_coupon(c + n%3)
        return c
```

```python
def chicken_coupon(n, base=3):  # n은 쿠폰의 갯수 # base는 치킨 한마리를 살때 필요한 쿠폰의 갯수
    c = n // base  # c는 쿠폰으로 산 치킨의 갯수
    if n < base:
        return c
    else:
        c = c + chicken_coupon(c + n%base)  # 뒤의 base도 입력해줘야함.
        return c  # c + n%base는 처음 쿠폰으로 치킨을 사고 남은 쿠폰의 갯수 (n%base)와 새로 치킨을 사면서 생긴 쿠폰의 갯수(n)합으로서 현재 가지고있는 총 쿠폰의 갯수를 의미함.
```

* 예제 5 : 개미수열(Look and Say)

  * 숫자를 세어서 몇개인지 말해요

  ```
  n = 1
  [1]
  n = 2
  [1, 1]
  n = 3
  [1, 2]
  n = 4
  [1, 1, 2, 1]
  .
  .
  .
  ```

```python
def look_say(n):  # 극 고통;;  # 내 풀이
    count = 1
    if n == 1:
        return [1]
    elif n >= 2:
        result = [1]
        loook = look_say(n-1)
        while len(loook) >= 2:
            if loook[0] == loook[1]:
                count += 1
            elif loook[0] != loook[1]:
                result.append(count)
                result.append(loook[1])
                count = 1
            loook.remove(loook[0])
        if result[-1] == loook[0]:
            result.append(count)
        else:
            result.append(count)
            count = 1
            result.append(loook[0])
            result.append(count)
        loook.remove(loook[0])
        return result
```

```python
def look_say(n):  # 고재두님답
    if n == 0:
        return [1]
    else:
        result = []
        my_list = look_say(n-1)
        temp = my_list[0]
        count = 0
        for i in my_list:
            if i == temp:
                count += 1
            else:
                result.append(temp)
                result.append(count)
                count = 1
            temp = i
        else:
            result.append(temp)
            result.append(count)
        return result
```

```python
def look_say(n, remain=[1], result=[]):  # 교수님답.
    if n == 0:
        return remain
    look = remain[0]
    say = 0
    for index, number in enumerate(remain):
        if number == look: # 보던 애가 계속 나오면
            say += 1
        else: # 못 보던 애가 나오면
            del(remain[0:index])
            break
    else:        # start앞을 버린다.
        remain = []
    result = result + [look, say]
        # result뒤에 look과 say를 붙인다.
    if not remain:
        return look_say(n-1, result, [])
        # remain이 비어있다면
        # return look_say(n-1, ,)
    else:
        return look_say(n, remain, result)
        #remain이 남아 있다면
        #return look_say(n, ,)
        
        
           
```

```python
def look_say(n):  # 강진우님 답  # 이건 진심 하나도 모르겠음ㅁㅁㅁㅁ
    if n == 0:
        return [1]
    else:
        list_1 = look_say(n-1)
        list_2 = []
        number = 0
        num_cnt = 0
        i = 0
        while i < len(list_1):
            if number != list_1[i]:
                if i != 0:
                    list_2.append(num_cnt)
                list_2.append(list_1[i])
                number = list_1[i]
                num_cnt = 1
            else:
                num_cnt += 1
            i += 1
        list_2.append(num_cnt)
        return list_2
```



* 예제 : 하노이의 탑
  * 한번에 한개의 층만을 다른 기둥으로 옮길 수 있다.
  * 옮기려는 기둥에는 아무것도 없거나 옮기려는 층보다 큰 층이 있을 경우에만 옮길 수 있다.
  * 옮기려는 기둥에 옮기려는 층보다 작은 층이 이미 있을 경우 그 기둥으로 옮길 수 없다.
  * 가능한 적은 횟수로 전체 탑을 다른 기둥으로 옮긴다.

```python
# 이건 나중에 풀어 봅 시 다ㅏㅏㅏㅏㅏㅏ
```



### 2. 문자열 메소드 활용하기

##### 변형

* .capitalize(), .title(), .upper()
  * .capitalize() : 앞글자를 대문자로 만들어 반환한다.
  * .title() : 어퍼스트로피나 공백 이후를 대문자로 만들어 반환한다.
  * .upper() : 모두 대문자로 만들어 반환한다.

```python
greeting = 'hI! EveryOne, I\'m ssafy'
print(greeting)  # hI! EveryOne, I'm ssafy
print(greeting.capitalize())  # Hi! everyone, i'm ssafy  -> 첫글자 제외 전부 소문자됨
print(greeting.title())  # Hi! Everyone, I'M Ssafy  -> 공백이나 ' 뒤의 문자 전부 대문자되고 나머진 모두 소문자됨
print(greeting.upper())  # HI! EVERYONE, I'M SSAFY  -> 모두 대문자 됨
```



* .lower(), .swapcase()
  * .lower() : 모두 소문자로 만들어 반환한다.
  * .swapcase() : 대 <-> 소문자로 변경하여 반환한다.

```python
print(greeting.lower())  # hi! everyone, i'm ssafy  -> 전부 소문자 됨
print(greeting.swapcase())  # Hi! eVERYoNE, i'M SSAFY  -> 소문자와 대문자가 서로 바뀜
```



* .join(iterable)
  * 특정한 문자열로 만들어 반환한다.

```python
'!'.join('아파요')  # 아!파!요  -> 글자 사이사이에 끼어들음
feelings = ['아파요', '어려워요', '힘들어요', '죽겠다']
print('으악!'.join(feelings))  # 아파요으악!어려워요으악!힘들어요으악!죽겠다  -> 리스트에선 요소 사이사이에 끼어들음
```



* replace(old, new[, count])
  * 바꿀 대상 글자를 새로운 글자로 바꿔서 반환한다.
  * count를 지정하면 해당 갯수만큼만 시행한다.

```python
print('갑분싸'.replace('싸', 'ssa'))  # 갑분ssa
print('aa너무 즐거워요aa'.replace('a', 'ㅠ'))  # ㅠㅠ너무 즐거워요ㅠㅠ
```



* 글씨 제거 (strip([chars]))
  * 특정한 문자들을 지정하면, 양쪽을 제거하거나 왼쪽을 제거하거나 (lstrip) 오른쪽을 제거한다.(rstrip)
  * 지정하지 않으면 공백을 제거한다.

```python
print('           recursive!\n'.strip())  # recursive!  -> 설정하지 않으면 공백이 제거됨
print('           recursive!\n\t'.lstrip())  # recursive!  -> 왼쪽의 공백만 제거됨
```



##### 탐색 및 검증

* .find(x) 
  * x의 첫 번째 위치를 반환한다. 없으면, -1을 반환한다.

```python
'apple'.find('p')  # 1  -> p의 위치를 찾아서 알려준다.
'apple'.find('f')  # -1  -> f가 없어서 -1로 알려준다.
```



* .index(x)
  * x의 첫 번째 위치를 반환한다. 없으면 오류가 뜬다.

```python
'apple'.index('p')  # 1 -> p의 위치를 찾아서 알려준다.
'apple'.index('f')  # 에러 -> 없으면 에러가 나온다.
```



* 다양한 확인 메소드 : True / False 반환
  * .isaplha(), .isdecimal(), .isdigit(), .isnumeric(), .isspace(), .issuper(), .istitle(), .islower()



##### split()

* 문자열을 특정한 단위로 나누어 리스트로 반환한다.

```python
'a_b_c'.split('_')  # ['a', 'b', 'c']  -> _을 기준으로 문자를 자른다.
```





## 3. 리스트 메소드 활용하기

##### 값 추가 및 삭제

* .append(x)
  * 리스트에 값을 추가할 수 있다.
* .extend(iterable)
  * 리스트에 iterable(list, range, tuple, string) 값을 붙일 수가 있다.
* insert(i, x)
  * 정해진 위치 i에 값을 추가한다.
* remove(x)
  * 리스트에서 값이 x인것을 삭제한다.
* .pop(i)
  * 정해진 위치 i에 있는 값을 삭제하고 그 항목을 반환한다.
  * i가 지정되지 않으면 마지막 항목을 삭제하고 반환한다.

##### 탐색 및 정렬

* .index(x)
  * 원하는 값을 찾아 index값을 반환한다.
* .count(x)
  * 원하는 값의 갯수를 확인할 수 있다.
*  .sort()
  * 정렬한다.
  * sorted()와 다르게 원본 list를 변형시키고 None을 리턴한다.
* .reverse()
  * 반대로 뒤집는다. (정렬아님)

##### 복사

```python

```

```python

```

```python

```

```python

```

```python

```

* 파이썬에서 모든 변수는 객체의 주소를 가지고 있을 뿐이다.

  num = [1, 2, 3]

  * 위와 같이 변수를 생성하면 num이라는 객체를 생성하고, 변수에는 객체의 주소가 저장된다.
  * 변경가능한 (mutable) 자료형과 변경불가능한 (immutable) 자료형은 서로 다르게 동작한다.

* 복사를 하고 싶을 때에는 다음과 같이 해야 한다.

``` python

```

```python

```



```python

```



```python

```



##### 삭제 clear()

* 리스트의 모든 항목을 삭제한다.

```python

```

