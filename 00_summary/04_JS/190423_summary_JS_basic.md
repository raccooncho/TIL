# JaveScript_Basic

### Browser Object Model (BOM) Manipulation(조작)

( F12 console에서..)

* window == browser

* window.innerHeight -> 브라우저 높이 출력
* window.print() -> 프린트창으로 넘어감

##### Browser event

* window.alert('??')
  * alert('??') -> 둘이 똑같음. window를 제외하고 입력해도 상관없음. ??라는 메세지를 띄워줌
* confirm('really?') -> yes를 누르면 true를, no를 누르면 false를 return 함

### Document Object Model (DOM) Manipulation

* window.document == document
  * window.document.title -> 문서의 title 검색
  * window.document.title = '쉬는시간' -> 문서의 title이 '쉬는시간'으로 변경됨

* window.document.write('김치볶음밥') -> '김치볶음밥'을 새로 씀 ( 새 화면에, 다시 쓰면 이어서 써짐 )
* document.querySelector('h1') -> h1 tag만 출력해줌



### Programming

```javascript
clap = '<p> 짝 </p>'
for (i = 1; i <= 10; i++) {
    if ( i % 3 == 0) {
        window.document.write(clap)
    }
    else {
        window.document.write(`<p> ${i} </p>`) }
}
```



### JS 문서를 html에서 작성할 때는 세미콜론(';')을 문장 끝에 입력해 줘야 한다.

```javascript
        alert('Welcome to JS');
        confirm('회식을 간다.');
```



### 주석의 종류는 두가지가 있다.

```javascript
    <script>
        /*
            This is Long Comment
         */
        // alert('hihi');
    </script>
```





