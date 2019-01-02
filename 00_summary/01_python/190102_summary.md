# 190102 summary_python



## 0. jupyter setting



git bash 를 실행한 후

```
pip install jupyter
cd TIL
cd 01_basic
git clone https://github.com/eduyu/jupyter_notebooks.git 
# 교수님 github 에서 녹색 clone or download 를 클릭해 링크를 복사해 온다.
```



이러면 교수님의 github에서 jupyter_notebooks를 복사해 올 수 있다.

```
cd jupyter_noteboooks/
ls -a # 이걸로 하위폴더를 확인
rm -rf .git # 이걸로 git 파일 삭제
jupyter notebook # 기본 웹 브라우저에 jupyter notebook 창이 자동으로 뜬다.
(ctrl + c 누르면 jupyter notebook 서버가 종료된다.)
```



cd TIL에서 아래의 실행어를 입력해야 한다. (git과 충돌을 방지하기 위함)

```
echo '.ipynb_checkpoints/' >> .gitignore
git config --global core.autocrlf true
```



jupyter_notebook 폴더에 생긴 unknown폴더를 playground로 바꾼다.

실행된 jupyter notebook 웹에서 playground폴더를 들어간 후 new -> python을 한다.

h키를 누르면 단축키를 알려준다

```
ctrl + enter -> 실행 (할 때 마다 in or out 옆에 숫자가 올라간다. -> 실행 순서인듯)
b -> 새 창 실행
00 -> restart (숫자가 1부터 다시 쌓인다 -> 그 전에 입력한 코드들은 모두 사라진다.)
kernel 에서 restart & clear output 을 누르면 숫자가 아예 사라져서 깨끗하다.
dd -> delete cell
```



git bash에서 몇몇 설치를 한다 ( 필수는 아닌듯 )

```
pip install rise
jupyter-nbextension install rise --py --sys-prefix
jupyter-nbextension enable rise --py --sys-prefix
# 안되면 bash를 입력해서 초기화한 후 한다.
```



### # 예제 : 최대 공약수, 최소 공배수 구하기



#### 구글링한 코드

```python
num1 = 42
num2 = 14

# 최대 공약수 gcd
def gcd(a, b):
    if a < b: # 큰 수가 앞에 오게 정렬
        (a, b) = (b, a)
    while b != 0: # 나머지가 0일때 까지 순환
        (a, b) = (b, a % b)
    return a
    
# 최소 공배수 lcm
def lcm(a, b):
    return a * b / gcd(a, b)

print("최대 공약수는", gcd(num1, num2))
print("최소 공배수는", round(lcm(num1, num2)))
```



#### 내가 생각한 코드

```python
num1 = 42
num2 = 14
num_1 = []
for i in range(1, num1+1):
    if num1 % i == 0:
        num_1.append(i)
num_2 = []
for i in range(1, num2+1):
    if num2 % i == 0:
        num_2.append(i)
num = set(num_1) & set(num_2)
gcd = max(num)
print("최대 공약수는", gcd, "입니다.")
lcm = num1 * num2 / gcd
print("최소 공배수는", round(lcm), "입니다.")•
```



### # 교재는 jupyter에서 01_python_intro를 들어가보자



## 1. python 기초



#### 식별자

* 첫 글자에 숫자가 올 수 없다.

* 사용할 수 없는 예약어가 있다.

  ```python
  # ex 12day = 12  -> 앞글자가 숫자이면 안된다.
  a = 1
  A = 2
  print(a)
  print(A)
  # 사용할 수 없는 예약어
  import keyword
  print(keyword.kwlist)
  ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
  ```

  ```python
  # str() 형변환 함수로 정해진 식별자로 변수를 할당해버리면, 함수호출이 되지 않음.
  str = 'my string'
  str(10) # 이렇게 str을 설정해버리면 str 함수가 먹통이 되어 버린다.
  # 뒤에 코드에 영향이 가니까 변수를 메모리에서 지워줍시다! (or 0,0 / Kernel => restart)
  ```



#### 인코딩 선언

