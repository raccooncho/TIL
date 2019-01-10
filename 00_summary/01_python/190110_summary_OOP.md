# 190110 summary_python



### 1. OOP intro

##### 들어가기 전에...

* 클래스(Class) - 같은 종류(또는 문제 해결을 위한)의 집단에 속하는 속성(attribute)과 행위(behavior)를 정의한 것으로 객체지향 프로그램의 기본적인 사용자 정의 데이터형(user define data type)이라고 할 수 있다. 클래스는 프로그래머가 아니지만 해결해야 할 문제가 속하는 영역에 종사하는 사람이라면 사용할 수 있고, 다른 클래스 또는 외부 요소와 독립적으로 디자인하여야 한다.

* 인스턴스 - 클래스의 인스턴스(실제로 메모리상에 할당된 것)이다. 객체는 자신 고유의 속성(attribute)을 가지며 클래스에서 정의한 행위(behavior)를 수행할 수 있다. 객체의 행위는 클래스에 정의된 행위에 대한 정의를 공유함으로써 메모리를 경제적으로 사용한다.

* 메서드(Method) - 클래스로부터 생성된 객체를 사용하는 방법으로서 **객체에 명령을 내리는 것**이라 할 수 있다. 메서드는 한 객체의 속성을 조작하는 데 사용된다.

...그런듯...

```python
# 복소수를 하나 만들어보고, 타입을 출력해봅시다.
img_number = 3 + 4j
print(type(img_number))  # <class 'complex'>

# 허수부랑 실수부를 함께 출력해봅시다.
print(img_number.real)  # 3.0
print(img_number.imag)  # 4.0
```

```python
# 리스트를 하나 만들고 정렬해봅시다.
a = [3, 2, 1]
a.sort()
print(a)  [1, 2, 3]
```

```python
# list class가 할 수 있는 것들을 알아봅시다.
print(dir(list))
# ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
```



##### 예제

> 프로그래밍으로 나와 친구의 이름을 저장해보세요.

* 각자의 명함과 지갑을 만들어봅시다.
  * 내 생일, 전화번호, 이메일 주소 정보를 담은 변수를 확인해 봅시다.
  * 주머니에는 돈을 포함하여 현재 가지고 있는 것을 작성해 보세요.
  * 나는 인사를 하면서 내 명함에 있는 정보를 이야기 합니다. `greeting` 함수를 만듭시다.
  * 나는 주머니에 원하는 것과 갯수를 지정하여 넣을 수 있습니다.
    * 기존에 값이 있으면, 갯수를 추가하고 없으면 새로 만드는  `in_my_pocket` 함수를 만듭시다.

```python
my_info = {
    'name': '조성규',
    'phone': '01098559017',
    'email': 'wjtjdrb@naver.com'
}
my_pocket = {
    'money' : 4000,
    'card' : 3,
    'id_card' : 2,
    'trash' : 'a lot',
}

def greeting(info):
    return f" Hi, my name is {info['name']} my phone number is {info['phone']} and email adress is {info['email']} "
    
def in_my_pocket(pocket, stuff, count):
    if pocket.get(stuff):
        pocket[stuff] += count
    else:
        pocket[stuff] = count
    return pocket
```

```python
def info_add(name, birthday, phone, bloodtype, getup, sleep):
    info = {}
    info['name'] = name
    info['birthday'] = birthday
    info['phone'] = phone
    info['bloodtype'] = bloodtype
    info['getup'] = getup
    info['sleep'] = sleep
    return info

csk = info_add('조성규', '920527', '01098559017', 'AB', '알람끄기', '유산균먹기')
pcm = info_add('박찬미', '910604', '01052953958', 'A', '물마시기', '미드보기')
jsh = info_add('지상현', '950912', '01050242683', 'O', '거울보기', '스트레칭')

mates = {
    'cho': csk,
    'park': pcm,
    'ji': jsh
}

# 친구의 정보 입력
```

```python
class Mate:  # class를 이용한 입력  # 앞글자가 대문자인건 컨벤션임 지켜줍시다.
    
    def set_info(self, name, birthday, phone, blood, getup, sleep):  # self가 계속 들어감..
        self.name = name
        self.birthday = birthday
        self.phone = phone
        self.blood = blood
        self.getup = getup
        self.sleep = sleep
    def get_info(self):  # 여기도 self
        print(self.name, self.birthday, self.phone, self.blood, self.getup, self.sleep)
    def before_sleep(self):  # 저기도 self
        print(f'{self.name}는 자기전에 {self.sleep}를 합니다.')
    
    
cho = Mate()
cho.set_info('조성규', '920527', '01098559017', 'AB', '알람끄기', '유산균먹기')
cho.get_info()
cho.before_sleep()  # 조성규는 자기전에 유산균먹기를 합니다.
```

