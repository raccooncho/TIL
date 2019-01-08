# 190107 summary_python



### 0. 아침 문제풀이 & setting changes

* jupyter notebook명령어 내가 원하는거로 바꾸기

  * 우선 cd로 홈가기

  * less .bash_history 를 들어가면 명령어 목록 보기 가능(q로 나옴)

  * touch .bashrc 폴더 만들기

  * (vim .bashrc로 수정하는곳 들어가기

  * i 누른 후 alias 'jn'='jupyter notebook'입력

  * :w로 저장 후 :q로 나오기)

    or

  * (echo 'alias "jn"="jupyter notebook"' >> .bashrc) 

  * --> 수정할 때는 >>를 >로 쓰면 됨(덮어쓰기)

  * cat .bashrc로 제대로 입력됬나 확인하기

  * bash를 껐다 키거나 bash를 입력해서 자동으로 재부팅시킨 후 사용하면 됨

* quiz 1. 이상한 덧셈

  * 숫자로 구성된 리스트에서 양의 정수의 합을 구하는 함수, 'positive_sum'을 만들어 보세요.
  * 예시)

  ```python
  positive_sum([1, -10, 2]) #3
  positive_sum([-1, -2, -3, -4]) #0
  ```

```python
def positive_sum(lists):  # 내 답
    pos_list = []
    for num in lists:
        if num > 0:
            pos_list.append(num)
    return sum(pos_list)
```

```python
def positive_sum(numbers):  # 교수님 답
    total = 0
    for number in numbers:
        if number > 0:
            total += number
    return total
```

```python
def pos_sum(numbers):  # 교수님의 고오급 답
    return sum(x for x in numbers if x > 0)  
```



* quiz 2. 문자열 탐색

  * 문자열 요소로만 이루어진 리스트를 넣었을 때, 문자열의 길이가 2 이상이고 주어진 문자열의 첫 번째와 마지막 문자가 같은 문자열의 수를 세는 함수 'start_end' 를 작성하세요
  * 예시)

  ```python
  start_end(['level', 'asdwe', 's', 'abadsfa', 'q1q']) # 3
  ```

```python
def start_end(lists):  # 내 답 == 교수님 답 # 성공적
    count = 0
    for words in lists:
        if len(words) > 1 and words[0] == words[-1]:
            count += 1
    return count
```

* quiz 3. Collatz

  * Collatz 추측: 어떤 자연수 n 이던지, 다음과 같은 작업을 반복하면 1로 만들수 있다.
    1. n이 짝수라면 2로 나눈다.
    2. n이 홀수라면 3을 곱하고 1을 더한다.
    3. 결과로 나온 수에 1/2의 작업을 1이 될때까지 반복한다. 예를 들어 n이 6이면, 6 => 3 => 10 => 5 => 16 => 8 => 4 => 2 => 1이 되며 8번(=>갯수!)만에 1이 됩니다. 자연수 n이 들어왔을 때, 몇 번의 작업만에 1이 되는 지를 'return'하는 함수 'collatz()'를 완성하세요. 단! 500번을 넘어가도 1이 되지 않는다면, -1을 'return'하세요!
  * 예시)

  ```python
  collatz(6) # 8
  collatz(16) # 4
  collatz(6263313) # -1
  ```

```python
def collatz(n):  # 내 답
    count = 0
    while int(n) >= 2 and count <=500:
        if int(n) % 2:
            n = n * 3 + 1
            count += 1
        else:
            n = n / 2
            count += 1
    if int(n) == 1:
        return count
    else:
        return -1
```

```python
def collatz(num):  # 교수님 답
    for i in range(500):
        if num % 2:
            num = num * 3 + 1
        else:
            num = num / 2
        if num == 1:
            return i + 1
    return -1
```



* quiz 4.  솔로 천국

  * 리스트가 주어질 때, 리스트의 요소 'e'는 'range(0, 10)'에 포함되는 자연수이다. 리스트에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거하여 'return'하는 함수 'lonely()'를 작성해 보세요. 이때! 제거된 후 남은 수들을 반환할 때는 리스트의 요소들이 순서를 유지해야 합니다!
  * 예시)

  ```python
  lonely([1, 1, 3, 3, 0, 1, 1, 3, 0, 3]) # [1, 3, 0]
  lonely([4, 4, 3, 3, 3, 4]) # [4, 3]
  ```

```python
def lonely(lists):
    tlist = []
    for i in lists:
        if i not in tlist:
            tlist.append(i)
    return tlist
```

* quiz 5. (hard) RGB 삼각형

  | BG   | RG   | BR   | RR   | GG   | BB   |
  | ---- | ---- | ---- | ---- | ---- | ---- |
  | R    | B    | G    | R    | G    | B    |
  > 입력으로  ''R', 'G', 'B''가 섞여있는 문자열이 들어온다. 문자열은 다음과 같이 합쳐진다. 해당 문자열을 처리하여 마지막 색깔만 'return'하는 'triange()'을 작성하세요.

  * 예시)

  ```python
  triangle('RRGBRGBB') # G
  triangle('GB') # R
  triangle('B') # B
  triangle('RGBG') # B
  ```