* 정보의 형태나 형식을 변환하는 방식이다.

* 기본 설정은 utf-8 이다.

* 인코딩 설정을 변경하기 위해선 맨 윗줄에

  ```
  -*- coding: utf-8 -*- 
  ```

  을 입력해 주면 된다 . (utf-8에 원하는 인코딩 설정 입력)



#### 주석(Comment)

* 주석은 #으로 표현한다.

* 덩어리 주석은 """으로 표현한다. (docstring)

  ```python
  # 이 줄을 실행되지 않습니다.
  # print('hi')
  def ss3(a, b):
      """ 멀티 스퀘어 703호
      반장: 황은석
      총무: 강진우
      새해 복 많이 받으세요.    
      """
      return(a + b)
  ```

  ```python
  print(ss3(1, 2)) # 이러면 주석처리된 부분은 출력되지 않고 1 + 2의 값인 3이 출력된다.
  print(ss3.__doc__) # .__doc__ 을 뒤에 붙이면 주석이 출력된다.
  ```



#### 코드 라인

* 파이썬에서는 ;을 작성하지 않는다.

* 한줄로 표기할 때는 ;를 작성하여 표기할 수 있다.

* 거의 안쓴다.

  ```python
  print('ss3'); print('coding')
  # 이렇게 쓰면 된다.
  ```

* 줄을 여러줄 작성할 때는 역슬래시 ( \ )를 사용하여 사용할 수 있다.

  ```python
  a = 'longlongword'
  if a \
  == 'longlongword':
  	print(a)
  ```

* [ ], { }, ( ) 는 \ 없이도 가능하다.

  ```python
  ['a',
  'b',
  'c']
  ```



## 2. 변수 및 자료형

* 변수는 = 을 통해 할당된다.

* 자료형을 확인하기 위해서는 type( )을 활용한다.

* 메모리 주소를 확인하기 위해서는 id( )를 활용한다.

  ```python
  x = 1004
  print(x)  # 1004
  print(type(x))  # <class 'int'> -> integer (정수)
  print(id(x))  # 2655147411376
  
  x = 10004
  print(x)  #10004
  print(type(x))  # <class 'int'>
  print(id(x))  # 2655147410512 -> 확인 할때마다 바뀜.
  
  x = 1
  print(id(x))  # 1983408896 -> 자주 쓰는 숫자는 고정되어 있음. (1 ~ 256)
  ```

* 같은 값을 동시에 할당할 수 있다.

  ```python
  x = y = 100
  ```

* 다른 값을 동시에 할당 가능하다

  ```python
  a = 1
  b = 2
  
  tmp = a
  a = b
  b = tmp  # 원래는 임시변수를 지정해서 순서를 바꿔야 한다.
  
  print(a)
  print(b)
  ```

  ```python
  a = 1
  b = 2
  
  a = a + b
  b = a - b
  a = a - b  # 이렇게도 가능하다.
  
  print(a)
  print(b)
  ```

  ```python
  a, b = 1, 2
  a, b = b, a
  print(a)  # a = 2
  print(b)  # b = 1   python 에서는 a, b 순서를 동시에 변경할 수 있다.
  ```

  ```python
  x, y = 1  # 이건 안됨.
  x, y = 1, 2, 3  # 이것도 안됨.
  ```



#### 수치형(Numbers)

* int (정수)

  ```python
  i = 100
  type(i)  # int
  ```

* 파이썬 3.x 버전에서는 `long` 타입은 없고 모두 `int` 형으로 표기 된다.

  ```python
  i = 2 ** 64
  print(i, type(i))  # 18446744073709551616 <class 'int'>
  ```

  ```python
  import sys
  max_int = sys.maxsize
  print(max_int)  # 9223372036854775807
  max_int = sys.maxsize * sys.maxsize
  print(max_int)  # 85070591730234615847396907784232501249
  ```

* 10진수가 아닌 8진수 : `0o`/2진수 : `0b` /16진수: `0x`로도 표현 가능하다.

  ```python
  binary_number = 0b100  # 0b = 2진수 코드 / 100 = 4
  octal_number = 0o777  # 0o = 8진수 코드 / 777 = 511
  hexadecimal_number = 0xfff  # 0x = 16진수 코드 / fff = 4095 -> 123456789abcdef
  decimal_number = 2019  # 2019
  ```



#### 부동 소수점, 실수 (float)

* 실수는 float로 표현된다.

  ```python
  a = 3.5
  type(a)  # float
  ```

  ```python
  b = 314 * 10**-2 # = 314e-2 (e = 10**)
  b  # 3.14
  ```

* 실수의 경우 실제 값을 처리할 때 조심할 필요가 있다. (오류가 발생할 수 있다.)

  ```python
  3.5 + 3.2  # 6.7
  3.5 - 3.12  # 0.3799999999999999 -> 오류 발생..
  round(3.5 - 3.12, 2)  # 0.38
  ```

  ```python
  0.1 * 3 == 0.3  # False
  0.1 * 3  # 0.30000000000000004
  ```

* 처리 방법 1 : 절대값을 비교

  ```python
  a = 0.1 * 3
  b = 0.3
  a - b  # 5.551115123125783e-17
  ```

  ```python
  a = 0.1 * 3
  b = 0.3
  abs(a - b) <= 1e-10  # True
  ```

* 처리 방법 2 : 절대값 비교를 내장된 float epsilon값과 비교

  ```python
  import sys
  abs(a - b) <= sys.float_info.epsilon  # True 
  sys.float_info.epsilon  # 2.220446049250313e-16 -> 시스템에 내장된 가장 작은 수
  ```

* 처리 방법 3 : math 모듈을 통해 근사한 값인지 비교

  ```python
  import math
  math.isclose(a, b)  # True
  ```



#### 복소수 (complex)

* 복소수는 허수부를 j로 표현한다.

  ```python
  a = 3 - 4j
  type(a)  # complex
  ```

  ```python
  print(a.imag)  # -4.0
  print(a.real)  # 3.0
  print(a.conjugate())  # (3+4j)
  print(a.conjugate() * a)  # (25+0j)
  ```



#### Bool

* 파이썬에는 `True`와 `False`로 이뤄진 `bool` 타입이 있다.

  ```python
  print(type(True), type(False))  # <class 'bool'> <class 'bool'>
  print(True, 1 == 1, 3 > 2)  # True True True
  print(False, 1 != 1, 3 < 2)  # False False False
  ```

* 0, 0.0, ( ), [ ], { }, ' ', None 등도 False로 변환된다.

  ```python
  bool(0)  # False
  bool(None)  # False
  bool([])  # False
  bool('')  # False
  
  bool(1)  # True
  bool([0])  # True
  ```



#### 문자형 (String)

* 문자열은 Single quotes( ' )나 Double quotes( " )을 활용하여 표현 가능하다.

* 단 시작과 끝은 동일한 문장부호로 유지해야 한다. 

* PEP-8에서는 **하나의 문장부호를 선택하여 유지**하도록 하고 있다.

  ```python
  greeting = 'Hi'
  name = 'Cho Seong Kyu'
  print(greeting, name)  # Hi Cho Seong Kyu
  ```

* 문자열 안에 문장부호가 활용될 경우 \를 사용하는 것 대신 활용 가능 하다.

  ```python
  print('스티브 잡스가 말하길, 'Real Artist Ship'')  # 오류 납니다.
  print('스티브 잡스가 말하길, "Real Artist Ship"')  # 스티브 잡스가 말하길, "Real Artist Ship"
  print('he saids, \'Real Artist Ship\'')  # he saids, 'Real Artist Ship' -> ( \' ) 합쳐서 하나의 문장 부호임.
  ```

* 여러줄에 걸쳐있는 문장은 """를 이용하여 표현 가능하다.

  ```python
  print("""
  말하는대로,
  쓰는대로,
  다 써져요!
  """)  # 이대로 출력된다.
  ```

  ```python
  name = 'raccooncho'
  print("""
  my name is {}
  """.format(name))  # my name is raccooncho
  ```



