# Basic Workflow
```sh
$ git init
$ git status  # 빨간색 확인
$ git add .
$ git status  # 초록색 확인 ( 초록색만 커밋됨 )
$ git commit -m '짧고 간결한 현재형'

# githup, bitbucket, gitlab etc.. remote repo 를 생성

$ git remote add origin <REMOTE REPO URL.git>
$ git push (-u origin master # 첫 번째만 )

# 다른 컴퓨터라면,

$ git clone <REMOTE REPO URL.git> # downloadZIP => .git 없음....ㅠ

# 작업 하다가

$ git add .
$ git commit -m 'MSG'
$ git push

#  ||
#  ||

$ git add . && git commit -m 'MSG' && git push
# (ㄴ Error 나면 작업이 실행되지 않음.)
$ git add . ; git commit -m 'MSG' ; git push
# (ㄴ Error 나도 작업을 실행함. -> 불안정함;;)
```
.
.
.
(반복)
.
.
.