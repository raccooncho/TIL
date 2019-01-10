# 190110 summary_python



### 1. 



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
            elif is_answer(answer, my_answer):
                return f'정답은 {answer} 입니다! {count}번 만에 성공하셨어요!'
            else:
                input_letter.append(my_answer)
            print('\n', ' ♥ '*(h-count_heart), '♡ '*(count_heart), '\n')
            print(status(answer, input_letter), '\n')
    if count == n+1:
        return f'{count}번의 도전기회를 모두 소모하셨습니다. 가망이 없군요!' 
    else:
        return f'{count_heart}개의 목숨을 모두 소진하셨습니다. 포기하세요!'
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
