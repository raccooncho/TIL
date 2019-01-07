# 190104 summary_cli



### 1. command line interface

##### $ ls ( in bash ) = > dir  = user -> student ( in 탐색기, ssafy 컴퓨터의 경우 )

* 파일 디렉토리를 보여 준다.
* ls = list, dir = directory



### BASH

#### $(== prompt)  : 명령할 준비가 되어 있음

##### $ pwd

* 현재 위치 ( /C/Users/student)
  * / 는 내 PC이다.

##### $ ls -a  == $ ls --all 

* 숨김파일까지 모두 보여준다.
* 앞에 .이 붙어있으면 숨김파일이다. (유닉스에서만 지원하고 윈도우에선 지원해주지 않는 기능이다.)

##### $ ls -l

* long형식으로 파일들을 나열한다.
* 자세한 내용이 나온다.

##### $ ls -la or $ ls -al

* 모든 파일을 long형식으로 나열한다.
* 시간을 반대로 하려면 tr을 붙이면된다. (time reverse)

##### $ ls a*

* ls를 이용하면 특정 조건의 파일만 찾아서 볼 수 있다.

* ls a*는 a로 시작한는 파일들만 찾는 명령어다.


##### $ cd () 

* () 에 입력한 폴더로 이동한다.
* cd .. 은 상위 폴더로 이동이다.
* cd /은 최상위 폴더로 이동한다.
* cd ~ 은 작업하기 좋게 컴퓨터가 정해준 공간으로 이동한다. ( ~ == home )
* cd .은 현재 내 위치로 이동이다.
* cd - 는 뒤로가기임.

##### $ mkdir classroom

* classroom 이란 이름의 폴더가 형성된다.
* $ mkdir -p ssafy/ss3/students
  * ssafy폴더를 생성하고 그 안에 ss3폴더를 생성 및 또 ss3폴더 안에 students폴더를 생성한다.

##### $ rmdir a

* a 폴더를 삭제한다.
* 폴더가 비어있지 않으면 삭제되지 않는다. 
* $ rmdir -f 혹은 $ rm -r을 이용해서 강력삭제를 한다.
* 강압적으로 다 지울수 있는 명령어는 $ rm -rf이다.

##### $ touch classmate.txt

* classmate.txt란 이름의 메모장이 형성된다.
* touch a.txt b.txt c.txt d.py e.py  이거처럼 여러 파일을 동시에 만들 수 있다.
* 파일 명 앞에 .을 붙이면 숨김파일로 생성된다. 
* 접근이 허용되지 않은 폴더가 있음. 
  * $ ls /을 했을때 대부분은 허용이 되지 않는 폴더임   
  * sudo 를 앞에 붙여서 강제 명령 실행이 가능함.                                                                                         

##### $ vim classmate.txt

* 메모장을 수정하로 간다
* esc키를 눌러야 커맨드를 입력할 수 있다.
* dd가 삭제다
* :w 저장
* :q 나가기
* i 입력

##### $ man echo

- echo의 기능을 설명해주는 manual임.

- q 를 누르면 나올 수 있음. (quit)

- windows에서 실행하는 bash는 사용할 수 없음

- h버튼은 help임.

- /는 검색기능임

  - n하고 b로 이전 검색어 다음 검색어 찾을 수 있음.

- u누르면 반페이지 위로 가고 d누르면 반페이지 아래로 간다.

- 


#### $ yes는 입력하지 맙시다!!



#### $ echo

##### $ echo hello

- hello 가 출력됨
- 파이썬처럼 'hello' 혹은 "hello" 를 입력해도 됨
- echo는 표준 출력임

##### $ echo "When I was a young boy" > black_parade.txt 

* black_parade.txt 파일을 생성해서 해당 문구를 입력해줌.
* 다시 다른 문구를 입력하면 해당하는 내용으로 덮어 써버림.( redirect)

##### $echo 'to the black' >> black_parade.txt

* append 하는 기능임

##### $ cat black_parade.txt

