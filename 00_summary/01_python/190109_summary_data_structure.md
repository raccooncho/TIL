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

```python
def guess_up_down(max_n=100, min_n=0):  # 교수님 답 # 이렇게 풀으라는 거였구나..;;
    count = 0
    max_n = max_n + 1
    print('숫자를 생각하세요.!')
    
    while 1:
        guess = (max_n + min_n) // 2
        print(guess)
        count += 1
        feedback = int(input('작으면 -1, 크면 1, 맞으면 0: '))
        
        if feedback == -1:
            max_n = guess
        if feedback == 1:
            min_n = guess
        else:
            return count

guess_up_down()
```



##### work shop 문제

* 이분법
  * 양의 정수 x 를 입력받아 제곱근의 근사값의 결과를 반환하는 함수를 작성하세요.
    * sqrt() 사용 금지

```python
def root(sample_num, c=6):
    count = 0
    sample_num = sample_num * 10
    down_num = sample_num -1
    if count == 1:
        while True:
            if down_num ** 2 > (10**count) * sample_num:
                down_num = down_num -1
            elif down_num ** 2 < (10 **count) * sample_num:
                down_num = down_num + 1
                count += 1
                break
            else:
                sample_num = down_num
                count += 1
                return sample_num / (10 ** count)        
    while count != c:
        sample_num = 10 * sample_num
        down_num = 10 * down_num -1
        while True:
            if down_num ** 2 > (10**count) * sample_num:
                down_num = down_num -1
            elif down_num ** 2 < (10 **count) * sample_num:
                down_num = down_num + 1
                count += 1
                break
            else:
                sample_num = down_num
                count += 1
                return sample_num / (10 ** count)
    sample_num = down_num
    return sample_num / (10 ** count)
```

```python
def root(sample_num, c=6):  # 재귀 함수를 적용 한...건가 ㅋㅋㅋㅋ
    count = 1
    min_n = sample_num - 0.1
    while count != (c+1):
        if min_n ** 2 > sample_num:
            min_n = min_n - 0.1 ** (count)
        elif min_n ** 2 < sample_num:
            min_n = min_n + 0.1 ** (count)
            count += 1
        else:
            return min_n
    return round(min_n, c)
```





### 1. 리스트 메소드 활용하기

##### 값 추가 및 삭제

* `.append(x)`
  * 리스트에 값을 추가할 수 있다.

```python
caffes = ['starbucks', 'tom&toms', 'coffebean', 'hollys']
caffes.append('ediya')  # no return
# ['starbucks', 'tom&toms', 'coffebean', 'hollys', 'ediya']
```

* `.extend(iterable)`
  * 리스트에 iterable(list, range, tuple, string)(->돌릴 수 있는..) 값을 붙일 수가 있다.

```python
caffes.extend(['droptop', '빽다방'])
# ['starbucks', 'tom&toms', 'coffebean', 'hollys', 'ediya', 'droptop', '빽다방']
== caffes += ['droptop', '빽다방']
```

```python
caffes.append('the venti') == caffes.append(['the venti'])
```

​	* extend에 스트링을 넣으면 알파벳이 다 쪼개짐...

* `.insert(i, x)`
  * 정해진 위치 i에 값을 추가한다.
  * index가 넘어가면 마지막에 붙는다.

```python
fast_foods = ['McDonald', 'Burger King', 'KFC']
fast_foods.insert(0, 'Moms touch')
fast_foods.insert(3, 'Lotteria')
# ['Moms touch', 'McDonald', 'Burger King', 'Lotteria', 'KFC']
```

* `.remove(x)`
  * 리스트에서 값이 x인것을 삭제한다.

```python
numbers = [1, 2, 3, 1, 2]
numbers.remove(1)
# [2, 3, 1, 2]  -> 하나씩만 지워짐 ( 앞에 있는 순서대로 지워지는 듯)
```

* `.pop(i)`
  * 정해진 위치 i에 있는 값을 삭제하고 그 항목을 반환한다.
  * i가 지정되지 않으면 마지막 항목을 삭제하고 반환한다.
  * i 는 index를 의미함.