는 사실 set_info 는 필요 없다는 것...

```python
class Mate:
    def __init__(self, name, birthday, phone, blood, getup, sleep):  # init을 합시다.
        self.name = name
        self.birthday = birthday
        self.phone = phone
        self.blood = blood
        self.getup = getup
        self.sleep = sleep
    def get_info(self):
        print(self.name, self.birthday, self.phone, self.blood, self.getup, self.sleep)
    def before_sleep(self):
        print(f'{self.name}는 자기전에 {self.sleep}를 합니다.')
    
    
cho = Mate('조성규', '920527', '01098559017', 'AB', '알람끄기', '유산균먹기')
cho.get_info()
cho.before_sleep()
```

이런식으로 쓰면 됨/

```python
class Text:
    def __init__(self, content):
        self.content = content
    def view_all(self):
        print(content)
    def is_palindrome(self):
        txt = self.content.replace(' ', '').lower()
        return txt == ''.join(reversed(txt))
    def start_hangman(self):
        guess = input('한글자만 넣어라 : ')
        if guess in self.content:
            print('오!맞음')
        else:
            print('ㅅㄱ')
    
        
my_text = Text('A santa at NASA')

print(my_text.is_palindrome())

your_text = Text('apple')
your_text.start_hangman()
```



### 2. 클래스 및 인스턴스

##### 클래스 객체

```python
class ClassName:  # `-`언더바를 사용해야 할 경우 대신 대문자를 씁니다.
```

* 선언과 동시에 클래스 객체가 생성됨.
* 선언된 공간은 지역 스코프로 사용된다.
* 정의된 어트리뷰트 중 변수는 멤버 변수로 불린다.
* 정의된 함수(`def`)는 메서드로 불린다.

```python
# Class를 만들어봅시다.
class TestClass:
    """This is Test Class"""
print(type(TestClass))  # <class 'type'>

tc = TestClass()
print(type(tc))  # <class '__main__.TestClass'>
print(tc.__doc__.)  # This is Test Class -> 설명을 읽을 수 있음.
```

```python
# Person 클래스를 만들어봅시다.
class Person:
    name = '홍길동'
    
    def say_hi(self):
        print('HELLO!')
    def intro(self):
        print(f'I am {name}')
        
p = Person()
p.say_hi()  # HELLO!
p.name  # return '홍길동' -> class의 모든 요소에 적용할 값이다.
```

* 선언 시 self는 반드시 작성!



##### 인스턴스 객체

* 인스턴스 객체는 `ClassName()`을 호출함으로써 선언된다.
* 인스턴스 객체와 클래스 객체는 서로 다른 이름 공간을 가지고 있다.
* 인스턴스 -> 클래스 -> 전역 순으로 탐색을 한다.

```python
# iu라는 클래스 Person의 인스턴스를 만들어봅시다. 
iu = Person()
# iu의 이름을 확인해봅시다.
iu.name  # 홍길동 - > Person의 모든 요소는 name:홍길동이 적용된 상태임
# iu로 이름을 바꿔주세요.
iu.name = 'IU'
print(iu.name)  # IU -> 개별로 변경할 수 있음.
```

```python
# iu가 인사를 합니다.
iu.intro()  # name 'name' is not defined
# class Person:의 intro를 정의하는 부분에서 name를 self.name로 변경하면 됨
class Person:
    name = '홍길동'  
    def intro(self):
        print(f'I am {self.name}')
iu = Person()
iu.intro()  # I am IU -> 잘됨
```

```python
# iu와 Person이 같은지 확인해보겠습니다.
isinstance(iu, Person)  # True
isinstance('a', str)  # True -> 이런식으로 isinstance를 사용해서 생각하는 type이 맞는지 확인할 수 있음.
type(iu) == Person  # True
```

```python
# iu를 출력해봅시다.
print(iu)  # <__main__.Person object at 0x000001F509CC50F0>
iu  # <__main__.Person at 0x1f509cc50f0>
# 메모리 상 어딘가에 고정됨
```

```python
# type을 확인해봅시다.
type(iu)  # __main__.Person
```

* 파이썬 출력의 비밀 : repr, str



##### 실습문제 발전

> 자유롭게 만들어 보세요. -> 포켓몬스터 게임

