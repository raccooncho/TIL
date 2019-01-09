# 181221 수업정리



## 1. html in c9 using FLASK



### render_template 이용하기



* html 을 이용하기 위해선 render_template를 import해와야 한다.

```python
from flask import Flask, jsonify, render_template
```



* "templates"라는 이름으로 폴더를 형성한다 (반드시 templates라는 이름을 지켜야 한다.)


* 그 밑에 introduction.html이라는 파일을 형성하고 app.py에서

```python
@app.route('/raccooncho')
def raccoon():
    return render_template('introduction.html')
```

​	을 입력하면 https://startcamp-raccooncho-1.c9users.io/raccooncho 라는 url이 형성된다



* 이렇게 형성한 html 파일은 html형식을 유지해서 작성하면 된다.

* 유동적으로 변하는 url도 형성할 수 있다.

```python
@app.route("/get_number/<string:username>/<string:number>")
def get_number(username,number):
    return "{}'s number is {}".format(username,number)
```

​	이렇게 <string: >과 format 을 이용하면 입력하는 값이 url에 출력된다.



### 매번 $flask run -h 0.0.0.0 -p 8080을 입력하기 귀찮을 때

```python
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
```

​	을 **파일 맨 밑**에 작성하면 $python3 app.py로 간단하게 url을 작동할 수 있다.
​	(반드시 맨 아래에 작성해야 다른 함수와 충돌을 일으키지 않는다.)



### 한글관련 오류가 발생할 시 

* app.py 맨 위에 

  ```python
   -*- coding: utf-8 -*-
  ```

  을 입력하면 한글 충돌이 사라진다고 한다. (나는 이 코드가 오류를 일으켜서 ..... )



### Input form

```html
<form action="/aa">  # form으로 가방안에 집어 넣는다. # action으로 보낼곳을 지정한다
    <input type="text" placeholder="ohhh"/>  # 제일 많이 씀 # 그림자처럼 보이는 문구 (다른 문자 입력하면 사라짐)
    <input type="color" />  # 색 선택 창이 나옴
    <input type="submit" value="submit" />  # 제출 버튼이 됨 # value를 이용해서 버튼에 나올 문구를 선택할 수 있음
    <input type="date" />  # 날짜 선택 창이 나옴
    <input type="email" />  # 이메일 검새...ㄱ?
</form>
```





## 2. Chat_bot 퀘스트

* 텔레그램 회원가입을 한다

* 텔레그램 web버전에서 botfather을 찾아서 봇을 만든다

* https://api.telegram.org/bot<key>/getUpdates  # key를 제공받아서 확인한다 
  => 입력하는 내용이 출력된다

* https://api.telegram.org/bot<key>/sendMessage?chat_id=<chat_id>&text=<원하는 말>
  => 봇의 말이 출력된다

  ```python
  import requests
  import random
  
  MY_CHAT_ID = '751345255'
  BOT_TOKEN = '714587754:AAFFrK6l_ShZurmHQAO2doSGjB15Om5x3CI'
  msg = 'helloraccooncho'
  
  url = 'https://api.hphk.io/telegram/bot{}/sendMessage?chat_id={}&text={}'.format(BOT_TOKEN, MY_CHAT_ID, msg)
  # 원래는 https://api.telegram.org/bot~~로 입력해야 하지만 c9과 telegram은 연동이 되지 않으므로 우회 경로로 api.hphk.io/telegram/bot~~을 입력하면 된다
  
  response = requests.get(url)
  print(response.json())
  ```

  ```python
  @app.route('/amilucky')
  def amilucky():
      rounds = request.args.get('rounds')
      my_numbers = pick_lotto()
      WYL = am_i_lucky(my_numbers, int(rounds))
      MY_CHAT_ID = '751345255'
      BOT_TOKEN = '714587754:AAFFrK6l_ShZurmHQAO2doSGjB15Om5x3CI'
      result = ("추첨 번호는", WYL[0], "입니다.", WYL[1], "회차 당첨 번호는", WYL[2], "입니다. 맞춘 갯수는", WYL[4], "개 입니다. 당신은", WYL[5], "입니다.") # 이거 result가 
      url = 'https://api.hphk.io/telegram/bot{}/sendMessage?chat_id={}&text={}'.format(BOT_TOKEN, MY_CHAT_ID, result) # 여기 result로 와야 합니다.
  
      response = requests.get(url)
      
      return render_template('amilucky.html', pick_num=WYL[0], real_num=WYL[2], bonus_num=WYL[3], match_num=WYL[4], result=WYL[5], rounds=rounds)
  
  ```
