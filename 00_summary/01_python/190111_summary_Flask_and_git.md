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



### 2. Git

* Basic Workflow

```sh
$ git init

$ git status  # 빨간색 확인

$ git add .

$ git status  # 초록색 확인 ( 초록색만 커밋됨 )

$ git commit -m '짧고 간결한 현재형'
```

*  githup, bitbucket, gitlab etc.. remote repo 를 생성

```sh
$ git remote add origin <REMOTE REPO URL.git>

$ git push (-u origin master # 첫 번째만 )
```

* 다른 컴퓨터라면,

```sh
$ git clone <REMOTE REPO URL.git> # downloadZIP => .git 없음....ㅠ
```

* 작업 하다가

```sh
$ git add .

$ git commit -m 'MSG'

$ git push
```

* 한번에 입력한다면

```sh
$ git add . && git commit -m 'MSG' && git push

\# (ㄴ Error 나면 작업이 실행되지 않음.)

$ git add . ; git commit -m 'MSG' ; git push

\# (ㄴ Error 나도 작업을 실행함. -> 불안정함;;)
```

* 변동사항을 알아보기 위해선

```sh
$ git diff
```

* 작업중인 txt문서는 .txt.swp라는 임시파일을 계속 생성한다 ( 작업이 끝날 때까지)

* 그래서 작업중에 git add를 하면 임시파일도 계속 기록되게 된다.

* 그래서 `$ touch .gitignore`를 입력해서 gitignore파일을 생성하면 해결할 수 있다.

  ```
  .dummy.txt.swp
  ```

  * 이렇게 .gitignore파일에서 직접 파일명을 입력하면 해당 파일은 git이 무시하게 된다.

  ```
  *.swp
  ```

  * 이런 식으로 *을 붙이면 .swp로 끝나는 모든 파일은 git 이 무시하게 된다.

  ```
  secrets/
  ```

  * secrets라는 폴더 안에 있는 파일들을 git에 올리고 싶지 않다면 폴더/ 를 입력하면 그 안의 내용은 git 이 무시하게 된다.
  * Home에 .gitignore_global 파일을 만들고 `$ git config --global core.excludesfile ~/.gitignore_global`을 입력한 후 ignore할 내용을 입력한다면 모든 directory에 적용된다.

* 잘못 git add 한 파일은 `$ git rm --cached dummy.txt`와 같이 입력하면 git 에 등록된 정보가 삭제된다.(unstaged)



##### git branch

* 기본 설정 (git init할 때)은 master임.
* `$ git branch`로 branch를 볼 수 있음.
* `$ git branch about-page`를 통해 about-page라는 branch를 생성함
* `$ git checkout about-page`를 통해 about-page branch로 이동함
* `$ git checkout -b about-page`를 통해 한번에 about-page branch를 생성하고 이동함.
* 다시  master로 옮기면 about-page에서 작업한 내용이 사라짐..
  * 하지만 다시 about-page로 돌아오면 작업한 내용이 돌아오니 걱정 ㄴㄴ



##### git merge

* master로 돌아와서
* `$ git merge about-page`하면 about page의 작업내용이 Master 로 합쳐진다.
* 근데 master랑 about page가 달라지면 conflict가 자주 난다.



##### Conflict

* 대부분의 conflict는 git이 자동으로 merge해준다.
  * conflict 상황에서 merge하면 vim 화면이 뜬다.
  * 이 경우는 다른 파일에서 conflict가 발생한 경우이다.

* 같은 파일에서 conflict가 발생한 경우는 문제가 더 복잡하다.

  * merge를 시도하면

  ```bash
  Auto-merging index.html
  CONFLICT (content): Merge conflict in index.html
  Automatic merge failed; fix conflicts and then commit the result.
  ```

  * 이렇게 문제가 발생한 파일을 알려준다.
  * 파일에 가서 문제가 발생한 부분을 직접 수정해야한다.

  * 하지만, vscode에서는 링크 클릭을 통해 conflict 를 해결할 수 있게 해준다.
  * ![1547192120523](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1547192120523.png)
  * commit까지 진행하면 문제 상황이 모두 해결된다. 



##### Github은 branch정보를 가져오지 않는다//////

* master에서 `$ git push`를 하면 master branch의 정보만 push하기 때문에 branch가 생성되지 않는다.
* 다른 branch(final-check)에서 push해도 

```bash
\fatal: The current branch final-check has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin final-check

```

이런 메세지가 뜨면서 push되지 않는다.

* `$ git push -u origin final-check` 를 이용해서 push하면 github사이트에 

  ![1547192822510](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1547192822510.png)

  이런 버튼이 생기고 메세지를 남긴 후 다른사람이 동의하면 push가 된다.

* 이러면 local에서는 merge가 되지 않아서 local에서 다시 merge해줘야 한다.

