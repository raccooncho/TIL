# 190103 summary_python



## 1. 조건문



#### 			조건문 문법

* if 문은 반드시 일정한 참/거짓을 판단할 수 있는 조건식과 함께 사용이 되어야 한다.

  * if <조건식>:

* <조건식>이 참인 경우 : 이후의 문장을 수행한다.

* <조건식>이 거짓인 경우 else: 이후의 문장을 수행한다.

* 예제 1 : 조건문을 통해 변수 num의 값과 홀수/짝수 여부를 출력 하세요.

  ```python
  num = int(input("점수를 입력하세요 : "))
  if num % 2 == 0:
      print("짝수 입니다.")
  else:
      print("홀수 입니다.")
  ```



  #### 	복수 조건문

* 2개 이상의 조건문을 활용한 elif <조건식>: 을 활용한다.

* 예제 2 : 조건문을 통해 변수 score에 따른 평점을 출력하세요.

  ```python
  score = int(input("점수를 입력하세요 : "))
  if score >= 90:
      print('A')
  elif score >= 80:
      print('B')
  elif score >= 70:
      print('C')
  elif score >= 60:
      print('D')
  else:
      print('F')
  ```

* 예제 3 :  예제 2에서 95점 이상이면, "참잘했어요"를 함께 출력해 주세요.

  ```python
  score = 96
  if score >= 90:
      print('A')
      if score >= 95:
          print('참잘했어요')
  elif score >= 80:
      print('B')
  elif score >= 70:
      print('C')
  elif score >= 60:
      print('D')
  else:
      print('F')
  ```

* 예제 4 : FizzBuzz

  ```python
  # 3의 배수면, Fizz
  # 5의 배수면, Buzz
  # 3과 5의 배수면, FizzBuzz
  n = int(input('숫자를 입력 하세요 : '))
  for i in range(1, n+1):
      if i % 3 == 0 and i % 5 == 0:
          print('FizzBuzz')
      elif i % 3 == 0:
          print('Fizz')
      elif i % 5 == 0:
          print('Buzz')
      else:
          print(i)
  
  ```


  #### 	조건 표현식(Conditional Expression)

* true_value if <조건식> else false_value 와 같이 작성한다.

  ```python
  num = int(input('숫자를 입력하세요 : '))
  print('3 입니다.') if num == 3 else print('3이 아닙니다.')
  ```

* 표현식은 보통 조건에 따라 값을 정할 때 많이 활용된다.

  ```python
  # 아래의 코드는 무엇을 위한 코드일까요?
  num = int(input("숫자를 입력하세요 : "))
  value = num if num >= 0 else 0
  print(value)  # 음수를 0으로 출력하는 코드
  ```

  ```python
  # 위와 동일한 코드
  num = int(input("숫자를 입력하세요 : "))
  if num >= 0:
      value = num
  else:
      value = 0
  print(value)
  ```

  ```python
  # 다음의 코드와 동일한 조건 표현식을 작성해보세요.
  num = 2
  if num % 2:   # 나머지가 0이면 False고 1이면 True라서 코드가 정상적으로 작동함.
      result = '홀수입니다.'
  else:
      result = '짝수입니다.'
  print(result)
  ```

  ```python
  num = 2
  result = '홀수입니다.' if num % 2 else '짝수입니다.'
  print(result)
  ```



## 2. 반복문



#### 		while 문

* while문은 조건식이 참인 경우 반복적으로 코드를 실핸한다.

* while문은 종료조건을 반드시 설정해 주어야 한다.

  ```python
  n = 0
  while n < 5:
      print(n)
      n += 1
  print('끝')
  ```

* while문 역시 <조건식> 이후에 :이 반드시 필요하며, 들여쓰기를 해주어야 한다.



  #### 	for 문

* for 문은 정해진 범위 내에서 순차적으로 코드를 실행한다.

  ```python
  n = range(10)
  for i in n:
      if i < 5:
          print(i)
  print('끝')
  ```

* for 문은 sequence를 순차적으로 variable에 값을 바인딩하며, 코드 블록을 시행한다.

