# 190116 summary_OOP_Module_Error



### 1. OOP

##### 용어 정리

```python
class Person:  # 클래스 정의(선언) : 클래스 객체 생성
    name = '홍길동'  # 멤버 변수(데이터 어트리뷰트)
    def greeting(self):  # 멤버 메서드(메서드)
        print(f'{self.name}')
        
iu = Person()  # 인스턴스 객체 생성
iu.name  # 데이터 어트리뷰트 호출
iu.greeting  # 메서드 호출
```



##### `Self` : 인스턴스 객체 자기 자신

* 특별한 상황을 제외하고는 무조건 메서드에서 `self`를 첫번째 인자로 설정한다.
* 메서드는 인스턴스 객체가 함수의 첫번째 인자로 전달되도록 되어있다.

```python
p.name = 'kim ssafy'
print(p.greeting())  # hi kim ssafy
print(Person.greeting(p))  # hi kim ssafy
```



##### 클래스 - 인스턴스 간 이름공간

* 클래스 정의를 하면 클래스 객체가 생성되고, 해당하는 이름공간이 생성된다.
* 인스턴스를 만들 때도 인스턴스 객체가 생성되고, 해당하는 이름공간이 생성된다.
* 인스턴스의 어트리뷰트가 변경되면, 변경된 데이터를 인스턴스 객체 이름공간에 저장한다.
* 인스턴스에서 특정 어트리뷰트에 접근한 순간 **인스턴스 -> 클래스** 순으로 탐색을 한다.



##### 생성자 / 소멸자

* 생성자는 인스턴스 객체가 생성될 때 호출되는 함수이며, 소멸자는 객체가 소멸되는 과정에서 호출되는 함수이다.

```python
class Person:
	def __init__(self):
        print('생성될 때 자동으로 호출되는 메서드')
    def __del__(self):
        print('소멸될 때 자동으로 호출되는 메서드')
```

* 양 쪽에 `__`로 가둬져 있는 메서드는 스페셜 메서드 혹은 매직 메서드로 불린다.

```python
p1 = Person()  # '생성될 때 자동으로 호출되는 메서드'
del p1  # '소멸될 때 자동으로 호출되는 메서드'
```

* 생성자 또한 메서드 이기 때문에 추가적인 인자를 받을 수 있다.

```python
def __init__(self, parameter1, parameter2):
    print('생성될 때 자동으로 호출되는 메서드입니다.')
    print(parameter1)
def __init__(self, *args):
    print('생성될 때 자동으로 호출되는 메서드입니다.')
def __init__(self, **kwagrs):
    print('생성될 때 자동으로 호출되는 메서드입니다.')
```



##### 클래스 변수 / 인스턴스 변수

```python
class Person:
    population = 0  # 클래스 변수 : 모든 인스턴스가 공유함.
    def __init__(self, name):
        self.name = name  # 인스턴스 변수 : 인스턴스 별로 각각 가지는 변수
        Person.population += 1  # Person class가 가지는 클래스 변수인 population이 1올라감.
```





##### 정적 메서드 / 클래스 메서드

* 인스턴스가 아닌 클래스가 메서드호출을 할 수 있도록 구성할 수 있다.
* 이때 활용되는게 정적 메서드 혹은 클래스 메서드 이다.
* 정적 메서드는 객체가 전달되지 않은 형태이며, 클래스 메서드는 인자로 클래스를 넘겨준다.

```python
class Dog:
    num_of_dogs = 0
    birth_of_dogs = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Dog.num_of_dogs += 1
        Dog.birth_of_dogs += 1
    def __del__(self):
        Dog.num_of_dogs -= 1  
    @staticmethod  # 정적 메서드
    def info():
        return f'총 {Dog.num_of_dogs}마리의 강아지가 있습니다.'
    
    @classmethod  # 클래스 메서드 -> 클래스 변수에 접근할 수 있음
    def birth(cls):
        return f'총 {cls.birth_of_dogs}마리의 강아지가 태어났습니다.'
```