* black_parade.txt의 내용을 확인할 수 있음.

##### $ cat line_1.txt line_2.txt >> song.txt

* line_1.txt의 내용과 line_2.txt 의 내용이 순서대로 song.txt에 저장됨.

##### $ mv reverse.txt rev.txt 

* reverse.txt의 파일명을 rev.txt로 변경한다. (move)

##### $ cp rev.txt copy.txt

* rev.txt 를 copy.txt라는 이름으로 복사한다.

##### $ rm copy.txt

* copy.txt를 삭제한다.

* rm -i copy.txt를 입력하면 삭제 할지 여부를 물어본다.

* 윈도우의 shift+del기능과 같이 완전 삭제한다. (y를 누르면 삭제 함)

* 더 강력한 삭제를 원하면 rm -f copy.txt를 입력한다 .

* rm *.txt를 입력하면 .txt로 이름이 끝나는 모든 파일을 삭제한다.






####  ^C 

* ^은 ctrl을 의미함
* 실행을 취소한다는 의미임 ( cancel)



##### ←→는 커서가 움직이고 ↑↓는 이전 이후 명령어를 입력함

##### ^p 는 이전 명령어 ^n 은 이후 명령어 이지만 윈도우(크롬)에서는 ^n이 새창을 여는 명령어라 겹침///

##### ^l 은 다 위로 올려서 화면을 깨끗하게 해줌

##### ^d 는 터미널 종료

* python3를 들어갔을때 ^C로 종료가 안됨.
* ^d를 통해 나올 수 있음.



##### $ sleep time

* 숫자를 입력함.
* 기본 설정은 s임 (second)
* m 이나 h등을 이용해서 분 혹은 시간 단위로도 재울 수 있음.
* ^C를 통해 나올 수 있음.



#### $ curl

##### $ which curl

* 이렇게 curl이 설치되어 있는지 확인한다.

##### $ curl -OL neovansoarer.github.io/files/sonnets.txt

* 교수님 깃헙에 있는 파일을 다운로드 받을 수 있다.
* 없는 파일로 입력하면 오류 페이지의 html을 다운받게된다.
* 네이버를 입력하면 네이버의 html을 다운받는다.

##### $ curl -I https://raccooncho.github.io

* 내 깃헙의 헤더를 가져온다.



##### $ head sonnets.txt

* 첫 10줄만 나온다.
* $tail sonnets.text하면 마지막 10줄만 나온다.



##### $ ping google.com

* google.com에 계속 신호를 보낸다.
* $ ping google.com > google.log를 통해 신호를 받은 결과를 google.log에서 확인할 수 있다. 



##### $ wc sonnets.txt

* 줄 단어 문자 파일명 순으로 출력됨
* $ head sonnets.txt | wc
  * | 앞의 출력을 뒤의 명령어로 해석함



##### $ less sonnets.txt

* man같이 뷰어형식으로 읽을 수 있음
* 검색 기능 있음 (/)



#####  $ grep rose sonnets.txt

* sonnets.text의 rose가 들어있는 줄을 찾아준다.
* $ grep rose sonnets.txt | wc  -> 이렇게 rose의 갯수도 검색할 수 있다.
* $ grep -i rose sonnets.txt | wc  -> 대문자로 시작하는  rose도 검색한다.

* 한줄에 rose가 두개이상 들어간건 셀 수 없는 단점이 있다.

#####  

##### $ ps aux 

* 지금 실행 중인 status가 검색된다.

* 컴퓨터에서 계속 실행하고 있는 프로그램을 의미함.

* `$ ps aux | grep jupyter                                                         `  이렇게 실행중인 jupyter을 검색하면

  ```
  16060   15252   16060      15516  pty0      197609 17:20:02 /c/Python36/Scripts/jupyter
  
  ```

  이렇게 출력되고 

* kill -9 16060

  * 이렇게 맨 앞숫자인 16060을 kill하는 명령어를 입력하면 jupyter이 종료된다.