```python
a = [1, 2, 3, 4, 5]
a.pop(0)
# [2, 3, 4, 5]
last = a.pop()
print(a, last)
# [2, 3, 4] 5  # i를 지정하지 않으면 마지막 index가 삭제되고 삭제된 값은 return된다.
```



##### 탐색 및 정렬

* `.index(x)`
  * 원하는 값을 찾아 index값을 반환한다.

```python
b = [1, 2, 3, 4, 5]
b.index(4) # 3 -> 4의 index 3을 return 한다. 없는 값을 요청하면 Error
```

* `.count(x)`
  * 원하는 값의 갯수를 확인할 수 있다.

```python
alph = ['a', 'b', 'c', 'c', 'b', 'd', 'b']
alph.count('b')  # 3
```

* `.sort()`
    * 정렬한다.
    * sorted()와 다르게 원본 list를 변형시키고 None을 리턴한다.

```python
my_list = [4, 3, 2, 1]
sorted_list = sorted(my_list)
print(my_list, sorted_list)
# [4, 3, 2, 1] [1, 2, 3, 4]  # 원본 남겨놓고 정렬된 새로운 리스트가 생성됨
```

```python
my_list = [4, 3, 2, 1]
sorted_list = my_list.sort()
print(my_list, sorted_list)
# [1, 2, 3, 4] None  # 원본을 변경하고 return 값은 없다.
```



* `.reverse()`
  * 반대로 뒤집는다. (정렬아님)

```python
class_mates = ['이원진', '지상현', '조성규']
r_class_mates = class_mates.reverse()
print(class_mates, r_class_mates)
#['조성규', '지상현', '이원진'] None  # 원본을 변경하고 return 값은 없다.
```



##### 복사

```python
# 리스트 복사를 해봅시다.
origin = ['A']
copy = origin
print(origin, copy)  # ['A'] ['A']
```

```python
# b의 값을 바꾸고 a를 출력해봅시다.
origin.append('B')
print(origin, copy)  # ['A', 'B'] ['A', 'B']
```

```python
# 실제로 같은지 확인해봅시다.
print(origin == copy)
print(id(origin) == id(copy))  # True True  
# 복사가 복사가 이니게 되버림 ㅜㅠㅜㅠㅜㅜㅜㅠㅜ
```

```python
# 숫자를 확인해봅시다.
c = 1
o = c
c += 1
print(c, o)  # 숫자는 값이 할당되는 거라 제대로 복사됨;
```

```python
# 딕셔너리도 확인해봅시다.
lunch = { '김밥천국': '치즈김밥', '김가네': '빠에야새우볶음밥' }
dinner = lunch
dinner['김가네'] = '참치김밥'
print(lunch, dinner)
# {'김밥천국': '치즈김밥', '김가네': '참치김밥'} {'김밥천국': '치즈김밥', '김가네': '참치김밥'}
# 딕셔너리도 같이 바껴버림;;
```

* 파이썬에서 모든 변수는 객체의 주소를 가지고 있을 뿐이다.

  num = [1, 2, 3]

  * 위와 같이 변수를 생성하면 num이라는 객체를 생성하고, 변수에는 객체의 주소가 저장된다.
  * 변경가능한 (mutable) 자료형과 변경불가능한 (immutable) 자료형은 서로 다르게 동작한다.

* 복사를 하고 싶을 때에는 다음과 같이 해야 한다.

``` python
# 복사 예시
a = [1, 2, 3]
b = a[:]  # list의 모든 값을 slicing
a[0] = 5
print(a, b)
# [5, 2, 3] [1, 2, 3]
```

```python
# 복사 예시2
a = [1, 2, 3]
b = list(a)  # list를 list함
a[0] = 5
print(a, b)
# [5, 2, 3] [1, 2, 3]
```

* 이렇게 하는 것도 일부 상황에서만 서로 다른 얕은 복사(shallow copy)이다.

