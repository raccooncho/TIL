# 190116 summary_OOP



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
class Stack:
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

