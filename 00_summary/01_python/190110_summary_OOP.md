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
    count = 0  # 시도 횟수
    count_heart = 1  # 목숨
    while count != n and count_heart != h:
        count += 1
        if count == n:
            my_answer = input(f'마지막 시도입니다. 신중하게 입력하세요 : ')
        else:
            my_answer = input(f'{count}번째 시도입니다. 단어를 입력하세요 : ')
        if status(answer, my_answer) == '오답입니다.':
            count_heart += 1
        elif is_answer(answer, my_answer):
            return f'정답은 {answer} 입니다! {count}번 만에 성공하셨어요!'
        print(' ♥ '*(h-count_heart+1), '♡ '*(count_heart-1))
        print()
        print(status(answer, my_answer))
        print()
    if count == n:
        return f'{count}번의 도전기회를 모두 소모하셨습니다. 가망이 없군요!' 
    else:
        return f'{count_heart}개의 목숨을 모두 소진하셨습니다. 포기하세요!'
```





### 
