# 190103 summary_python



## 1. 조건문



#### 		조건문 문법

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



  #### 복수 조건문

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
  
  ```

* 표현식은 보통 조건에 따라 값을 정할 때 많이 활용된다.

  ```python
  
  ```

  ```python
  
  ```

  ```python
  
  ```

  ```python
  
  ```



## 2. 반복문



#### 	while 문

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



  #### for 문

* for 문은 정해진 범위 내에서 순차적으로 코드를 실행한다.

  ```python
  n = range(10)
  for i in n:
      if i < 5:
          print(i)
  print('끝')
  ```

* for 문은 sequence를 순차적으로 variable에 값을 바인딩하며, 코드 블록을 시행한다.

* 예제 : 반복문과 조건문만 활용하여 1~30까지 숫자 중에 홀수만 담긴 리스트를 만드세요.

  ```python
  odd = []
  for i in range(31):
      if i % 2 == 1:
          odd.append(i)
  print(odd)
  ```

* index와 함께 for 문 활용하기

  * enumerate( )를 활용하면 추가적인 변수를 활용할 수 있다.

  ```python
  
  ```

  * enumerate( )는 파이썬 내장함수이다.
    * 열거 객체를 돌려줍니다. iterable은 시퀀스, 이터레이터 또는 이터레이션을 지원하는 다른 객체여야 합니다. neumerate( ) 에 의해 반환된 이터레이터의 ____next___( ) 메서드는 카운트 (기본값 0 을 갖는 start부터)와 iterable을 이터레이션 해서 얻어지는 값을 포함하는 튜플을 돌려줍니다.

  ```python
  
  ```

  ```python
  
  ```

* dictionary 반복문 활용하기