#### 이스케이프 문자열

| 예약문자 |   내용(의미)    |
| :------: | :-------------: |
|    \n    |     줄바꿈      |
|    \t    |       탭        |
|    \r    |   캐리지리턴    |
|    \0    |    널(Null)     |
|   \ \    |        \        |
|    '     | 단일인용부호(') |
|    "     | 이중인용부호(") |

```python
print('이 다음에 새 줄이 시작됨. \n 그리고 나온다 탭 \t얍')
# 이 다음에 새 줄이 시작됨.
# 그리고 나온다 탭     얍
```

* 출력할 때 활용하는 방법

  ```python
  print('나는 뒤에 문자열과 떨어지기 싫어', end='\n')
  print('나는 앞에 문자열과 너무 가깝기 싫어')
  # 나는 뒤에 문자열과 떨어지기 싫어
  # 나는 앞에 문자열과 너무 가깝기 싫어
  ```

  ```python
  print('나는 뒤에 문자열과 떨어지기 싫어', end='\t')
  print('나는 앞에 문자열과 너무 가깝기 싫어')
  # 나는 뒤에 문자열과 떨어지기 싫어	나는 앞에 문자열과 너무 가깝기 싫어
  ```

  ```python
  print('나는 뒤에 문자열과 떨어지기 싫어', end='~~~~')
  print('나는 앞에 문자열과 너무 가깝기 싫어')
  # 나는 뒤에 문자열과 떨어지기 싫어~~~~나는 앞에 문자열과 너무 가깝기 싫어
  ```