* 예제 1 : 반복문과 조건문만 활용하여 1~30까지 숫자 중에 홀수만 담긴 리스트를 만드세요.

  ```python
  odd = []
  for i in range(31):
      if i % 2:
          odd.append(i)
  print(odd)
  ```

  ```python
  odds = []
  for i in range(31):
      if i % 2:
          odds = odds + [i]
  print(odds)
  ```

* 예제 2 : 1 부터 100 까지 자연수 중에 5의 배수들의 총합을 구하세요

  ```python
  fifth = []
  for i in range(1, 101):
      if i % 5 == 0:
          fifth = fifth + [i]
  print(sum(fifth))
  ```

  ```python
  f = 0
  for i in range(1, 101):
      if i % 5 == 0:
          f += i
  print(f)
  ```

  ```python
  s = 0
  for i in range(1, int(100/5+1)):
      s += i
  result = s * 5
  
  print(result)
  ```

* index와 함께 for 문 활용하기

  * enumerate( )를 활용하면 추가적인 변수를 활용할 수 있다.

  ```python
  lunch = ['생선까스', '북어해장국', '비엔나소세지']
  for index, menu in enumerate(lunch):
      print(index, menu)
  # 0 생선까스
  # 1 북어해장국
  # 2 비엔나소세지
  ```

  * enumerate( )는 파이썬 내장함수이다.
    * 열거 객체를 돌려줍니다. iterable은 시퀀스, 이터레이터 또는 이터레이션을 지원하는 다른 객체여야 합니다. neumerate( ) 에 의해 반환된 이터레이터의 ____next__ ( ) 메서드는 카운트 (기본값 0 을 갖는 start부터)와 iterable을 이터레이션 해서 얻어지는 값을 포함하는 __튜플__을 돌려줍니다.

  ```python
  mates = ['박준태', '박찬미', '백지원', '송건호', '안도건']
  enumerate(mates)
  # <enumerate at 0x19b03f533f0> -> 16진법으로 메모리에 저장된 위치를 알려준다.
  list(enumerate(mates))
  # [(0, '박준태'), (1, '박찬미'), (2, '백지원'), (3, '송건호'), (4, '안도건')]
  list(enumerate(mates, start = 1))
  # [(1, '박준태'), (2, '박찬미'), (3, '백지원'), (4, '송건호'), (5, '안도건')]
  ```

* dictionary 반복문 활용하기

  ```python
  classroom= { 'teacher': 'Yu', 'leader': 'Hwang', 'CA': 'Kang' }
  for role in classroom:
      print(role)
  ```

  * dictionary 의 key를 출력함으로써 value에도 접근할 수 있다.

  ```python
  for role in classroom:
      print(classroom[role])
  ```

* dictionary에서 for 활용하는 4가지 방법

  * dictionary (key반복)

    ```python
    for key in dict:
        print(key)
    ```

  * key 반복

    ```python
    for key in dict.keys():
        print(key)
    ```

  * value 반복

    ```python
    for val in dict.values():
        print(val)
    ```

  * key 와 value 반복

    ```python
    for key, val in dict.items():
        print(key, val)
    ```

* 예제 : 한번 직접 4가지 반복문을 활용해보고 출력되는 결과를 확인해보세요

  ```python
  classroom = { "teacher": "Kim", "student1": "Hong", "student2": "Kang" }
  ```

  ```python
  for role in classroom:
      print(role)
  # teacher
  # student1
  # student2
  ```

  ```python
  for role in classroom.keys():
      print(role)
  # teacher
  # student1
  # student2
  ```

  ```python
  for member in classroom.values():
      print(member)
  # Kim
  # Hong
  # Kang
  ```

  ```python
  for role, member in classroom.items():
      print(role, member)
  # teacher Kim
  # student1 Hong
  # student2 Kang
  ```




## 3. Break, Continue, else



#### 	Break

* break 문은 반복문을 종료하는 표현이다.

  ```python
  for i in range(10):
      if i == 6:
          break
      print(i)
  # 0
  # 1
  # 2
  # 3
  # 4
  # 5
  ```

* 예제 : 조건문과 반복문, break를 통해서 아래의 코드와 동일한 코드를 작성하세요

  (3이 있을 경우 True를  print하고, 아닐 경우 False를 print합니다.)

  ```python
  numbers = [1, 5, 10]
  result = False
  for i in numbers:
      if i == 3:
          result = True
          break
  print(result)
  ```



