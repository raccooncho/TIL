# 190114 summary



```
식별자
파이썬에서 식별자는 변수, 함수, 모듈, 클래스 등을 식별하는데 사용되는 이름이다.

식별자의 이름은 영문알파벳, _, 숫자로 구성된다.
첫 글자에 숫자가 올 수 없다.
대소문자를 구별한다.
아래의 예약어는 사용할 수 없다.
False, None, True, and, as, assert, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield
```

```
인코딩 선언
# -*- coding: utf-8 -*-
이건 그냥 손에 익혀놓기
```

```
주석(Comment)
주석은 #으로 표현한다.
docstring은 """으로 표현한다.

: 여러 줄의 주석을 작성할 수 있으며, 보통 함수/클래스 선언 다음에 해당하는 설명을 위해 활용한다.
```

```
코드 라인
기본적으로 파이썬에서는 ; 을 작성하지 않는다.

한 줄로 표기할 떄는 ;를 작성하여 표기할 수 있다
```

- 줄을 여러줄 작성할 때는 역슬래시`\`를 사용하여 아래와 같이 할 수 있다.

```
변수는 =을 통해 할당(assignment) 된다.
해당 자료형을 확인하기 위해서는 type()을 활용한다.
해당 변수의 메모리 주소를 확인하기 위해서는 id()를 활용한다.
```

```
수치형(Numbers)
int (정수)
모든 정수는 int로 표현된다.
파이썬 3.x 버전에서는 long 타입은 없고 모두 int 형으로 표기 된다.
10진수가 아닌 8진수 : 0o/2진수 : 0b /16진수: 0x로도 표현 가능하다.
```

```
float(부동소수점, 실수)
실수는 float로 표현된다.

import sys
abs(a - b) <= sys.float_info.epsilon
sys.float_info.epsilon

import math
math.isclose(a, b)`
```

```
complex (복소수)
복소수는 허수부를 j로 표현한다.
```

```
Bool
파이썬에는 True와 False로 이뤄진 bool 타입이 있다.
비교/논리 연산을 수행 등에서 활용된다.
다음은 False로 변환됩니다.
0, 0.0, (), [], {}, '', None
```

```
None
파이썬에서는 값이 없음을 표현하기 위해 None타입이 존재합니다.
```

```
문자형(String)
문자열은 Single quotes(')나 Double quotes(")을 활용하여 표현 가능하다.
다만 문자열 안에 문장부호(', ")가 활용될 경우 이스케이프 문자(\)를 사용하는 것 대신 활용 가능 합니다.
여러줄에 걸쳐있는 문장은 PEP-8에 따르면 반드시 """를 사용하도록 되어 있습니다.
```

```
String interpolation
1) %-formatting
2) str.format()
3) f-strings : 파이썬 3.6 버전 이후에 지원 되는 사항입니다. ( 이게 제일 편함 )
```

```
연산자
산술연산자 ( + -* / // % ** )
비교연산자 ( > < >= <= == != )
논리연산자 ( and or not)
복합연산자 ( += -= *= /= //= %= **= )
기타연산자 ( concatenation( + ) Containment Test ( in ) Ideneity ( is ) Indexing/Slicing ( [:] ))
```

```
Slide Type
명시적 형변환(Explicit Type Conversion)
위의 상황을 제외하고는 모두 명시적으로 형 변환을 해주어야한다.
string -> intger : 형식에 맞는 숫자만 가능
integer -> string : 모두 가능
암시적 형변환이 되는 모든 경우도 명시적으로 형변환이 가능하다.
int() : string, float를 int로 변환
float() : string, int를 float로 변환
str() : int, float, list, tuple, dictionary를 문자열로 변환
```

```
시퀀스(sequence) 자료형
시퀀스는 데이터의 순서대로 나열된 형식을 나타낸다.
주의! 순서대로 나열된 것이 정렬되었다라는 뜻은 아니다.
파이썬에서 기본적인 시퀀스 타입은 다음과 같다.
리스트(list) : [value1, value2, value3] -> list[i]
튜플(tuple) : (value1, value2) -> 읽기 전용
레인지(range) : 기본형 : range(n)
						0부터 n-1까지 값을 가짐
			   범위 지정 : range(n, m)
						n부터 m-1까지 값을 가짐
			   범위 및 스텝 지정 : range(n, m, s)
						n부터 m-1까지 +s만큼 증가한다
문자열(string)
```

```
시퀀스에서 활용할 수 있는 연산자/함수
( x in s, x not in s, s1 + s2, s*n, s[i], s[i:j], s{i:j:k], len(s), min(s), max(s), s.count(x) )
```

```
set, dictionary
set과 dictionary는 기본적으로 순서가 없습니다.
```

```
set : {value1, value2, value3}
세트는 수학에서의 집합과 동일하게 처리됩니다.
세트는 중괄호{}를 통해 만들며, 순서가 없고 중복된 값이 없습니다.
연산자 / 함수 : ( a-b, a|b, a&b, a.union(b), a.intersection(b) )
```