* 깜짝 퀴즈

  ```
  다음의 문장을 출력해보세요.
  
  """ 사용 금지
  print 여러번 사용 금지
  "파일은 C:\Windows\Users\내문서\Python에 저장이 되어있습니다."
  나는 생각했다. 'cd를 써서 git bash로 들어가봐야지'
  ```

  ```python
  print('"파일은 C:\\Windows\\Users\\내문서\\Python에 저장이 되어 있습니다."\n 나는 생각했다. \'cd를 써서 git bash로 들어가봐야지\'')
  # "파일은 C:\Windows\Users\내문서\Python에 저장이 되어 있습니다."
  #  나는 생각했다. 'cd를 써서 git bash로 들어가봐야지'
  ```



#### String interpolation

* %-formatting

  ```python
  name = 'Cho'
  year = 2019
  'Hello %s' % name  # 'Hello Cho'
  ```

* str.format()

  ```python
  'Hello, {}'.format(name)  # 'Hello, Cho'
  ```

* f-strings ( python 3.6 이상 버전에서만 지원됨)

  ```python
  f'Hello, {name}, It\'s {year}'  # "Hello, Cho, It's 2019"
  ```

  ```python
  import datetime
  today = datetime.datetime.now()
  f'오늘은 {today:%y}년 {today:%m}월 {today:%d}일 {today:%A}'
  # '오늘은 19년 01월 02일 Wednesday'
  ```

  ```python
  pi = 3.1415926535
  r = 2
  f'원주율은 {pi:0.3}, 반지름 {r}인 원의 넓이는 {pi * r ** 2:0.3}'
  # '원주율은 3.14, 반지름 2인 원의 넓이는 12.6'
  ```


## 3. 연산자

산술 연산자

| 연산자 |   내용   |
| :----: | :------: |
|   +    |   덧셈   |
|   -    |   뺄셈   |
|   *    |   곱셈   |
|   /    |  나눗셈  |
|   //   |    몫    |
|   %    |  나머지  |
|   **   | 거듭제곱 |

* 예시

  ```python
  print(5 / 2)  # 나누기 2.5
  print(5 // 2)  # 몫 2
  print(5 % 2)  # 나머지 1
  ```

  ```python
  divmod(5, 2)
  quotient, remainder = divmod(5, 2)
  # quotient = divmod(5, 2)[0]
  # remainder = divmod(5, 2)[1]
  print(f'몫은 {quotient}, 나머지는 {remainder}') # 몫은 2, 나머지는 1
  ```

  ```python
  positive_num = 4
  print(-positive_num)  # -4
  print(--positive_num)  # 4
  ```



  #### 비교 연산자

