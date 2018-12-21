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