```python
ss3 = {
    'teacher': 'neo',
    'gamtoo': {
        'leader': 'Hwang',
        'CA': 'Kang'
    }
}

new_ss3 = dict(ss3)
ss3['gamtoo']['CA'] = 'KangJW'
print(ss3, new_ss3)
# {'teacher': 'neo', 'gamtoo': {'leader': 'Hwang', 'CA': 'KangJW'}}
# {'teacher': 'neo', 'gamtoo': {'leader': 'Hwang', 'CA': 'KangJW'}}
# 리스트, 딕셔너리, 튜플, 셋 안에 리스트, 딕셔너리, 튜플, 셋 이 있다면 값이 같이 바뀜....(복사가 복사가 아니게 됨;;)
```

* 만일 중첩된 상황에서 복사를 하고 싶다면, 깊은 복사(deep copy)를 해야 한다.
* 내부에 있는 모든 객체까지 새롭게 값이 변경된다.

```python
# 깊은 복사 예시
import copy  # copy를 import해와서
ss3 = {
    'teacher': 'neo',
    'gamtoo': {
        'leader': 'Hwang',
        'CA': 'Kang'
    }
}
new_ss3 = copy.deepcopy(ss3)  # deepcopy를 이용해야 한다.
ss3['gamtoo']['CA'] = 'KangJW'
print(ss3, new_ss3)
# {'teacher': 'neo', 'gamtoo': {'leader': 'Hwang', 'CA': 'KangJW'}}
# {'teacher': 'neo', 'gamtoo': {'leader': 'Hwang', 'CA': 'Kang'}}
```



##### 삭제 clear()

* 리스트의 모든 항목을 삭제한다.

```python
numbers = list(range(1, 10))
print(numbers)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]  
numbers.clear()
print(numbers)  # []
```



### List Comprehension

* List를 만들 수 있는 간단한 방법이 있습니다.

##### 사전 준비

> 다음의 리스트를 만들어보세요.

1. 1~10까지의 숫자 중 짝수만 담긴 리스트 `even_list`
2. 1~10까지의 숫자로 만든 세제곱 담긴 리스트 `cubic_list`

```python
even_list = [x * 2 for x in range(1, 6)]
# [2, 4, 6, 8, 10]
```

```python
cubic_list = [x ** 3 for x in range(1, 11)]
# [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
```



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

```python
girls = ['jane', 'iu', 'mary']
boys = ['justin', 'david', 'kim']
my_way = []
for g in girls:
    for b in boys:
        my_way.append((g, b))  # 기존에 쓰던 방법
```

```python
girls = ['jane', 'iu', 'mary']
boys = ['justin', 'david', 'kim']
easy_way = [(b, g) for b in boys for g in girls]  # 편한 방법
```



##### 피타고라스 정리

> 주어진 조건(x < y < z < 50) 내에서 피타고라스 방정식의 해를 찾아보세요.

1. 반복문 활용
2. list comprehension 활용

```
예시 출력)
[(3, 4, 5), (5, 12, 13), (6, 8, 10), (7, 24, 25), (8, 15, 17), (9, 12, 15), (9, 40, 41), (10, 24, 26), (12, 16, 20), (12, 35, 37), (15, 20, 25), (15, 36, 39), (16, 30, 34), (18, 24, 30), (20, 21, 29), (21, 28, 35), (24, 32, 40), (27, 36, 45)]
```

```python
ptagoras = [(x, y, z) for x in range(1, 48) for y in range(x+1, 49) for z in range(y+1, 50) if x**2+y**2==z**2]
```



##### 모음 제거하기

> 다음의 문장에서 모음(a, e, i, o, u)를 모두 제거하시오.

1. list comprehension만 사용해보세요.

```
    words = 'Life is too short, you need python!'

    예시출력)
    Lf s t shrt, y nd pythn!
```

```python
words = 'Life is too short, you need python!'
result = ''.join([w for w in words if w not in 'aeiouAEOIU'])
```



### 2. 딕셔너리 메소드 활용



##### 추가 및 삭제

* `.pop(key[, default])`
  * key가 딕셔너리에 있으면 제거하고 그 값을 돌려준다. 그렇지 않으면 default를 반환한다.
  * default가 없는 상태에서 딕셔너리에 없으면 KeyError가 발생한다.

```python
fruits = { 'apple': '사과', 'banana': '바나나'}
apple = fruits.pop('apple')
print(apple, fruits)
```