| 연산자 |   내용    |
| :----: | :-------: |
| a > b  |   초과    |
| a < b  |   미만    |
| a >= b |   이상    |
| a <= b |   이하    |
| a == b |   같음    |
| a != b | 같지 않음 |

  ```python
  3 > 6  # False
  3 != 4  # True
  3.0 == 3  # True	
  type(3.0) == type(3)  # False
  'HI' == 'hi'  # False
  ```



  #### 논리 연산자

| 연산자  |             내용             |
| :-----: | :--------------------------: |
| a and b |   a와 b 모두 True시만 True   |
| a or b  |  a와 b 모두 False시만 False  |
|  not a  | True -> False, False -> True |

  ```python
  print(True and True and True and False)  # 하나라도 False면 다 False
  print(True and True and True)  # True -> eg. Login
  ```

  ```python
  print(False or False or True or False)  # 하나라도 True면 다 True -> eg. 학생증 밥먹기
  ```

  ```python
  print(not True)  # False
  print(not 0)  # True
  print(not True and not 0)  # False
  ```

* 파이썬에서 and는 a가 거짓이면 a를 리턴하고, 참이면 b를 리턴한다.

  ```python
  print(3 and 5)  # 5
  print(0 and 3)  # 0 -> 0이 출력된다.
  print(5 and 3)  # 3 -> 뒤의 숫자가 나온다.
  ```

* 파이썬에서 or은 a가 참이면 a를 리턴하고, 거짓이면 b를 리턴한다.

  ```python
  print(3 or 5)  # 3
  print(0 or 3)  # 3 -> 하나라도 참이면 참을 return한다.
  print(0 or 0)  # 0
  print(5 or 3)  # 5 -> 앞의 숫자가 나온다.
  ```



#### 복합 연산자

| 연산자  | 내용       |
| ------- | ---------- |
| a += b  | a = a + b  |
| a -= b  | a = a - b  |
| a *= b  | a = a * b  |
| a /= b  | a = a / b  |
| a //= b | a = a // b |
| a %= b  | a = a % b  |
| a **= b | a = a ** b |

```python
a = 1
a = a + 1
a += 1
print(a)  # 3

b = 10
b *= 5
print(b)  # 50
```

```python
count = 0
while count < 5:
    print(f'{count} 번째 얍!')
    count += 1
    
# 0 번째 얍!
# 1 번째 얍!
# 2 번째 얍!
# 3 번째 얍!
# 4 번째 얍!
```



#### 기타 연산자

* Concatenation : 숫자가 아닌 자료형은 + 연산자를 통해 합칠 수 있다.

  ```python
  print('hi' + '2019')  # hi2019
  print([1] + [2, 3])  # [1, 2, 3]
  ```

* Containment Test : in 연산자를 통해 속해있는지 여부를 확인할 수 있다.

  ```python
  'a' in 'apple'  # True
  'pe' in 'apple'  # False
  ```

  ```python
  1 in [1, 2, 3]  # True
  print('b' in {'a', 'b', 'c'})  # True
  ```

  ```python
  3 in range(10)  # True
  10 in range(10)  # False
  ```

* Identity : is 연산자를 통해 동일한 object인지 확인할 수 있다.

  ```python
  a = 10
  b = 10
  print(a == b)  # True
  print( a is b)  # True
  print(id(a), id(b))  # 1983409184 1983409184
  
  x = 257
  y = 257
  print(x == y)  # True
  print(x is y)  # False -> 256범위 넘어가서 id값으로 판단, id 값이 다르므로 False
  print(id(x), id(y))  # 2485985830544 2485985831056
  ```

* Indexing / Slicing : [ ]를 통한 값 접근 및 [ : ] 을 통한 슬라이싱

  ```python
  print([1,2,3][0])  # 1
  print(('a', 'b', 'c')[1])  # b
  print('apple'[4])  # e
  print({1, 2, 3}[1])  # 이건 인덱스 접근이 안됨 -> 집합(set)에는 순서가 없음.
  ```