#### 	Continue

* continue 문은 continue 이후의 코드를 수행하지 않고 다음 요소를 선택해 반복을 계속 수행한다.

  ```python
  for i in range(10):
      if i % 2 == 0:
          continue  
  # continue를 만나면 밑의 코드는 진행하지 않고 바로 위로 돌아가서 다음 회차로 넘어간다.
      print(f'{i}은 홀수다.')
  ```



#### 	Else

* else 문은 끝까지 반복문을 시행한 이후에 실행됩니다.

  (break를 통해 중간에 종료되지 않은 경우만 실행)

  ```python
  for i in range(3):
      if i == 3:
          print(f'{i}에서 break 실행됨')
          break
  else:
      print('break 안걸림')  # break 안걸림
  ```

  ```python
  for i in range(3):
      if i == 2:
          print(f'{i}에서 break 실행됨')
          break
  else:
      print('break 안걸림')  # 2에서 break 실행됨
  ```



## 4. 함수의 기초

#### 		워밍업

```python
height = 30
width = 20
# 아래에 코드를 작성하세요.
perimeter = (height + width)*2
area = height * width
print(f'직사각형 둘레는 {perimeter}이고 면적은 {area}입니다.')
# 직사각형 둘레는 100이고 면적은 600입니다.
```

```python
def rectangle(width, height):
    area = width * height
    perimeter = (width + height) * 2
    print(f'직사각형 둘레는 {perimeter}이고 면적은 {area}입니다.')
print(rectangle(20, 30))
# 직사각형 둘레는 100이고 면적은 600입니다.
```



#### 		개요

```python
def func(parameter1, parameter2):
    code line1
    code line2
    return value
```

* 함수 선언은 def로 시작하여 :로 끝나고 들여쓰기로 코드블록을 만든다.

* 함수는 매개변수(parameter)를 넘겨줄 수 있다.

* 함수 동작후에 return을 통해 결과값을 전달 할 수있다.

  (return값이 없으면 None를 반환한다.)

  ```python
  a = int('1')
  b = print('hi')  # hi
  c = rectangle(10, 20)  # 직사각형 둘레는 60이고 면적은 200입니다.
  
  print(a)  # 1
  print(b)  # None  -> print의 print는 None이다.
  print(c)  # None  -> return값이 없어서 print했을 경우 None값이 출력된다.
  ```

* 내장함수 목록

