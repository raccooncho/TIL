# 190108 summary_python



### 1. Git

- $ git init 
  - .git -> 버전관리의 기능을 가진 directory로 바꿈 == repository
  - (master)라는 수식어가 따라다니게 됨
  - rm -rf .git 로 .git을 제거하면 사라짐
- $ which git 으로 사용하는 git이 설치된 경로를 확인할 수 있다.
- home으로 돌아가서 cat .gitconfig를 입력할 수 있다.
  - $ vim .gitconfig로 수정할 수 있다.
  - [core]에서 editor을 vim으로 바꾼다.
  - a를 입력하면 insert모드로 변경되어 입력 및 수정이 가능하다.
  - esc키로 insert에서 나온다.
  - :w로 저장하고 :q로 나온다.
    - :wq로 한번에 저장하고 나올 수 있다.
- $ git help는 명령어를 알려주는 명령어이다.
- 작업하는 장소 (repository)에서 cd .git하면 (master)가 (GIT_DIR!)로 바뀌면서 .git폴더로 이동한다.
- $ git status
  - repository의 상태를 알려준다.
  - 파일의 수정/추가/제거 상황이 반영된다.
- $ git add
  - git에 파일을 추가한다.
  - . 은 현재 위치를 말한다.
  - 파일명을 직접 입력하면 해당 파일만 추가된다.
  - git add 한걸 없애는건 $git rm --cached (파일명) 하면 된다.
- $ git commit -m '할말'
  - add된 파일에 대한 commit을 기록한다.
  - $ git commit -m ??
    - commit 할 수 있는 상태를 알려준다.
    - add된게 없으면 할 수 없다고 나옴.

```markdown
commit 메세지 작성 요령
1. 현재형으로
2. 명령하듯이
3. 너무 길지 않게
```



- $ git log

  ```
  commit 52fd37a85f937d675a5cb3a52bd21a5fe05e0cb9 (HEAD -> master)
  Author: RaccoonCho <wjtjdrb@naver.com>
  Date:   Tue Jan 8 06:43:39 2019 +0000
  
      first commit
  ```

  commit 뒤 내용이 내가 올리는 버전을 말한다.

  first commit자리는 commit 한 내용이 나오는 자리다.



- github에서 new repository생성하기

  (https://github.com/raccooncho/learn_git_prj.git)

- (만약 git add랑 git commit를 한 상태라면 -> 아니라면 해줘야함)

  - ```
    git remote add origin https://github.com/raccooncho/learn_git_prj.git
    ```

- 그러면 $ cat .git/config에 url과 fetch가 추가됨. (url과 fetch는 보내는 곳과 받는 곳인데 보통 같음)

- $ git remote -v로 url과 fetch를 확인할 수 있음.

- $ git push -u origin master한 후에 login하게 됨

  - -u : upstream(안중요)

- github사이트의 repository에서 clone or download를 하면 url을 복사할 수 있음.

- $ git clone url을 입력하면 git에 있는 파일을 다운받게 됨(bash에서는 ctrl v가 안되므로 shift insert로 붙여넣기 할수있음.)

  - $ git clone url name : name(폴더명)을 입력할 수 있음.

- $ code .하면 현재 위치에서 vscode가 열림!

- 만약 push pull하다가 꼬이면

  - $ git pull 하고 vim화면으로 가는데 여기서 esc키 하고 :wq로 나오면 됨
  - 새로 로그인 하게 됨



### 0. 아침 문제풀이 & setting changes

* jupyter notebook명령어 내가 원하는거로 바꾸기

  * 우선 cd로 홈가기

  * less .bash_history 를 들어가면 명령어 목록 보기 가능(q로 나옴)

  * touch .bashrc 폴더 만들기

  * (vim .bashrc로 수정하는곳 들어가기

  * i 누른 후 alias 'jn'='jupyter notebook'입력

  * :w로 저장 후 :q로 나오기)

    or

  * (echo 'alias "jn"="jupyter notebook"' >> .bashrc) 

  * --> 수정할 때는 >>를 >로 쓰면 됨(덮어쓰기)

  * cat .bashrc로 제대로 입력됬나 확인하기

  * bash를 껐다 키거나 bash를 입력해서 자동으로 재부팅시킨 후 사용하면 됨

* quiz 1. 이상한 덧셈

  * 숫자로 구성된 리스트에서 양의 정수의 합을 구하는 함수, 'positive_sum'을 만들어 보세요.
  * 예시)

  ```python
  positive_sum([1, -10, 2]) #3
  positive_sum([-1, -2, -3, -4]) #0
  ```

```python
def positive_sum(lists):  # 내 답
    pos_list = []
    for num in lists:
        if num > 0:
            pos_list.append(num)
    return sum(pos_list)
```

```python
def positive_sum(numbers):  # 교수님 답
    total = 0
    for number in numbers:
        if number > 0:
            total += number
    return total
```

```python
def pos_sum(numbers):  # 교수님의 고오급 답
    return sum(x for x in numbers if x > 0)  
```



* quiz 2. 문자열 탐색

  * 문자열 요소로만 이루어진 리스트를 넣었을 때, 문자열의 길이가 2 이상이고 주어진 문자열의 첫 번째와 마지막 문자가 같은 문자열의 수를 세는 함수 'start_end' 를 작성하세요
  * 예시)

  ```python
  start_end(['level', 'asdwe', 's', 'abadsfa', 'q1q']) # 3
  ```