```python
# 아래에 코드를 작성해주세요.
class Pokemon:
    
    def __init__(self, name, level, element):
        elements = ['elec', 'water', 'fire', 'leef']
        element_attacks = ['10만볼트', '물대포', '화염방사', '잎날가르기']
        self.name = name
        self.level = level
        self.HP = level * 10
        self.vapp = 5
        self.speed = level * 2
        self.element = elements.index(element)
        self.e_attack = element_attacks[self.element]
    def set_HP(self, point):
        self.HP += point
    def check_status(self):
        if self.HP <= 0:
            return False
        else:
            return self.HP
    def body_attack(self, enemy):
        enemy.set_HP(-self.level)
        print(f'{self.name}가 {enemy.name}에게 몸통박치기를 시도하였다.')
        print(f'{self.level}의 데미지를 주었다.')
    def element_attack(self, enemy):
        if self.element == enemy.element + 1:
            if self.vapp > 0:
                print(f'{self.name}가 {enemy.name}에게 {self.e_attack}를 시도하였다.')
                print(f'효과가 부족했다.')
                print(f'{self.level * 1}의 데미지를 주었다.')
                print(f'{self.name}의 스피드가 1 떨어졌다.')
                self.speed -= 1
                enemy.set_HP(-self.level * 1)
                self.vapp -= 1
            else:
                print(f'{self.name}는 pp가 부족하여 더 이상 {self.e_attack}를 사용할 수 없다.')
                print(f'대신 몸통 박치기를 하였다.')
                enemy.set_HP(-self.level)
                print(f'{self.level}의 데미지를 주었다.')
        elif self.element == enemy.element - 1:
            if self.vapp > 0:
                print(f'{self.name}가 {enemy.name}에게 {self.e_attack}를 시도하였다.')
                print('효과가 굉장했다.')
                print(f'{self.level * 4}의 데미지를 주었다.')
                print(f'{self.name}의 스피드가 1 떨어졌다.')
                self.speed -= 1
                enemy.set_HP(-self.level * 4)
                self.vapp -= 1
            else:
                print(f'{self.name}는 pp가 부족하여 더 이상 {self.e_attack}를 사용할 수 없다.')
                print(f'대신 몸통 박치기를 하였다.')
                enemy.set_HP(-self.level)
                print(f'{self.level}의 데미지를 주었다.')
        else:
            if self.vapp > 0:
                print(f'{self.name}가 {self.enemy.name}에게 {self.e_attack}를 시도하였다.')
                print(f'{self.level * 2}의 데미지를 주었다.')
                print(f'{self.name}의 스피드가 1 떨어졌다.')
                self.speed -= 1
                enemy.set_HP(-self.level * 2)
                self.vapp -= 1
            else:
                print(f'{self.name}는 pp가 부족하여 더 이상 {self.e_attack}를 사용할 수 없다.')
                print(f'대신 몸통 박치기를 하였다.')
                enemy.set_HP(-self.level)
                print(f'{self.level}의 데미지를 주었다.')

    
    
    
    
    
a = Pokemon('피카츄', 5, 'elec')
b = Pokemon('꼬북이', 15, 'water')

import random

while a.check_status() and b.check_status():
    if a.speed > b.speed:
        aattack = random.choice([1, 2])
        if aattack == 1:
            a.body_attack(b)
        else:
            a.element_attack(b)
        print(f'{b.name}의 체력이 {b.HP} 남았다.\n')
        if b.check_status() == False:
            break
        battack = random.choice([1, 2])
        if battack == 1:
            b.body_attack(a)
        else:
            b.element_attack(a)
        print(f'{a.name}의 체력이 {a.HP} 남았다.\n')
    elif a.speed == b.speed:
        order = random.choice([1, 2])
        if order == 1:
            aattack = random.choice([1, 2])
            if aattack == 1:
                a.body_attack(b)
            else:
                a.element_attack(b)
            print(f'{b.name}의 체력이 {b.HP} 남았다.\n')
            if b.check_status() == False:
                break
            battack = random.choice([1, 2])
            if battack == 1:
                b.body_attack(a)
            else:
                b.element_attack(a)
            print(f'{a.name}의 체력이 {a.HP} 남았다.\n')
        else:
            battack = random.choice([1, 2])
            if battack == 1:
                b.body_attack(a)
            else:
                b.element_attack(a)
            print(f'{a.name}의 체력이 {a.HP} 남았다.\n')
            if a.check_status() == False:
                break
            aattack = random.choice([1, 2])
            if aattack == 1:
                a.body_attack(b)
            else:
                a.element_attack(b) 
            print(f'{b.name}의 체력이 {b.HP} 남았다.\n')
    else:
        battack = random.choice([1, 2])
        if battack == 1:
            b.body_attack(a)
        else:
            b.element_attack(a)
        print(f'{a.name}의 체력이 {a.HP} 남았다.\n')
        if a.check_status() == False:
            break
        aattack = random.choice([1, 2])
        if aattack == 1:
            a.body_attack(b)
        else:
            a.element_attack(b)
        print(f'{b.name}의 체력이 {b.HP} 남았다.\n')
if a.check_status() == False:
    print(f'{a.name}는 더이상 싸울 힘이 없다.')
    print(f'{b.name}이 전투에서 이기고 {a.level}의 경험치를 획득하였다!!')
else:
    print(f'{b.name}는 더이상 싸울 힘이 없다.')
    print(f'{a.name}이 전투에서 이기고 {b.level}의 경험치를 획득하였다!!')
```



