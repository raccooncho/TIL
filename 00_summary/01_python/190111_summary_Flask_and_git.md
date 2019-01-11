# 190111 summary_python



### 1. Flask

##### 더이상 쥬피터 노트북을 사용할 수 없으므로 새 directory를 만듭시다.

* cd til -> mkdir 04_flask -> cd 04_flask -> mkdir first_app -> cd first_app -> touch app.py
* pip -V 로 버전을 확인한 후 최신버전 (다른 말이 안뜨면 최신버전임)이라면 pip install flask로 flask를 다운 받는다.
* code . 으로 현재 위치에서 vscode를 실행한다.

##### from flask import Flask

* flask로 부터 Flask class를 받아온다.

```python
from flask import Flask

app = Flask(__name__)

@app.route('/') 
def index():
    return 'Hi'

if __name__ == '__main__':  # 항상 최하단에 존재해야 함.
    app.run()
```

* $python app.py로 실행하면

```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [11/Jan/2019 09:33:07] "GET / HTTP/1.1" 200 -  # 접속자가 들어옴
127.0.0.1 - - [11/Jan/2019 09:33:07] "GET /favicon.ico HTTP/1.1" 404 -
127.0.0.1 - - [11/Jan/2019 09:36:14] "GET /1 HTTP/1.1" 404 -  # /1은 없는 사이트
127.0.0.1 - - [11/Jan/2019 09:36:46] "GET /ssafy HTTP/1.1" 404 -  # /ssafy은 없는 사이트
127.0.0.1 - - [11/Jan/2019 09:37:54] "GET /ssafy HTTP/1.1" 404 -
127.0.0.1 - - [11/Jan/2019 09:37:56] "GET /ssafy HTTP/1.1" 404 -
```

* 200은 True고 404는 False

```python
if __name__ == '__main__':
    app.run(debug=True)  # app.run 에서 debug를 True로 정해주면 debug mode가 on이 되면서 파일을 수정 및 저장하는 내용이 실시간으로 사이트에 적용됨.
    app.run(debug=True, host=0.0.0.0, port=3000)
    # 이렇게 세부적으로 더 조절할 수 있지만 0.0.0.0호스트와 3000포트의 조합은 실행되지 않으므로 기본값으로 실행하겠음.
```

* $ export FLASK_ENV='development' ; bash ; reset를 하면 개발환경으로 바뀌면서 warning 메세지가 사라진다.
  * export : 변수설정을 하겠습니다.
  * FLASK_ENV : 변수의 이름은 FLASK_ENV입니다.
  * 'development' : FLASK_ENV의 설정은 'development'로 하겠습니다.
  * ; : 뒤의 명령어를 바로 실행 하겠습니다.
  * export FLASK_ENV= 으로 하면 초기화됨;;

```python
@app.route('/')
def index():  # '/' : 뿌리(root) 모든 것의 최상단, 보통 index로 설정함.
    return 'Hi!'

@app.route('/ssafy')  # 이런식으로 페이지를 늘리는.. ( routing )
def ssafy():
    return 'sssssssssafy'

```

* 실시간으로 주소창에 입력한 정보가 변수로서 반영되려면 `<string:name>`을 입력하고 함수 값으로 name를 입력한다.

```python
@app.route('/hi/<string:name>')  # ( variable routing )
def hi(name):
    return(f'hi {name}')
```

* from flask import jsonify를 하면 list를 웹으로 보낼 수 있다.