```python
def start_end(lists):  # 내 답 == 교수님 답 # 성공적
    count = 0
    for words in lists:
        if len(words) > 1 and words[0] == words[-1]:
            count += 1
    return count
```

* quiz 3. Collatz

  * Collatz 추측: 어떤 자연수 n 이던지, 다음과 같은 작업을 반복하면 1로 만들수 있다.
    1. n이 짝수라면 2로 나눈다.
    2. n이 홀수라면 3을 곱하고 1을 더한다.
    3. 결과로 나온 수에 1/2의 작업을 1이 될때까지 반복한다. 예를 들어 n이 6이면, 6 => 3 => 10 => 5 => 16 => 8 => 4 => 2 => 1이 되며 8번(=>갯수!)만에 1이 됩니다. 자연수 n이 들어왔을 때, 몇 번의 작업만에 1이 되는 지를 'return'하는 함수 'collatz()'를 완성하세요. 단! 500번을 넘어가도 1이 되지 않는다면, -1을 'return'하세요!
  * 예시)

  ```python
  collatz(6) # 8
  collatz(16) # 4
  collatz(6263313) # -1
  ```

```python
def collatz(n):  # 내 답
    count = 0
    while int(n) >= 2 and count <=500:
        if int(n) % 2:
            n = n * 3 + 1
            count += 1
        else:
            n = n / 2
            count += 1
    if int(n) == 1:
        return count
    else:
        return -1
```

```python
def collatz(num):  # 교수님 답
    for i in range(500):
        if num % 2:
            num = num * 3 + 1
        else:
            num = num / 2
        if num == 1:
            return i + 1
    return -1
```



* quiz 4.  솔로 천국

  * 리스트가 주어질 때, 리스트의 요소 'e'는 'range(0, 10)'에 포함되는 자연수이다. 리스트에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거하여 'return'하는 함수 'lonely()'를 작성해 보세요. 이때! 제거된 후 남은 수들을 반환할 때는 리스트의 요소들이 순서를 유지해야 합니다!
  * 예시)

  ```python
  lonely([1, 1, 3, 3, 0, 1, 1, 3, 0, 3]) # [1, 3, 0]
  lonely([4, 4, 3, 3, 3, 4]) # [4, 3]
  ```

```python
def lonely(lists):  # 내 답 
    tlist = []
    for i in lists:
        if i not in tlist:
            tlist.append(i)
    return tlist
```

```python
def lonely(numbers):  # 교수님 답
    result = []
    for number in numbers:
        if not result:
            result.append(number)
        elif result[-1] != number:
            if result.count(number) == 0:
                result.append(number)
    return result
```



* quiz 5. (hard) RGB 삼각형

  | BG   | RG   | BR   | RR   | GG   | BB   |
  | ---- | ---- | ---- | ---- | ---- | ---- |
  | R    | B    | G    | R    | G    | B    |
  > 입력으로  ''R', 'G', 'B''가 섞여있는 문자열이 들어온다. 문자열은 다음과 같이 합쳐진다. 해당 문자열을 처리하여 마지막 색깔만 'return'하는 'triange()'을 작성하세요.

  * 예시)

  ```python
  triangle('RRGBRGBB') # G
  triangle('GB') # R
  triangle('B') # B
  triangle('RGBG') # B
  ```

```python
def triange(RGB):  # 고재두님 답 참고한 내 답
    RGB = ' '.join(RGB).split()
    tri = RGB
    sample = { 'R', 'G', 'B' }
    while len(RGB) != 1:
        tri = []
        for i in range(len(RGB) - 1):
            if RGB[i] == RGB[i + 1]:
                tri.append(RGB[i])
            else:
                color = sample - { RGB[i], RGB[i + 1] }
                tri = tri + list(color)
        RGB = tri
    return tri
```

```python
def triange(RGB):  # 삼각형 그리기 ( no return )
    RGB = ' '.join(RGB).split()
    tri = RGB
    sample = { 'R', 'G', 'B' }
    count = 0
    while len(RGB) != 1:
        tri = []
        for i in range(len(RGB) - 1):
            if RGB[i] == RGB[i + 1]:
                tri.append(RGB[i])
            else:
                color = sample - { RGB[i], RGB[i + 1] }
                tri = tri + list(color)
        count += 1
        blankc = (count) * ' '
        print(blankc + ' '.join(tri))
        RGB = tri
```

* quiz 6 . (??) 홀수개를 찾아라.

  > 입력으로 list가 한개 들어옵니다. 이 list에는 1개의 숫자만 홀수 개 들어있습니다.
  >
  > 이 1개의 홀수개인 숫자를 return 하는 find_odd()를 작성하세요.

  * 예시)

  ```python
  find_odd([1, 1, 2, 2, 3, 3, 3]) # 3
  find_odd([2, 1, 2]) # 1
  find_odd([1, 2, 2, 3, 2, 2, 1]) # 3
  ```

```python
def find_odd(numbers):  # 내답안
    odd_number = set()
    for i in numbers:
        if numbers.count(i) % 2:
            odd_number.add(i)
    return list(odd_number)
```

```python
def find_odd(numbers):  # 오.....한 답안 
    for uniq in list(set(numbers)):
        if numbers.count(uniq) % 2:
            return uniq
```

```python
from operator import xor  # 교수님의 import 한 답안. 은 reduce도 import해야하는데 어디서 해야하는지 몰라서 fail

def find_odd(numbers):
    return reduce(xor, numbers)

def find_odd_2(numbers):  # 이렇게 하면 import안해도 됨.
    result = 0
    for n in numbers:
        result = result ^ n
    return result

```