#### 연산자 우선 순위

```
0. ()을 통한 grouping
1. Slicing
2. Indexing
3. 제곱연산자 **
4. 단항연산자 +, - (음수/양수 부호)
5. 산술연산자 *, /, %
6. 산술연산자 +, -
7. 비교연산자, in, is
8. not
9. and
10. or
```



## 4.기초 형변환(Type conversion, Typecasting)

* 파이썬에서 데이터타입은 서로 변환할 수 있다.



##### 암시적 형변환(Implicit Type Conversion)

* 사용자가 의도하지 않았지만, 파이썬 내부적으로 자동으로 형변환하는 경우이다. 아래의 상황에서만 가능하다.

  * bool
  * Numbers (int, float, complex)

  ```python
  True + 3  # 4 -> True == 1
  ```

  ```python
  int_number = 3
  float_number = 5.0
  complex_number = 3 + 5j
  print(int_number + float_number)  # 8.0
  print(int_number + complex_number)  # (6+5j)
  ```



##### 명시적 형변환(Explicit Type Conversion)

* 위 상황을 제외하고는 명시적 형변환을 해 주 어야 한다.

  * string -> integer :  형식에 맞는 숫자만 가능
  * integer -> string : 모두 가능
  * float는 int로 변환이 가능

* 암시적 형변환이 되는 모든 경우도 명시적으로 형변환이 가능하다

  * `int()` : string, float를 int로 변환
  * `float()` : string, int를 float로 변환
  * `str()` : int, float, list, tuple, dictionary를 문자열로 변환

  ```python
  str(1) + '등'  # '1등'
  1 + int('등')  # 안됨
  int('1')  # 1
  int('00010')  # 10
  int('10.0')  # 안됨 -> 10.0은 float
  float('10.0')  # 10.0
  int(3.5)  # 3 -> 버림
  ```

  ```python
  int('55') + 10  # 65
  str(55) + '10'  # 5510
  ```



## 5. 시퀀스(sequence) 자료형

* 시퀀스는 데이터의 순서대로 나열된 형식이다.

  ! 순서대로 나열된 것이 정렬되었다는 뜻은 아니다.

* 기본적인 시퀀스 타입

  * 리스트 (list)

  * 튜플 (tuple)

  * 레인지 (range)

  * 문자열 (string)

  * 바이너리 (binary) : 따로 다루지 않음.

    ! set 과 dic은 시퀀스타입에 포함되지 않는다.



  #### list

  ```python
  [value1, value2, value3]  # list는 대괄호 [ ]를 통해 만들 수 있다.
  list[1]  # 값에 대한 접근은 list[i]를 통해 한다.
  ```

  ```python
  locations = ['서울', '대전', '구미', '광주']
  print(locations)  # ['서울', '대전', '구미', '광주']
  seoul = locations[0]
  print(seoul)  # 서울
  ```



  #### tuple

  ```python
  (value1, value2) # tuple은 ( )로 묶어서 표현한다.
  # tuple은 수정 불가능하고, 읽을 수 밖에 없다.
  ```

  ```python
  my_tuple = (1, 2, 3)  # class 'tuple'
  is_tuple = 'a', 'b'  # class 'tuple'
  ```

  ```python
  x, y = (1, 2)
  print(x, y)  # 1 2
  x, y = y, x
  print(x, y)  # 2 1  -> swap하는 코드는 tuple을 활용한다.
  ```



#### 	range

*  기본형 : range(n)
  * 0부터 n-1까지 값을 가짐

