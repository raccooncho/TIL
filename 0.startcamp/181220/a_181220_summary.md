# 181220 수업정리



## 0. HTML





* HTML = Hyper Text **Markup** Language

* 결과론적인 시각보다는 원인을 더 먼저 보려고 하자



## 1. 아침 로또



* 일반적인 언어의 정답 추론 과정

```python
count = 0   # 교수님 정답 1
for my_number in my_numbers:
    for real_number in real_numbers:
        if my_number == real_number:
            count += 1
print(count)

if count == 6:
    print(1)
elif count == 5 and bonus in my_numbers:
    print(2)
elif count == 5:
    print(3)
```



* 파이썬용 정답 (set기능 이용)

```python
match_count = len(my_numbers & real_numbers) # 교수님 정답 2
print(match_count)

if match_count == 6:
    print('1등')
elif match_count == 5 and bonus in my_numbers:
    print('2등')
```



### set 기능



* 파이썬에는 set기능도 있다

```python
list = [1, 2, 3]
set = {1, 2, 3}
tuple = (1, 2, 3)
```



* 교집합

```python
s1 = {1, 2, 3}
s2 = {3, 4, 5}
intersection = s1.intersection(s2)
or
intersection = s1 & s2
```



* 차집합

```python
s1 = {1, 2, 3}
s2 = {3, 4, 5}
difference = s1.difference(s2)
or
difference = s1 - s2
```



* 합집합

```python
s1 = {1, 2, 3}
s2 = {3, 4, 5}
union = s1.union(s2)
or 
union = s1|s2
```



## 2. 함수 정의



* pick_lotto 함수 정의하기

```python
def pick_lotto():
    numbers = set(random.sample(range(1, 46), 6))
    return numbers   # 이걸 안하면 함수가 None을 출력함. 없어도 동작할수는 있음.


my_numbers = pick_lotto()
print(my_numbers)
```

```python
print(pick_lotto()) # 이렇게 출력해 보면
[24, 41, 13, 32, 12, 28] # 이렇게 리스트 형식으로 출력함
```





* return in def:

```python
a = sorted([1,2,3])
b = [3,2,1].sort()

print(a,b)
then
[1,2,3] None

because
	sorted() 함수는 return을 포함하고 있고
	.sort() 함수는 return을 포함하지 않고 있음.
```



* get_lotto(num) 함수 정의하기

```python
def get_lotto(draw_no):  # num 은 int이므로 str로 변경해줘야 url로 읽을 수 있음
    url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo='+str(draw_no)
    response = requests.get(url, verify = False) #verify = False는 인증서 오류 사라지면 삭제
    lotto_data = response.json()
    numbers = []
    for key, value in lotto_data.items():
        if 'drwtNo' in key:
            numbers.append(value)
    numbers.sort()
    bonus_number = lotto_data['bnusNo']
    final_dict = { 
        "numbers": numbers,
         'bonus': bonus_number
         }
    return final_dict
```

```python
print(get_lotto(836)) # 이렇게 836회 번호를 검색하면
{'numbers': [1, 9, 11, 14, 26, 28], 'bonus': 19} # 이렇게 dict 항목으로 나타남
```



* am_i_lucky(a, b) 함수 정의하기

```python
def am_i_lucky(pick_num, draw_no):
    real_num = get_lotto(draw_no) # get_lotto 함수를 내장해서 회차정보를 획득할수 있다.
    match_number = len(set(pick_num) & set(real_num['numbers']))
    print("당신의 번호는", pick_num, "입니다.")
    print(draw_no, "회차의 당첨 번호는", real_num['numbers'], "이고,")
    print("2등 보너스 번호는", real_num['bonus'], "입니다")
    print("맞은 갯수는", match_number, "개 입니다.")
    if match_number == 6:
        print("당신은 1등입니다")
    elif match_number == 5 and bonus in pick_num:
        print("당신은 2등입니다")
    elif match_number == 5:
        print("당신은 3등입니다")
    elif match_number == 4:
        print("당신은 4등입니다")
    elif match_number == 3:
        print("당신은 5등입니다")
    else:
        print("당신은 꼴등입니다")
```

```python
am_i_lucky(pick_lotto(), get_lotto(1)) # 이걸로 1회차 로또 번호를 요청하면 / # print() 함수가 am_i_lucky()함수 안에 내장되어 있음 # print 함수를 따로 또 적용하면 맨 아래에 None이 같이 출력됨
당신의 번호는 [36, 22, 29, 17, 15, 6] 입니다.
1 회차의 당첨 번호는 [10, 23, 29, 33, 37, 40] 이고,
2등 보너스 번호는 16 입니다
맞은 갯수는 1 개 입니다.
당신은 꼴등입니다
# 로 출력 된다. 어김없이 꼴등 ㅎㅎ
```