```
dictionary : {Key1:Value1, Key2:Value2, Key3:Value3, ...}
딕셔너리는 key와 value가 쌍으로 이뤄져있으며, 궁극의 자료구조입니다.
{}를 통해 만들며, dict()로 만들 수도 있습니다.
key는 immutable한 모든 것이 가능하다. (불변값 : string, integer, float, boolean, tuple, range)
value는 list, dictionary를 포함한 모든 것이 가능하다.
```

```
조건문 문법
if 문은 반드시 일정한 참/거짓을 판단할 수 있는 조건식과 함께 사용이 되어야한다. if <조건식>:
2-1. <조건식>이 참인 경우 : 이후의 문장을 수행한다.
2-2. <조건식>이 거짓인 경우 else: 이후의 문장을 수행한다.
이때 반드시 들여쓰기를 유의해야한다. 파이썬에서는 코드 블록을 자바나 C언어의 {}와 달리 들여쓰기로 판단하기 때문이다.
2개 이상의 조건문을 활용할 경우 elif <조건식>:을 활용한다.
```

```
조건 표현식(Conditional Expression) : true_value if <조건식> else false_value
보통 다른 언어에서 활용되는 삼항연산자와 동일하다.
```

```
반복문

while 문
while문은 조건식이 참(True)인 경우 반복적으로 코드를 실행합니다. 
while 문은 종료조건을 반드시 설정해주어야 합니다.

for 문
for문은 정해진 범위 내에서 순차적으로 코드를 실행합니다.
```

```
index와 함께 for문 활용하기
enumerate()를 활용하면, 추가적인 변수를 활용할 수 있다.
enumerate() 는 index와 value를 같이 출력 합니다.
```

```
dictionary 반복문 활용하기
기본적으로 dictionary를 for문을 시행시키면 key값만 출력된다.
dictionary에서 for 활용하는 4가지 방법
# 0. dictionary (key 반복)
for key in dict:
    print(key)
# 1. key 반복
for key in dict.keys():
    print(key)
# 2. value 반복    
for val in dict.values():
    print(val)
# 3. key와 value 반복
for key, val in dict.items():
    print(key, val)
```

```
break
break문은 반복문을 종료하는 표현입니다.
```

```
continue
continue문은 continue 이후의 코드를 수행하지 않고 다음 요소를 선택해 반복을 계속 수행합니다.
```

```
else
else문은 끝까지 반복문을 시행한 이후에 실행됩니다.
(break를 통해 중간에 종료되지 않은 경우만 실행)
```

```
함수
def func(parameter1, parameter2):
    code line1
    code line2
    return value
함수 선언은 def로 시작하여 :으로 끝나고, 다음은 4spaces 들여쓰기로 코드 블록을 만듭니다.
함수는 매개변수(parameter)를 넘겨줄 수도 있습니다.
함수는 동작후에 return을 통해 결과값을 전달 할 수도 있습니다.
(return 값이 없으면, None을 반환합니다.)
```

```
함수의 return
앞서 설명한 것과 마찬가지로 함수는 반환되는 값이 있으며, 이는 어떠한 종류의 객체여도 상관없습니다.
단, 오직 한 개의 객체만 반환됩니다.
함수가 return 되거나 종료되면, 함수를 호출한 곳으로 돌아갑니다.
```

```
기본 값(Default Argument Values)
함수가 호출될 때, 인자를 지정하지 않아도 기본 값을 설정할 수 있습니다.
def func(p1=v1):
    return p1
=> p1의 default == v1
```

```
키워드 인자(Keyword Arguments)
키워드 인자는 직접적으로 변수의 이름으로 특정 인자를 전달할 수 있습니다
def greeting(age, name='ssafy'):
    return f'{name}은 {age}살 입니다.'
단, 키워드 인자를 활용한 뒤에 위치 인자를 활용할 수는 없습니다.   
```

```
가변 인자 리스트 : def func(*agrs):
앞서 설명한 print()처럼 정해지지 않은 임의의 숫자의 인자를 받기 위해서는 가변인자를 활용합니다.
가변인자는 tuple 형태로 처리가 되며, *로 표현합니다.
```

````
정의되지 않은 인자 처리하기
**kwagrs를 통해 인자를 받아 처리할 수 있습니다.
kwagrs는 dict형태로 처리가 됩니다.
````

```
Slide Type
dictionary를 인자로 넘기기(unpacking arguments list)
**dict를 통해 함수에 인자를 넘길 수 있습니다.
```

```
이름공간 및 스코프(Scope)
파이썬에서 사용되는 이름들은 이름공간(namespce)에 저장되어 있습니다. 그리고, LEGB Rule을 가지고 있습니다.
변수에서 값을 찾을 때 아래와 같은 순서대로 이름을 찾아나갑니다.
Local scope: 정의된 함수
Enclosed scope: 상위 함수
Global scope: 함수 밖의 변수 혹은 import된 모듈
Built-in scope: 파이썬안에 내장되어 있는 함수 또는 속성
```