* 정적 메서드와 클래스 메서드는 선언과 함수가 `\n`으로 떨어지면 안된다. (붙어있어야 함)
* 예제 1 : 정적 메서드를 활용하여 계산기를 만들어 보세요.

```python
class Calculator:
    @staticmethod
    def add(num1, num2):
        return num1 + num2
    @staticmethod
    def sub(num1, num2):
        return num1 - num2 
    @staticmethod
    def mul(num1, num2):
        return num1 * num2
    @staticmethod
    def div(num1, num2):
        return num1 / num2
    
Calculator.add(1, 2)  # 1 + 2 =3
Calculator.sub(1, 2)  # 1 - 2 = -1
Calculator.mul(1, 2)  # 1 * 2 =  2
Calculator.div(1, 2)  # 1 / 2 = 0.5
```

* 예제 2 : `stack` class를 구현해 봅시다.
  1. empty() : 스택이 비었다면 참을 주고, 그렇지 않다면 거짓이 된다.
  2. top() : 스택의 가장 마지막 데이터를 넘겨준다. 스택이 비었다면 None을 리턴해주세요.
  3. pop() : 스택의 가장 마지막 데이터의 값을 넘겨주고 해당 데이터를 삭제한다. 스택이 비었다면 None을 리턴해주세요.
  4. push() : 스택의 가장 마지막 데이터 뒤에 값을 추가한다. 리턴값 없음

```python
class Stack:  # 내 코드
    def __init__(self):
        self.items = []
    def empty(self):
        if self.items:
            return False
        else:
            return True
    def top(self):
        if self.items:
            return self.items[-1]
    def pop(self):
        if self.items:
            answer = self.items[-1]
            self.items.remove(answer)
            return answer
        else:
            return None        
    def push(self, *datas):
        for data in datas:
            self.items.append(data)
```

```python
class Stack:   # 선생님 코드
    def __init__(self):
        self.items = []
    def empty(self):
        return not bool(self.items)
    def top(self):
        if self.items:
            return self.items[-1]
    def pop(self):
        if self.empty():
            return None
        else:
            self.items.pop()
    def push(self, e):
        self.items.append(e)
```

* `repr`, `str` (class 안에서...)

```python
def __repr__():   # 그냥 인스턴스만 출력 했을 때 출력되는 값을 설정할 수 있음. (in str)
   				  # 객체가 리턴하는 값
def __str__():   # 그냥 인스턴스를 print했을 때 출력되는 값을 설정할 수 있음. (in str)
    			 # 객체를 print했을 때 return 하는 값
```



##### 연산자 오버라이딩 (기본적으로 정의된 연산자의 정의를 덮어 씌워서 마음대로 정함!!!)

|     +     |     -     |     *     |    <     |    <=    |    ==    |    !=    |    >=    |    >     |
| :-------: | :-------: | :-------: | :------: | :------: | :------: | :------: | :------: | :------: |
| `__add__` | `__sub__` | `__mul__` | `__lt__` | `__le__` | `__eq__` | `__ne__` | `__ge__` | `__gt__` |

```python
class Person:
    population = 0
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.population += 1
        
    def greeting(self):
        print(f'{self.name}입니다. 반갑습니다!')
        
    def __repr__(self):
        return f"< 'name' : {self.name}, 'age' : {self.age} >"
    
    def __gt__(self, other):
        if self.age > other.age:
            return f'{self.name} is 연장자'
        else:
            return f'{other.name} is 연장자'
```

```python
p1 = Person('cho', 22)
p2 = Person('kim', 19)

p1 > p2  # 'cho is 연장자'  -> " > " 비교하는 연산자가 내가 설정한 함수로 출력되는 것을 볼 수 있다.
```



##### 상속

* 부모 클래스의 모든 속성이 자식클래스에게 상속된다.