|                                                              |                                                              |                      Built-in Functions                      |                                                              |                                                              |
| :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
| [`abs()`](https://docs.python.org/3/library/functions.html#abs) | [`delattr()`](https://docs.python.org/3/library/functions.html#delattr) | [`hash()`](https://docs.python.org/3/library/functions.html#hash) | [`memoryview()`](https://docs.python.org/3/library/functions.html#func-memoryview) | [`set()`](https://docs.python.org/3/library/functions.html#func-set) |
| [`all()`](https://docs.python.org/3/library/functions.html#all) | [`dict()`](https://docs.python.org/3/library/functions.html#func-dict) | [`help()`](https://docs.python.org/3/library/functions.html#help) | [`min()`](https://docs.python.org/3/library/functions.html#min) | [`setattr()`](https://docs.python.org/3/library/functions.html#setattr) |
| [`any()`](https://docs.python.org/3/library/functions.html#any) | [`dir()`](https://docs.python.org/3/library/functions.html#dir) | [`hex()`](https://docs.python.org/3/library/functions.html#hex) | [`next()`](https://docs.python.org/3/library/functions.html#next) | [`slice()`](https://docs.python.org/3/library/functions.html#slice) |
| [`ascii()`](https://docs.python.org/3/library/functions.html#ascii) | [`divmod()`](https://docs.python.org/3/library/functions.html#divmod) | [`id()`](https://docs.python.org/3/library/functions.html#id) | [`object()`](https://docs.python.org/3/library/functions.html#object) | [`sorted()`](https://docs.python.org/3/library/functions.html#sorted) |
| [`bin()`](https://docs.python.org/3/library/functions.html#bin) | [`enumerate()`](https://docs.python.org/3/library/functions.html#enumerate) | [`input()`](https://docs.python.org/3/library/functions.html#input) | [`oct()`](https://docs.python.org/3/library/functions.html#oct) | [`staticmethod()`](https://docs.python.org/3/library/functions.html#staticmethod) |
| [`bool()`](https://docs.python.org/3/library/functions.html#bool) | [`eval()`](https://docs.python.org/3/library/functions.html#eval) | [`int()`](https://docs.python.org/3/library/functions.html#int) | [`open()`](https://docs.python.org/3/library/functions.html#open) | [`str()`](https://docs.python.org/3/library/functions.html#func-str) |
| [`breakpoint()`](https://docs.python.org/3/library/functions.html#breakpoint) | [`exec()`](https://docs.python.org/3/library/functions.html#exec) | [`isinstance()`](https://docs.python.org/3/library/functions.html#isinstance) | [`ord()`](https://docs.python.org/3/library/functions.html#ord) | [`sum()`](https://docs.python.org/3/library/functions.html#sum) |
| [`bytearray()`](https://docs.python.org/3/library/functions.html#func-bytearray) | [`filter()`](https://docs.python.org/3/library/functions.html#filter) | [`issubclass()`](https://docs.python.org/3/library/functions.html#issubclass) | [`pow()`](https://docs.python.org/3/library/functions.html#pow) | [`super()`](https://docs.python.org/3/library/functions.html#super) |
| [`bytes()`](https://docs.python.org/3/library/functions.html#func-bytes) | [`float()`](https://docs.python.org/3/library/functions.html#float) | [`iter()`](https://docs.python.org/3/library/functions.html#iter) | [`print()`](https://docs.python.org/3/library/functions.html#print) | [`tuple()`](https://docs.python.org/3/library/functions.html#func-tuple) |
| [`callable()`](https://docs.python.org/3/library/functions.html#callable) | [`format()`](https://docs.python.org/3/library/functions.html#format) | [`len()`](https://docs.python.org/3/library/functions.html#len) | [`property()`](https://docs.python.org/3/library/functions.html#property) | [`type()`](https://docs.python.org/3/library/functions.html#type) |
| [`chr()`](https://docs.python.org/3/library/functions.html#chr) | [`frozenset()`](https://docs.python.org/3/library/functions.html#func-frozenset) | [`list()`](https://docs.python.org/3/library/functions.html#func-list) | [`range()`](https://docs.python.org/3/library/functions.html#func-range) | [`vars()`](https://docs.python.org/3/library/functions.html#vars) |
| [`classmethod()`](https://docs.python.org/3/library/functions.html#classmethod) | [`getattr()`](https://docs.python.org/3/library/functions.html#getattr) | [`locals()`](https://docs.python.org/3/library/functions.html#locals) | [`repr()`](https://docs.python.org/3/library/functions.html#repr) | [`zip()`](https://docs.python.org/3/library/functions.html#zip) |
| [`compile()`](https://docs.python.org/3/library/functions.html#compile) | [`globals()`](https://docs.python.org/3/library/functions.html#globals) | [`map()`](https://docs.python.org/3/library/functions.html#map) | [`reversed()`](https://docs.python.org/3/library/functions.html#reversed) | [`__import__()`](https://docs.python.org/3/library/functions.html#__import__) |
| [`complex()`](https://docs.python.org/3/library/functions.html#complex) | [`hasattr()`](https://docs.python.org/3/library/functions.html#hasattr) | [`max()`](https://docs.python.org/3/library/functions.html#max) | [`round()`](https://docs.python.org/3/library/functions.html#round) |                                                              |

* 내장함수 목록을 보기 위해서는

  ```python
  dir(__builtins__)
  ```

  을 입력하면 볼 수 있다.



  #### 	함수의 return

* 함수는 오직 한 객체만 반환한다.

* 함수가 return되거나 종료되면, 함수를 호출한 곳으로 돌아간다.

  ```python
  def yes_in_yes_out(x):
      return x  # return 되는것만 함수 값이 출력되는 것이다.
  
  def yes_in_no_out(x):
      print(x)
      
  def no_in_yes_out():
      return 'ss3'
  
  def no_in_no_out():
      print('ss3')
  ```

* 예제 : 아래의 코드와 동일한 my_max함수를 만들어 주세요

  * 정수를 두개 받아서, 큰 값을 반환합니다.

  ```python
  def my_max(num1, num2):
      if num1 > num2:
          return num1
      else: 
          return num2
  ```

  ```python
  def my_max(num1, num2):
      return num1 if num1 > num2 else num2
  ```




  #### 	함수의 인수

* 함수는 인자(parameter)를 넘겨줄 수 있습니다.

* 위치 인수

  * 함수는 기본적으로 인수를 위치로 판단합니다.

  ```python
  def my_func(a, b, c):
      return a * b + c
  print(my_func(1, 2, 3))
  print(my_func(3, 2, 1))  # 순서는 중요하다.
  ```



#### 	기본 값(Default Argument Values)

* 함수가 호출될 때, 인자를 지정하지 않아도 기본 값을 설정할 수 있다.

  ```python
  def func(p1=v1):
      return p1
  ```

  ```python
  def greeting(name='ssafy'):  # name의 기본값을 'ssafy'로 설정함
      return f'{name}, 안녕?'
  
  print(greeting('Cho'))  # Cho, 안녕? -> 기본값을 설정하더라도 입력을 하면 입력값으로 출력됨
  print(greeting())  # ssafy, 안녕?
  ```

* 기본 인자 값이 설정되어 있떠라도 기존의 함수와 동일하게 호출 가능하다.

* 호출시 인자가 없으면 기본 인자 값이 활용된다.

* **기본 매개변수 이후에 기본 값이 없는 매개변수를 사용할 수는 없다.**

  ```python
  def greeting(age, name='ssafy'):  # 기본값이 설정된 변수는 뒷 순서로 가야함. 아니면 오류남.
      return f'{name}은 {age}살 입니다.'
  ```

  ```python
  print(greeting(1))
  print(greeting(0, '미래의 ssafy'))
  print(greeting())  # 이건 Error -> 기본값이 설정되지 않은 변수에 값을 입력해 줘야 한다.
  ```



#### 	키워드 인자(Keyword Arguments)

* 키워드 인자는 직접적으로 변수의 이름으로 특정 인자를 전달할 수 있다.

  ```python
  def greeting(age, name='ssafy'):
      return f'{name}은 {age}살 입니다.'
  print(greeting(30, '서른즈음에'))  # 서른즈음에은 30살 입니다.
  print(greeting(name='아홉수인생', age=29))  # 아홉수인생은 29살 입니다.
  ```

* 키워드 인자를 활용한 뒤에 위치 인자를 활용할 수는 없다.

  ```python
  greeting(age=60, '환갑')  # Error
  ```

* print () 함수

  ```python
  print('hi', end='_')
  print('hi', end='!')  # hi_hi! -> end값을 변경할 수도 있다.
  
  def print(*objects, sep='', end='\n', file=sys.stdout, flush=False)  # 이게 기본 설정 값이다. -> seperate는 Space 1칸, end는 줄바꿈
  ```



  #### 가변 인자 리스트

* print( )처럼 정해지지 않은 임의의 숫자의 인자를 받기 위해서 가변인자를 활용한다.

* 가변인자는 tuple형태로 처리되며 *로 표현한다.

  ```python
  def func(*agrs):
  ```

  ```python
  print(1, 2, 3, 4, 5, 6, end='~!', sep='&')
  # 1&2&3&4&5&6~!
  ```

  ```python
  def unknown_args(*args):
      print(args, type(args))
      
  unknown_args(1, 2, 3, 4, 5, ['a', 'b'])
  # (1, 2, 3, 4, 5, ['a', 'b']) <class 'tuple'>  -> tuple로 묶여서 나옴
  ```

* 예제 : 정수를 여러 개 받아서 가장 큰 값을 반환(return)하는 my_max()을 만들어주세요.

  ```python
  def my_max(*num):
      max_num = num[0]  # 주어진 값 중에서 비교하면 숫자의 크기에 상관없이 모두 비교 가능하다.
      for i in num:
          if i > max_num:
              max_num = i
      return max_num
  print(my_max(10, 20, 30, 40, 50, -99))  # 50
  ```



#### 	정의되지 않은 인자 처리하기

* **kwagrs를 통해 인자를 받아 처리할 수 있다.

* kwagrs는 dict형태로 처리된다.

  ```python
  def unknown_things(**kwargs):  # *이 하나만 있으면 dict로 나오지 않는다.(Error)
      return kwargs              # 'kw'args에서 kw는 *이 두개 붙어있다는 convention이다.
  
  print(unknown_things(a=1, b=2, c=3, d=4))
  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
  ```

  ```python
  result = dict(한국어='안녕', 영어='hi')
  print(result)
  # {'한국어': '안녕', '영어': 'hi'}
  ```

* 예제 : 앞선 fake_dict는 단순히 dictionary형태로 print를 합니다.

  ​	my_dict() 함수를 만들어 실제로 dictionary를 반환하는 함수를 만들어 보세요.

  ```python
  def my_dict(**kwargs):
      return kwargs
  
  my_dict(ssafy='1기', classname='ss3', classroom=703)
  # {'ssafy': '1기', 'classname': 'ss3', 'classroom': 703}
  ```



#### 	Dictionary를 인자로 넘기기(unpacking arguments list)

* **dict 를 통해 함수에 인자를 넘길 수 있습니다.

  ```python
  def signup(username, password, password_confirmation):
      #username이 중복되는지 확인하는 코드는 생략 (username in username같은 형식으로 구현)
      if password == password_confirmation:
          return True
      else:
          return False
  ```

  ```python
  new_account = {
      'username': 'raccooncho',
      'password': 'abcdefg',
      'password_confirmation': 'abcdefg'
  }
  signup(new_account)  # Error
  ```

  ```python
  signup(**new_account)  # True
  # == signup(username='raccooncho', password='abcdefg', password_confirmation='abcdefg')
  print(**new_account)  # Error
  ```



#### 	이름공간 및 스코프(Scope)

* 파이썬에서 사용되는 이름들은 이름공간에 저장되어 있고 LEGB Rule을 가지고 있다.

* 다음과 같은 순서로 이름을 찾아간다

  * Local scope : 정의된 함수
  * Enclosed scope : 상위 함수
  * Global scope : 함수 밖의 변수 혹은 import된 모듈
  * Built-in scope : 파이썬 안에 내장되어 있는 함수 또는 속성

  ```python
  str = 4  # str 값을 정의해버리면 (global scope -> 3순위)
  str(123)  # str 함수가 사라져버림 (built-in scope -> 4순위)
  ```

  ```python
  del str
  str(1)  # 1 -> str = 4를 삭제하면 정상 작동
  ```

  ```python
  a = 1  # global scope -> 3순위
  
  def localscope(a):
      return a  # local scope -> 1순위
  
  localscope(5)
  ```

  ```python
  a = 1
  
  def localscope():
      return a
  
  localscope()  # 1 -> 1순위가 사라져서 3순위인 a = 1값이 출력됨.
  ```

  ```python
  # 전역 변수를 바꿀 수 있나요?
  global_num = 3
  def localscope2():
      global_num = 5
      print(f'global_num이 {global_num}으로 설정됨!')
  localscope2()  # global_num이 5으로 설정됨! 
  print(global_num)  # 3
  # 함수 안에서 선언한 변수는, 함수 밖의 변수와 전혀 상관이 없다.
  ```

  ```python
  # 굳이 전역에 있는 변수를 바꾸고 싶으면 이렇게 할 수 있다.
  재석 = '국민mc'
  def localscope2():
      global 재석
      재석 = '장남' 
      print(f'<재석>이 {재석}으로 설정됨!')
  localscope2()  # <재석>이 장남으로 설정됨!
  print(재석)  # 장남
  # 그래봤자 함수를 한번은 실행해야 <재석>이 바뀐다.
  ```

  ```python
  from IPython.display import YouTubeVideo
  YouTubeVideo('yH_1vwnp3ZQ', width='100%')  # 하면 scope관련 youtube영상이 나옴
  ```

* 이름공간은 각자의 수명주기가 있다.

  * built-in scope : 파이썬이 실행된 이후부터 끝까지
  * Globla scope : 모듈이 호출된 시점 이후 혹은 이름 선언된 이후부터 끝까지
  * Local/Enclosed scope : 함수가 실행된 시점 이후부터 리턴할 때 까지
