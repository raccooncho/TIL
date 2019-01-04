# 190104 summary_python



### 0. 아침 문제풀이

* 아래 코드의 출력 결과를 예상해 보세요.

```python
if True:
    if False:
        print(1)
        print(2)
    else:
        print(3)
else:
    print(4)
print(5)

# 3 5
```



* 택시를 타려면 주머니에 4천원 이상 혹은 카드가 있어야 한다. 이때 택시를 탈수 있는지를 확인하는 코드를 짜보자.

```python
money = 3000
card = True

if money >= 4000 or card:
    print('택시 ㄱ')
else:
    print('BMW')
```

```python
def is_taxi(money,card):
    return '택시 ㄱ' if money >= 4000 or card else 'BMW'
    
is_taxi(3000, False)
```



* 정수 3개가 들어온다. 이때, 2번째로 큰 정수를 출력하라.

```python
def second_number(a, b, c):  # 내 정답
    if a > b:
        a, b = b, a
        if b > c:
            b, c = c, b
            if a > b:
                a, b = b, a
    elif b > c:
        b, c = c, b
        if a > b:
            a, b = b, a
    return b

```

```python
def second_number(*a):  # 입력값이 여러개일 때를 위한 답
    f = a[0]
    s = a[1]
    if f < s:
        f, s = s, f
    a = a[2:]
    for i in a:
        if i > s:
            if i > f:
                s = f
                f = i
            else: 
                s = i
    return s
```



* 환율계산
  * 사용자가 띄어쓰기를 기준으로, (Volume 단위)로 입력한다. 원화로 계산해서 print해주자

```python
volume = 100
unit = '달러'
def currency_calculator(volume, unit):
    currency = { 'USD': 1167, 'JPY': 10.96, 'EUR': 1268, 'CNY': 171 }
    unit_set = { '달러': 'USD', '유로': 'EUR', '위안': 'CNY', '엔': 'JPY' }
    won = round(currency[unit_set[unit]] * volume, 2)  # 소숫점 처리합시다.
    return f'{won} 원'

print(currency_calculator(volume, unit))  # 에러는..?
```

```python
# input => 100 달러, 300 유로, 200 위안, 1000 엔
def currency_calculator(unit):
    currency = { 'USD': 1167, 'JPY': 10.96, 'EUR': 1268, 'CNY': 171 }
    unit_set = {'달러': 'USD', '유로': 'EUR', '위안': 'CNY', '엔': 'JPY'}
    won = round(currency[unit_set[unit.split()[1]]] * int(unit.split()[0]), 2)
    return f'{won} 원'
print(currency_calculator(input('')))  # 이렇게 하면 input으로 입력한 값을 자동 환전해줌.
```



* sigma
  * 정수 n이 들어오면, 1 ~ n까지의 합을 출력 ( 함수로 )

```python
def sigma(n):
    return round((n * (n+1)) / 2)
print(sigma(10))
```



* 99단
  * 'for'와 'range'로 99단 출력하기 ( 띄어 쓰기 두칸)

```python
for i in range(1, 10):
    for j in range(1, 10):
        print(f'{i*j}', end='  ')
    print()
```



* 삼각형
  * 입력으로 높이가 들어옵니다. 높이만큼 산 모양으로 출력하세요( 함수인데, print로 끝.no out)
  * 별 찍을수 있으면 찍기

```python
def tri(h):
    print(' ' * (h-1) + '☆')
    for i in range(1, h+1):
        print((' ' * (h - i)) + ('*' * (i * 2 - 1)))        
```

```python
for i in range(h):
    for j in reversed(range(h)):
        if i < j:
            print(' ', end='')
        else:
            print('*', end='')
    for j in range(h):
        if i > j:
            print('*', end='')
    print()   # 이렇게도 되네;;
```

```python
h = 5  # 이렇게도 해봄 ㅋㅋ
for i in range(h):
    for j in reversed(range(h+1)):
        if i + j == h:
            print(' ' * j + '*' * i + '*' + '*' * i + ' ' * j)
```



* 'colors = ['red', 'green', 'blue', 'white', 'black', 'gold']' 
  * 다음 리스트에서 0, 4, 5 index 에 있는 요소들을 삭제한 새로운 리스트를 만드세요.

```python
colors = ['red', 'green', 'blue', 'white', 'black', 'gold']
delete_index = [0, 4, 5]
remain_colors = []

for index, color in enumerate(colors):
    if index not in delete_index:
        remain_colors.append(color)  # 교수님답 enumerate를 활용
```

아니면

```python
colors = ['red', 'green', 'blue', 'white', 'black', 'gold']
wants = [0, 4, 5]
colors2 = []

for i in wants:
    colors2.append(colors[i])
new_colors = list(set(colors) - set(colors2))

print(new_colors)
```

아니면 

```python
remain_colors = []
for color in colors:
    if colors.index(color) not in (0, 4, 5):
        remain_colors.append(color)
        
print(remain_colors)
```



* 달력 출력하기
  > 1월부터 12월까지 다음과 같은 형태로 달력을 출력하세요.
  >   1 월
  >   일  월  화  수  목  금  토 (1space)
  >    1  2  3   4   5   6   7 (2space)
  >    8  9 10  11  12  13  14
  >   15 16 17 18 19 20 21
  >   22 23 24 25 26 27 28
  >   29 30 31

```python

for i in range(1, 13):
    print(f'{i} 월\n 일 월 화 수 목 금 토 ')
    if i == (1 or 3 or 5 or 7 or 8 or 10 or 12):
        n = 31
    elif i == 2:    
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

# 다시 문제 발생;;
```



### 1. command line interface

#### ls ( in bash ) = dir ( in cmd ) = user -> student ( in 탐색기, ssafy 컴퓨터의 경우 )

* 파일 디렉토리를 보여 준다.
* ls = list, dir = directory

#### pwd ( in bash )

* 현재 위치 ( /C/Users/student)
  * / 는 내 PC이다.

#### ls -a  == ls --all ( in bash )

* 숨김파일까지 모두 보여준다.

* 앞에 .이 붙어있으면 숨김파일이다. (유닉스에서만 지원하고 윈도우에선 지원해주지 않는 기능이다.)

#### cd () ( in bash )

* () 에 입력한 폴더로 이동한다.
* cd .. 은 상위 폴더로 이동이다.

#### mkdir classroom ( in bash )

* classroom 이란 이름의 폴더가 형성된다.

#### touch classmate.txt ( in bash )

* classmate.txt란 이름의 메모장이 형성된다.
* touch a.txt b.txt c.txt d.py e.py  이거처럼 여러 파일을 동시에 만들 수 있다.                                                                                                  

#### vim classmate.txt ( in bash )

* 메모장을 수정하로 간다
* esc키를 눌러야 커맨드를 입력할 수 있다.
* dd가 삭제다
* :w 저장
* :q 나가기
* i 입력