```python
class Person:  # 부모 클래스
    population = 0
    def __init__(self,name='사람'):
        self.name = name
        Person.population += 1
    def greeting(self):
        print(f'반갑습니다, {self.name}입니다.')
```

```python
class Student(Person):  # 자식 클래스, 괄호 안에 부모클래스를 적어주어야 한다.
    def __init__(self, student_id, name='학생'):
        self.name = name
        self.student_id = student_id
```

```python
issubclass(Student, Person)  # `issubclass(자식, 부모)로 상속 관계를 확인할 수 있다.
```



##### super()

* 자식 클래스에 메서드를 추가 구현할 수 있다.
* 부모클래스의 내용을 사용하고자 할 때, `super()`를 사용할 수 있다.

```python
class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email 
        
    def greeting(self):
        print(f'안녕, {self.name}')
        
class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        super().__init__(name, age, number, email)  # ==> Person / 상위 클래스를 받아 옴
        self.student_id = student_id
```



##### 메소드 오버라이딩

* 메서드를 재정의할 수도 있다.
  * 부모 클래스와 자식 클래스에 이름이 같은 메서드가 있으면 자식 클래스가 덮어씌워서 적용된다.



##### 상속관계에서의 이름공간

* 기존에 인스턴스 -> 클래스 순으로 이름공간을 탐색해 나가는 과정에서 상속관계에 있으면 다음과 같이 확장된다.
  * 인스턴스 -> 자식클래스 -> 부모클래스 -> 전역
  * 다중 상속이라면 먼저 들어온 클래스가 우선이다.

```python
class Person:
    def __init__(self, name):
        self.name = name
    def breath(self):
        return '날숨'
    def greeting(self):
        return f'hi {self.name}'
    
class Mom(Person):
    gene = 'XX'
    
    def swim(self):
        return '첨벙첨벙'

class Dad(Person):
    gene = 'XY'
    
    def kick(self):
        return '슛'
class Child(Mom, Dad):  # Mom이 먼저 들어옴
    def cry():
        return '응애'