* am_i_lucky(a,b) 함수 수정한 것 (print를 return으로 수정) # print는 (주로)디버깅 체크용으로만 쓰임

```python
def am_i_lucky(pick_num, draw_no): # 가능하면 print를 함수 안에 넣지 말기!
    real_num = get_lotto(draw_no)
    match_number = len(set(pick_num) & set(real_num['numbers']))
    if match_number == 6:
        return(pick_num, draw_no, real_num['numbers'], real_num['bonus'], match_number, '1등')
    elif match_number == 5 and bonus in pick_num:
        return(pick_num, draw_no, real_num['numbers'], real_num['bonus'], match_number, '2등')
    elif match_number == 5:
        return(pick_num, draw_no, real_num['numbers'], real_num['bonus'], match_number, '3등')
    elif match_number == 4:
        return(pick_num, draw_no, real_num['numbers'], real_num['bonus'], match_number, '4등')
    elif match_number == 3:
        return(pick_num, draw_no, real_num['numbers'], real_num['bonus'], match_number, '5등')
    else:
        return(pick_num, draw_no, real_num['numbers'], real_num['bonus'], match_number, '꼴등')
```

```python
WYL = am_i_lucky(pick_lotto(), 10)
print(" 당신의 번호는", WYL[0], "입니다.\n", WYL[1], "회차의 당첨 번호는", WYL[2], "이고,\n", 
        "2등 보너스 번호는", WYL[3], "입니다.\n", "맞은 갯수는", WYL[4], "개 입니다.\n", "당신은", WYL[5], "입니다.") # 이렇게 출력 하면
 당신의 번호는 [21, 18, 19, 1, 42, 7] 입니다.
 10 회차의 당첨 번호는 [9, 25, 30, 33, 41, 44] 이고,
 2등 보너스 번호는 6 입니다.
 맞은 갯수는 0 개 입니다.
 당신은 꼴등 입니다. # 이렇게 출력 된다.
```



* arg

```python
real_numbers = get_lotto(3) # 3에 들어가는 부분은 arg (arguments)로 부름
```



## 3. 함수 import

### math_functions 파일을 형성한다

```python
def avg(numbers):
    return sum(numbers) / len(numbers)

def cube(x):
    return x * x * x

my_score = [79, 84, 66, 93]
print(avg(my_score))
print(cube(3))
print(3 ** 3)
```

### 이걸 do_math 파일에 import하면

```python
print('program start!')
print('--------------------')
import math_functions
print('importing finished') # 어디서 import됬는지 확인하기 위한 용도로 임시로 해봤다.

print(math_functions.cube(5))
print(math_functions.avg([10, 20, 30]))
```

```python
program start!
--------------------
80.5
27                    # import 된 파일의 print 내용도 같이 가져왔다
27
importing finished
125                   # 여기부터 본래 파일이 진행된다.
20.0
```

### 그래서 함수만 import하면

```python
print('program start!')
print('--------------------')
from math_functions import cube, avg
print('importing finished')

print(cube(5))
print(avg([10, 20, 30]))
```

```python
program start!
--------------------
80.5
27
27
importing finished
125
20.0
```

그래도 import한 함수의 내용이 같이 딸려 온다.

### 그럼 math_functions 파일에 새로운 함수를 지정해서 print될 내용을 삽입한다

```python
def main():
    my_score = [79, 84, 66, 93]
    print(avg(my_score))
    print(cube(3))
    print(3 ** 3)

if __name__ == '__main__':     # ...?
    main()
```

then,

```python
program start!
--------------------
importing finished
125
20.0
```

원하는 것만 출력 된다.

## 4. Flask

* installing Flask
  * $pip3 install flask

  * 안되면 $sudo pip3 install flask (sudo는 최고 관리자 명령어)

  * $export FLASK_APP=app.py (app.py는 생성한 파일 명)

  * from flask import Flask

  * app = Flask(__name__)

  * @app.route("/")

  * def index():

    ​	return 'Happy Hacking'

  * $flask run -h 0.0.0.0 -p 8080

  * http://0.0.0.0:8080/ 누르면 새 url이 됨

  * $export FLASK_ENV='development'

  * $python3 app.py

  ```python
  from flask import Flask, jsonify # jsonify는 list나 dict의 호환성을 높여줌
  from random import sample
  app = Flask(__name__)
  
  @app.route("/")  # 새 주소 추가하는 용도
  def index():
      return 'Happy Hacking'
      
  @app.route("/hi")
  def hi():
      return 'Hello SSAFY'
      
  @app.route('/pick_lotto')
  def pick_lotto():
      return jsonify(sorted(sample(range(1, 46), 6)))
      
  @app.route('/get_lotto')
  def get_lotto():
      data = {
          'numbers': [1, 2, 3, 4, 5, 6],
          'bonus': 7
      }
      return jsonify(data)
  ```