```python
def triange(RGB):  # 고재두님 답 참고한 내 답
    RGB = ' '.join(RGB).split()
    tri = RGB
    sample = { 'R', 'G', 'B' }
    while len(RGB) != 1:
        tri = []
        for i in range(len(RGB) - 1):
            if RGB[i] == RGB[i + 1]:
                tri.append(RGB[i])
            else:
                color = sample - { RGB[i], RGB[i + 1] }
                tri = tri + list(color)
        RGB = tri
    return tri
```

```python
def triange(RGB):  # 삼각형 그리기 ( no return )
    RGB = ' '.join(RGB).split()
    tri = RGB
    sample = { 'R', 'G', 'B' }
    count = 0
    while len(RGB) != 1:
        tri = []
        for i in range(len(RGB) - 1):
            if RGB[i] == RGB[i + 1]:
                tri.append(RGB[i])
            else:
                color = sample - { RGB[i], RGB[i + 1] }
                tri = tri + list(color)
        count += 1
        blankc = (count) * ' '
        print(blankc + ' '.join(tri))
        RGB = tri
```

* quiz 6 . (??) 홀수개를 찾아라

  > 입력으로 list가 한개 들어옵니다. 이 list에는 1개의 숫자만 홀수 개 들어있습니다.
  >
  > 이 1개의 홀수개인 숫자를 return 하는 find_odd()를 작성하세요.

  * 예시)

  ```python
  find_odd([1, 1, 2, 2, 3, 3, 3]) # 3
  find_odd([2, 1, 2]) # 1
  find_odd([1, 2, 2, 3, 2, 2, 1]) # 3
  ```

```python
def find_odd(numbers):  # 내답안
    odd_number = set()
    for i in numbers:
        if numbers.count(i) % 2:
            odd_number.add(i)
    return list(odd_number)
```

```python
def find_odd(numbers):  # 오.....한 답안 
    for uniq in list(set(numbers)):
        if numbers.count(uniq) % 2:
            return uniq
```

```python
from operator import xor  # 교수님의 import 한 답안. 은 reduce도 import해야하는데 어디서 해야하는지 몰라서 fail

def find_odd(numbers):
    return reduce(xor, numbers)

def find_odd_2(numbers):  # 이렇게 하면 import안해도 됨.
    result = 0
    for n in numbers:
        result = result ^ n
    return result

```



### 1. 리스트 메소드 활용하기

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

* 이렇게 하는 것도 일부 상황에서만 서로 다른 얕은 복사(shallow copy)이다.

```python

```

* 만일 중첩된 상황에서 복사를 하고 싶다면, 깊은 복사(deep copy)를 해야 한다.
* 내부에 있는 모든 객체까지 새롭게 값이 변경된다.

```python

```



##### 삭제 clear()

* 리스트의 모든 항목을 삭제한다.

```python

```



### 2. List Comprehension

* List를 만들 수 있는 간단한 방법이 있습니다.



##### 사전 준비

> 다음의 리스트를 만들어보세요.

1. 1~10까지의 숫자 중 짝수만 담긴 리스트 `even_list`
2. 1~10까지의 숫자로 만든 세제곱 담긴 리스트 `cubic_list`



##### 활용법

여러개의 `for` 혹은 `if`문을 중첩적으로 사용 가능합니다.



#### 연습 문제

##### 짝짓기 - 곱집합

> 주어진 두 list의 가능한 모든 조합을 담은 `pair` 리스트를 만들어주세요.

1. 반복문 활용
2. list comprehension 활용

------

```
girls = ['jane', 'iu', 'mary']
boys = ['justin', 'david', 'kim']

예시 출력)

[('justin', 'jane'), ('justin', 'iu'), ('justin', 'mary'), ('david', 'jane'), ('david', 'iu'), ('david', 'mary'), ('kim', 'jane'), ('kim', 'iu'), ('kim', 'mary')]
```



##### 피타고라스 정리

> 주어진 조건(x < y < z < 50) 내에서 피타고라스 방정식의 해를 찾아보세요.

1. 반복문 활용
2. list comprehension 활용

```
예시 출력)
[(3, 4, 5), (5, 12, 13), (6, 8, 10), (7, 24, 25), (8, 15, 17), (9, 12, 15), (9, 40, 41), (10, 24, 26), (12, 16, 20), (12, 35, 37), (15, 20, 25), (15, 36, 39), (16, 30, 34), (18, 24, 30), (20, 21, 29), (21, 28, 35), (24, 32, 40), (27, 36, 45)]
```



##### 모음 제거하기

> 다음의 문장에서 모음(a, e, i, o, u)를 모두 제거하시오.

1. list comprehension만 사용해보세요.

```
    words = 'Life is too short, you need python!'

    예시출력)
    Lf s t shrt, y nd pythn!
```



#### 딕셔너리 메소드 활용



##### 추가 및 삭제

* .pop(key[, default])
  * key가 딕셔너리에 있으면 제거하고 그 값을 돌려준다. 그렇지 않으면 default를 반환한다.
  * default가 없는 상태에서 딕셔너리에 없으면 KeyError가 발생한다.



* .update()
  * 값을 제공하는 key, value로 덮어쓴다.



* .get(key[, default])
  * key를 통해 value를 가져온다.
  * 절대로 KeyError가 발생하지 않는다. default는 기본적으로 None이다



#### dictionary comprehension

* dictionary도 comprehension을 활용하여 만들 수 있다.
  * 추후에 zip, map 등을 배우고 다시 다루도록 하겠습니다 :)