c = Child('애')
print(c.swim())  # 첨벙첨벙
print(c.kick())  # 슛
print(c.gene)  # XX  -> 먼저 들어온 Mom의 속성을 상속받는다.
print(c.greeting())  # hi 애  -> 직접 상속받지 않더라도 상속 받는다.(할아..버지?)
```



### 2. Module

##### 모듈 활용 기초

* `표준 라이브러리`에서 기본 제공되는 모듈을 확인할 수 있다.
  * https://docs.python.org/ko/3/library/index.html
* `dir()`을 이용해서 사용할 수 있는 메서드를 확인해보자.

```python
import random
print(dir(random))
```

```python
['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', '_BuiltinMethodType', '_MethodType', '_Sequence', '_Set', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_acos', '_bisect', '_ceil', '_cos', '_e', '_exp', '_inst', '_itertools', '_log', '_pi', '_random', '_sha512', '_sin', '_sqrt', '_test', '_test_generator', '_urandom', '_warn', 'betavariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']
```



##### from 모듈명 import 어트리뷰트

```python
from bs4 import BeautifulSoup
from random import sample
```

* 이렇게 특정 어트리뷰트만 import한다면 편하게 사용할 수 있다.

  ```python
  sample([1, 2, 3], 2)
  ```



##### from 모듈명 import *

* 해당하는 모듈 내의 모든 변수, 함수, 클래스를 가져온다.



##### from 모듈명 import 어트리뷰터 as 이름

* 내가 지정하는 이름으로 이름을 지정하여 가져올 수 있다.



#### 숫자 관련 함수

* 이외에도 분수(frctions), 십진(decimal), 통계(statistics) 등이 있다.



##### 수학 관련 함수(math)

* 다음의 기본 함수는 import없이 활용하였다.
  * sum, max, min, abs, pow, round, divmod

* 원주율(pi), 자연상수(e) 를 상수로 활용할 수 있다.
* 사용할 수 있는 연산 관련 함수는 다음과 같다.

| ceil(x)    | floor(x)   | trunc(x)   | copysign(x, y)           | fabs(x)                          | factorial(x)     | fmod(x, y)        | fsum(iterable) | modf(x)            |
| ---------- | ---------- | ---------- | ------------------------ | -------------------------------- | ---------------- | ----------------- | -------------- | ------------------ |
| 소수점올림 | 소수점내림 | 소수점버림 | y의 부호를 x에 적용한 값 | float 절대값 -> 복소수 오류 발생 | 팩토리얼 계산 값 | float 나머지 계산 | float 합       | 소수부 정수부 분리 |

| pow(x, y)    | sqrt(x)         | exp(x)   |     log(x[, base])     |
| ------------ | --------------- | -------- | :--------------------: |
| x의 y승 결과 | x의 제곱근 결과 | e^x 결과 | 밑을 base로 하는 log x |

* 삼각함수
  * sin, cos, tan
  * asin, acos, atan
  * sinh, cosh, tanh
  * ashinh, acosh, atanh



### 3. Errors and Exceptions



##### 문법 에러 (Syntax Error)

* 가장 많이 나는 에러로 `파일이름`과 `줄`, `^`을 통해 파이썬이 읽어들일 때의 문제 발생 위치를 표현한다.

```python
if True:
    print('true')
else
    print('false')
SyntaxError: invalid syntax # -> ":"가 생략됨
```

```python
if True: print('hi
SyntaxError: EOL while scanning string literal # -> 문장이 ' 으로 끝맺어지지 않음
```

```python
if True: print('hi'
SyntaxError: unexpected EOF while parsing # -> 괄호가 안닫힘
```



##### 예외(Exceptions)

* 문법이나 표현식이 바르지만, 발생하는 에러

```python
10 * (1/0)
ZeroDivisionError: division by zero # -> 0으로 나눌 수 없음
```

```python
print(abc)
NameError: name 'abc' is not defined # -> abc는 정의되지 않음
```

```python
1 + '1'
TypeError: unsupported operand type(s) for +: 'int' and 'str'
# -> int와 str을 더하는건 지원되지 않는 기능임
```

```python
round('2.5')
TypeError: type str doesn't define __round__ method
# -> round는 str을 대상으로 적용할 수 없는 method임
```

```python
import random
random.sample([1, 2, 3])
TypeError: sample() missing 1 required positional argument: 'k'
# -> 필수적인 arg가 입력되지 않음
```

```python
random.choice([1, 2, 3], 2)
TypeError: choice() takes 2 positional arguments but 3 were given
# -> 너무 많은 arg가 입력됨
```

```python
int('3.5')
ValueError: invalid literal for int() with base 10: '3.5'
# -> int로 변경할 수 없음 (str임...)
```

```python
a = [1, 2]
a.index(3)
ValueError: 3 is not in list
# -> 리스트에 없는 value임
```

```python
a = []
a[0]
IndexError: list index out of range
# -> 리스트의 인덱스 범위를 벗어남.
```

```python
song = { 'queen': 'sombody to love' }
song['coldplay']
KeyError: 'coldplay'
# -> 없는 key값임
```

```python
import ssafy
ModuleNotFoundError: No module named 'ssafy'
# -> 없는 모듈임
```

```python
from random import ssafy
ImportError: cannot import name 'ssafy'
# -> 모듈 안에 없는 어트리뷰트임
```

```python
ctrl + c 누르면 나옴. (강제 중지)
KeyboardInterrupt
```



##### 예외 처리

* try, except

  ```python
  try:
      codeblock1
  except 예외:
      codeblock2
  ```

  * try절이 실행된다.
  * 예외가 발생되지 않으면, except없이 실행이 종료된다.
  * 예외가 발생하면 남은부분을 수행하지 않고, except가 실행된다.

```python
try:
    num = input('값을 줘: ')  # ; 을 입력하면
    print(int(num))			# 여기서 에러가 발생하고
    print(num)				# 이 단계를 수행하지 않은 상태로
except ValueError:
    print('숫자만')		# except단계를 수행하게 된다.
```



* 복수의 예외 처리

  * 두가지 예외를 모두 처리할 수 있다.

  ```python
  try:
      codeblock1
  except (예외1, 예외2):
      codeblock2
  ```

```python
try:
    num = input('0이 아닌 정수를 입력해: ')
    100 / int(num)
except (ValueError, ZeroDivisionError):  # 한번에 error을 걸러낸다!
    print('ㅡㅡ')
```

```python
try:
    num = input('0이 아닌 정수를 입력해: ')
    100 / int(num)
except ValueError:
    print('정수라고')
except ZeroDivisionError:  # 여러번 except를 사용할 수도 있다!
    print('0말고')
except:
    print('.....?')
```

* 에러가 순차적으로 수행됨으로, 가장 작은 범주부터 시작해야만 한다!!!!!!!!



* 에러 문구 처리
  * 에러 문구를 함께 넘겨줄 수 있다.

  ```python
  try:
      codeblock1
  except 예외 as e:
      codeblock2
  ```

```python
try:
    a = []
    print(a[0])
except IndexError as errmsg:
    print(f'{errmsg}오류입니다. 아마 범위 밖의 index를 넣으셨나봐요 ^^')
# -> list index out of range오류입니다. 아마 범위 밖의 index를 넣으셨나봐요 ^^
```



* else

  * 에러가 발생하지 않는 경우 수행하는 문장은 else를 활용한다.

  ```python
  try:
      codeblock1
  except 예외:
      codeblock2
  else:
      codeblock3
  ```

```python
index = int(input('0, 1, 2 중에 입력'))  # 범위 안에 있는 2를 입력하고
try:
    a = [1, 2, 3]
    b = a[index]   # a에서 인덱스가 2인 값 3을 b의 값으로 받은 후
except IndexError:
    print('index error')  # 에러가 없이 지나가면
else:
    print(f'{index}에 있는 숫자는 {b}입니다.')  # else에서 정상적으로 작동한다.
```



* finally

  * 반드시 수행해야 하는 문장은 finally를 활용한다.

  ```python
  try:
      codeblock1
  except 예외:
      codeblock2
  finally:
      codeblock3
  ```

```python
lang = { 'python': 'dynamic', 'C': 'static' }
try:
    lang['java']  # 자바가 없으니까 keyerror
except KeyError as e:
    print(f'{e} : 딕셔너리에 키가 없어요')  # 그래서 except를 수행하지만
finally:
    print(lang)  # 그래도 finally는 수행함!
    
```



* 예외 발생시키기
  * raise를 통해 예외를 인위적으로 발생시킬 수 있다.

```python
try:
    raise ValueError('ERROOOOOOOOOOR')
except ValueError as e:
    print(f'힘듬..{e}')
```



* assert
  * assert를 통해서도 예외를 발생시킬 수 있다.
  * 상태를 검증하는데 사용되며 무조건 AssertionError가 발생한다
    * assert Boolean expression, error message
  * 위 검증식이 거짓일 경우를 발생한다.
  * raise는 항상 예외를 발생시키지만, assert는 지정한 예외가 발생한다는 점에서 다르다

```python
def my_div(x, y):
    assert type(x) == int and isinstance(y, int), '문자를 입력했네요'
    # -> x, y 둘중 하나라도 int가 아니면 '문자를 입력했네요' 문구를 출력시키며 에러가 발생한다.
    print('나눗셈을 시작합니다.')
    try:
        result = x / y
    except ZeroDivisionError as e:
        print(f'{e}에러가 발생!')
    except TypeError:
        raise ValueError('숫자를 넣어주세요!')
    else:
        return result
```



