# 190107 summary_python



### 0. 아침 문제풀이 

* quiz 1 :  up & down

  * 우리가 'range(1, 101)' 중 하나를 생각한다. 컴퓨터가 절반에 위치한 숫자를 물어보고, 생각한 수보다 크면 1, 작으면 -1, 맞으면 0을 입력한다. 이때 몇번만에 컴퓨터가 맞췄는지 출력하고 프로그램을 끝낸다.
  * 예시)

  ```sh
  숫자를 생각하세요...
  50
  > -1
  25
  > -1
  13
  > -1
  7
  > 1
  10 
  > 1
  12
  > 0
  6번만에 맞췄습니다.
  ```

```python
import random  # 이건 컴퓨터가 문제내고 내가 맞추는 코드
def guess_up_down():
    user_feedback = input('숫자를 입력하세요:')
    number = random.sample(list(range(1, 101)), 1)[0]
    count = 0
    while number != int(user_feedback):
        if int(user_feedback) > number:
            print('>1')
            user_feedback = input(f'{user_feedback}보다 작은 숫자를 입력하세요:')
            count += 1
        elif int(user_feedback) < number:
            print('>-1')
            user_feedback = input(f'{user_feedback}보다 큰 숫자를 입력하세요:')
            count += 1
    count += 1
    print('>0')
    print(f'{count}번 만에 맞췄습니다! 축하합니다!')
    
```

```python
def guess_up_down(number):  # 이건 내가 문제내고 컴퓨터가 맞추는 코드
    num_list = list(range(1, 101))
    count = 0
    num = num_list.index(num_list[-1]) // 2
    numberc = num_list[num]
    while numberc != number:
        print('작으면 -1, 맞으면 0, 크면 1')
        num = num_list.index(num_list[-1]) // 2
        numberc = num_list[num]
        numind = []
        if numberc > number:
            print(f'{numberc} >> 1')
            count += 1
            for i in num_list:
                if i >= numberc:
                    numind.append(num_list.index(i))
        elif numberc < number:
            print(f'{numberc} >> -1')
            count += 1
            for i in num_list:
                if i <= numberc:
                    numind.append(num_list.index(i))
        removelist = []
        for i in numind:
            removelist.append(num_list[i])
        num_list = list(set(num_list) - set(removelist))
            
       
    count += 1
    print(f'{numberc} >> 0')
    print(f'{count}번 만에 맞췄습니다! 축하합니다!')
    
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