### 0. 아침 문제풀이 

* quiz 1 : Hangman

  * 단어를 맞추는 문제를 만드세요!
  * 필요한 함수들

  ```python
  def is_answer(answer, letters):  # 답이 맞는지 알려주는 함수  # 교수님 예시
      sanswer = set(answer)
      count = 0
      for a in letters:
          if set(a) & sanswer:
              count += 1
      return len(sanswer) == count
  ```

  ```python
  def status(answer, letters):  # 오답을 _로 바꿔주는 함수 # 교수님 예시
      for char in answer:
          if char not in letters:
              answer = answer.replace(char, ' _ ')
      return answer
  ```

  * 내가 사용하게 바꾼 함수

  ```python
  def is_answer(answer, letters):
      answer = [x for x in answer]  # str을 list에 쪼개서 넣음.
      sanswer = set(answer)  # count가 있으면 오류가 나는거 같아서 없앰
      for a in letters:
          if set(a) & sanswer:
              sanswer -= set(a)
      if sanswer:
          return False
      else: 
          return True
  ```

  ```python
  def status(answer, letters):
      answer = (' ').join(answer).split()  # 리스트로 바꿔준 후
      for a in answer:
          if a not in letters:
              i = answer.index(a)  # 아닌 문자의 인덱스를 찾아서
              answer.insert(i, '_')  # _를 입력하고
              answer.remove(a)  # 삭제함
      for l in letters:
          if l not in answer:
              answer = ['오답입니다.']  # 만약 정답에 해당하지 않는 문자가 있으면 오답을 출력
      return (' ').join(answer)
  ```

  * Hangman 로직 만들기
    * 위의 코드를 활용하여 `hangman(answer)`를 만들자!
    * 사용자가 답을 맞추거나, 시도가 8번을 넘어가면 종료!

```python
def hangman(answer, n=8, h=5):  # n은 시도 횟수 제한  # h는 목숨 제한
    input_letter = []
    count = 1  # 시도 횟수
    count_heart = 0  # 목숨
    while count != n+1 and count_heart != h:
        if count == n:
            my_answer = input(f'마지막 시도입니다. 신중하게 입력하세요 : ')
        else:
            my_answer = input(f'{count}번째 시도입니다. 단어를 입력하세요 : ')
        if len(my_answer) != 1:
            print('\n한 글자만 입력해 주세요!\n')
        else:
            count += 1
            if status(answer, my_answer) == '오답입니다.':
                count_heart += 1
            else:
                input_letter.append(my_answer)
                if is_answer(answer, input_letter):
                    return f'\n정답은 {answer} 입니다! {count-1}번 만에 성공하셨어요!'
            print('\n', ' ♥ '*(h-count_heart), '♡ '*(count_heart), '\n')
            print(status(answer, input_letter), '\n')
    if count == n+1:
        return f'정답은 {answer}입니다. {n}번의 도전기회를 모두 소모하셨군요. 가망이 없어요!' 
    else:
        return f'정답은 {answer}입니다. {count_heart}개의 목숨을 모두 소진하셨습니다. 포기하세요!'
```



```python
def hangman(answer):  # 교수님 답  # 새 list를 만들고 거기에 정답인 알파벳을 추가하는식..
    input_letters = []
    attempt = 8
    print('===START===')
    while 1:
        print(f"남은 목숨: {'♥' * attempt}")
        print(status(answer, input_letters))
        
        guess = input('알파벳을 입력하세요: ').lower()
        input_letters.append(guess)
              
        if is_answer(answer, input_letters):
              return '성공'
        else:
              attempt -= 1
        if not attempt:
              return '실패'
            
```





### 