```python
fruits.pop('melon')  # 없는 것을 요구하면 Key Error
fruits.pop('melon', '없어요')  # '없어요' # default값에 값을 입력하면 입력한 값을 출력함
```



* `.update()`
  * 값을 제공하는 key, value로 덮어쓴다.

```python
fruits = { 'apple': '사과', 'banana': '바나나', 'melon': '멜론' }
fruits.update(banana='버네너')
# {'apple': '사과', 'banana': '버네너', 'melon': '멜론'}
```



* `.get(key[, default])`
  * key를 통해 value를 가져온다.
  * 절대로 KeyError가 발생하지 않는다. default는 기본적으로 None이다

```python
fruits.get('pineapple') # 없는 키를 넣으면 None
fruits.get('apple')  # 사과
fruits.get('strawberry', False)  # False
```





#### dictionary comprehension

* dictionary도 comprehension을 활용하여 만들 수 있다.

```python
cubic_dict = {x: x ** 3 for x in range(1, 10)}
# {1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729}
```

```python
# 아래에서 미세먼지 농도가 80 초과인 지역만 뽑자!
dusts = { 'seoul': 103, 'kyungki': 79, 'dajeon': 36, 'beijing': 500 }
bad_dusts = { key: value for key, value in dusts.items() if value > 80 }
# {'seoul': 103, 'beijing': 500}
how_bad = { key: 'bad' if value > 80 else 'not bad' for key, value in dusts.items()}
# {'seoul': 'bad', 'kyungki': 'not bad', 'dajeon': 'not bad', 'beijing': 'bad'}
```



### 3. Set 메서드 활용

#### 추가 및 삭제

* `.add(element)`
  * element를 추가한다.

```python
a = {1, 2, 3, 4}
a.add(5)
a.add(5)
a  # {1, 2, 3, 4, 5} -> set 는 중복값이 없음.
```

* `.update(*others)`
  * 여러가지(others)값을 순차적으로 추가한다.
    반드시 iterable한 값을 넣어야 한다.

```python
a = { 1, 2, 3 }
a.update({5, 5, 5, 2}, {7, 9, 10, 7})
a  # {1, 2, 3, 5, 7, 9, 10}
```

* `.remove(element)`
  * element를 set에서 삭제하고, 없으면 Error을 발생시킨다.

```python
a.remove(11)  # 11이 없어서 Error
a.remove(3)
a  # {1, 2, 5, 7, 9, 10}
```

* `.discard(element)`
  * `element`를 삭제하나, 에러가 발생하지 않는다.

```python
b = {1, 2, 3}
b.discard(5)
print(b) # {1, 2, 3} -> Error가 없다.
```

* `.pop()`
  * 임의의 원소를 제거하고 반환한다.

```python
c = {1, 2, 3, 4, 5}
r = c.pop
print(r)  # 순서 없이 그냥 작은거부터 제거하고 반환함;; 솔직히 알 수 없음....
```





###  * 정리!! `map()`, `zip()`, `filter()`

*  `.map(function, iterable)`
  * iterable 의 원소들에 function을 적용한 후, 그 결과를 돌려준다.	
  * iterable
    * list
    * dict
    * set
    * str
    * tuple
    * range
    * bytes
  * `.map()`의 return은 map object 형태로 나온다.

```python
l = ['1', '2', '3']
result = map(int, l)  # <map at 0x202cc644898> -> map object형태로 나온다.
list(result)  # [1, 2, 3]
```

 * 보통 문제풀이 사이트에서 입력같은 다음과 같은 방법으로 입력한다.

```python
l = input('띄어쓰기로 숫자 입력: ')
strings = l.split() # 띄어쓰기로 구분한 list
map_object = map(int, strings) # list요소들을 int() 적용시킨 요상한 object
r = list(map_object) # 원하는 list
print(r)
```

* 이렇게 다른언어(ex. html)에 data를 전달하는 용도로 자주 사용 된다.

```python
data = [10, 20, 30, 40]

def make_list_html(n):
    return f'<li class="container list">{n}</li>'

html_data = list(map(make_list_html, data))
print(html_data)
```