```python
list(range(10))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

* 범위 지정 : range(n, m)
  * n부터 m-1까지 값을 가짐

```python
list(range(5, 15))
# [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
list(range(-10, -20))
# 안나옴, 앞의 수가 더 커야함
```

* 범위 및 스텝 지정 :  range(n, m, s)
  * n부터 m-1까지 +s만큼 증가함

```python
list(range(5, 1, -1))
# [5, 4, 3, 2]
list(range(0, -10, -2))
# [0, -2, -4, -6, -8]
```



#### 	시퀀스에서 활용할 수 있는 연산자 / 함수

| operation  |          설명           |
| :--------: | :---------------------: |
|   x in s   |    containment test     |
| x not in s |    containment test     |
|  s1 + s2   |      concatenation      |
|   s * n    | n번만큼 반복하여 더하기 |
|    s[i]    |        indexing         |
|   s[i:j]   |         slicing         |
|  s[i:j:k]  |    k간격으로 slicing    |
|   len(s)   |          길이           |
|   min(s)   |         최솟값          |
|   max(s)   |         최댓값          |
| s.count(x) |        x의 갯수         |

* 예시

  ```python
  string = 'my string'
  print('y' in string)
  l = [1, 2, 3]  # True
  print(1 in l)  # True
  print(2 not in l)  # False
  ```

  ```python
  print('happy' + 'hacking')  # happyhacking
  print(['a', 'p', 'p'] + ['l', 'e'])  # ['a', 'p', 'p', 'l', 'e']
  ```

  ```python
  print('x' * 10)  # xxxxxxxxxx
  print([1, 2, 3] * 10) 
  # [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
  ```

  ```python
  names = ['강진우', '고재두', '곽동령', '권성령', '권택건']
  ca = names[0]
  print(ca)  # 강진우
  ```

  ```python
  new_list = [names[1], names[2]]
  print(new_list)  # ['고재두', '곽동령']
  neo_list = names[1:4]
  print(neo_list)  # ['고재두', '곽동령', '권성령']
  ```

  ```python
  r = range(30)
  r = r[0:len(r):3]
  list(r)  # [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
  list(r)[1:]  # [3, 6, 9, 12, 15, 18, 21, 24, 27]
  ```

  ```python
  min(r)  # 0
  max(r)  # 27
  max(range(100))  # 99
  ```

  ```python
  [1, 2, 3, 4, 5, 6, 7].count(5)  # 1 -> 5가 1개 있음.
  [1, 2, 3, 4, 5, 5, 5, 5, 5, 6, 7].count(5)  # 5
  ```



## 6. set, dictionary

* set 과 dictionary 는 기본적으로 순서가 없다.



#### set

* set = 집합 / 중괄호 { }를 이용

  |    연산자/함수    |  설명  |
  | :---------------: | :----: |
  |       a - b       | 차집합 |
  |      a \| b       | 합집합 |
  |       a & b       | 교집합 |
  |    a.union(b)     | 교집합 |
  | a.intersection(b) | 교집합 |

  ```python
  my_number = {1, 2, 3, 4, 5, 6}
  lotto = {1, 2, 4, 5, 8, 9}
  print(my_number & lotto) 
  # {1, 2, 4, 5}  -> 교집합 (중복값은 한번만 출력됨 -> 중복은 피하자)
  ```

* set을 활용하면 list의 중복값을 손쉽게 제거할 수 있다.

  ```python
  joongbok = [1, 2, 3] * 10
  my_set = set(joongbok)
  unique = list(my_set)
  print(unique)  #  [1, 2, 3]
  ```



#### dictionary

* 딕셔너리는 key와 value가 쌍으로 이루어져있는 자료구조

  * {Key1:Value1, Key2:Value2, . . .}

* { }를 통해 만들며, dict( )로 만들 수 있다.

* key는 immutable한 모든 것이 가능하다

  * 불변값 : string, integer, float, boolean, tuple, range

* value는 list, dictionary를 포함한 모든 것이 가능하다.

  ```python
  ss3 = { 'leader':'황은석', 'CA':'강진우' }
  ss3['leader']  # '황은석'
  ```

* 중복된 key는 존재할 수 없다.

  ```python
  my_dict = { 1: 1, 1: 2, 2: 1 }
  print(my_dict)  # { 1: 2, 2: 1 }
  ```

* 메소드를 이용하여 key와 value를 확인할 수 있다.

  ```python
  ss3.keys()  # dict_keys(['leader', 'CA'])
  ss3.values()  # dict_values(['황은석', '강진우'])
  
  ```




