# 181218 summary

## 1. 개발 환경 설정



* chocolatey

  * 윈도우 패키지 매니저

* python -v 3.6.7

  * 개발 tool

* googlechrome

  * Browser

* vscode

  * Code Editor

* typora

  * 메모장

* git

  * Version Control System


## 2. List



* Class : str(문자열, string), int(정수, iteger), float(실수), bool(True or False) etc.

* 변수 이름은 뜻을 담아서 짓자!	

  ```python
  numbers = [1, 2, 3]
  ```

* n차원 배열!

  ```python
  mcu = [
      ['Ironman', 'Captain america', 'Dr.strange', 'Hulk', 'Torr'], 
      ['Xmen', 'Deadpool'], 
      ['Spiderman']
      ]
  print(mcu[0][2])
  ```

* 마지막 숫자는 안나옴 (1~45까지 출력됨) / range 클래스가 list 클래스로 변경됨

  ```python
  lotto_numbers = list(range(1, 46))
  ```

* str인 '123'을 int인 123으로 변경해 줌 / True = 1, False = 0

  ```
  int('123')
  ```

* [start:end] => start 는 포함, end 는 포함하지 않음!

  ```
  lotto_numbers[2:5]
  ```

* slicing 하면 list로 추출됨

  ```python
  team = [
      'john', 10000,
      'neo', 100,
      'tak', 40500
  ]
  
  type(team[2:4])
  ```

* list끼리 합치기 가능함

  ```python
  new_member = ['js', 10]
  team = team + new_member
  ```

* 중복되는 문구는 +=으로 대체 가능

  ```python
  team += new_member
  ```

* del을 이용해서 삭제 가능

  ```python
  del(team[-2:])
  ```



## 3. Dictionary



* dict

  ```python
  my_info = {
      'name' : 'neo', 
      'job' : 'hacker',
      'department' : 'development',
      'phone number' : '010 2233 4442',
      'e-mail adress' : 'neo@multi.campus'
  }
  ```

* dict는 보통 list안에 있음

  ```python
  multicampus = [
      {'name' : 'aa',
      'email' : 'aa@aa.a' }
  ]
  ```

* 추출하려면 list랑 비슷한 방법

  ```python
  print(my_info['e-mail adress'])
  print(multicampus[0]['email'])
  ```

* {key : value} 순서임!!!!!!



## 4. Function



### 기본 함수



* print, len, type

  ```python
  print('hi') # 'hi'
  len('hi') # 2
  type('a') # str
  ```

* 최곳값, 최솟값 추출

  ```python
  scores = [45, 60, 78, 88]
  high_score = max(scores) # 최곳값 추출
  lowest_score = min(scores) # 최솟값 추출
  ```

* 반올림

  ```python
  round(1.8) # 반올림
  round(1.876, 2) # (숫자, 소숫점 자릿수) 원하는 자릿수까지 반올림
  ```

* 도움말

  ```python
  help(round) # help로 설명을 요구할 수 있음.
  ```




* sorted (정렬) 함수

  ```python
  first = [11.25, 18.0, 20.0]
  second = [10.75, 9.50] 
  
  full = first + second  #full에 first와 second을 합쳐서 저장
  
  full_sorted = sorted(full)  # full_sorted에 full을 정렬해서 저장
  
  reverse_sorted = sorted(full, reverse = True) # reverse_sorted에 full을 내림차순으로 정렬해서 저장
  ```



### methods 함수



* 특정 요소의 인덱스 확인

  ``` python
  my_list.index(9)
  ```




* list를 뒤집는 방법

  ``` python
  my_list.reverse()
  ```

* list  안에 몇개 있는지 세는 방법

  ```python
  samsung = ['elec', 'sds', 's1']
  samsung.count('s1') # 1개 있음
  ```

* 첫자리를 대문자로 바꾸는 방법

  ```python
  language.capitalize()
  ```

* 중간 문자 찾아서 바꾸기

  ```python
  language.replace('on', 'off') # (A, B) : A라는 문자열이 포함되어있으면 B로 변경함
  ```

* 분류함수 

  ```python
  samsung.sort() # method 함수들은 원본에 변경을 안주지만 sort 같이 원본을 변경하는 함수도 존재함
  ```

* 리스트에 추가하는 방법 

  ```python
  samsung.append('bio') # 얘도 원본 포기함. 리스트에 추가하는 것임
  ```


| str      | int  | list           | bool  | <=Class  |
| -------- | ---- | -------------- | ----- | -------- |
| 'python' | 100  | ['a', 3, True] | False | <=Object |



### import random



```python
import random

numbers = list(range(1, 46))

my_numbers = random.sample(numbers, 6)

print(sorted(my_numbers))
```

로또 번호 6자리 추출하는 함수이다



### import requests



```python
import requests

url = 'https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=837'

response = requests.get(url, verify = False) #"verify=False"는 인증서 요청하지 않음을 위해 삽입한 부분이다.
 
response.text # 원하는 text부분을 얻기 위해 .text를 추가한다 # 이건 class가 str임
response.json() # 이게 dict임 이걸 data라고 부름
lotto_data = response.json()

real_numbers = []

for key in lotto_data:
    if 'drwtNo' in key:
        real_numbers.append(lotto_data[key]) # key 말고 i 같은 다른 문자가 와도 됨
#for key, value in lotto_data.items():
   # if 'drwtNo' in key:
        #real_numbers.appent(value)  # 이런 방법으로도 가능함
        
print(sorted(real_numbers))
```

requests는 기본 내장된 함수가 아니므로 터미널에서 pip install requests를 입력해서 다운받는다.



## git



git init : 초기화

git add . : 버전 추가

git commit -m '할말' : 상태 추가

git push : github.com에 등록

git status : 상태 확인

git log : 등록된거 확인