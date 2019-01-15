# 190115 summary_html_css



### 1. html

##### input

* type : type를 여러가지 설정 가능하다.
  * text, number, submit 등등
    * text : text가 입력 가능하다
    * number : number만 입력 된다.
    * submut : 제출 버튼이 생성된다.

```html
이 름 : <input type="text" placeholder="이름을 입력해라!"/>
나 이 : <input type="number" />
<input type="submit">
```

 * placeholder를 통해서 입력 예시 혹은 주의사항 등을 사용자에게 전달할 수 있다.

* input 대신 textarea를 이용하면 유동적으로 입력칸이 늘어나는 input area를 출력할 수 있다.

```html
자기소개: <textarea></textarea>
```

* input 에서 name값을 입력해 줘야 submit했을 때 해당 value가 제대로 넘어가게 된다.

```html
<input name="name" type="text" placeholder="이름을 입력해라!"/>
<input name="age" type="number" />
<input name="phone" type="text" />
<textarea name="intro"></textarea>
```

* 이 상태에서 submit를 하면 제출받는 페이지의 url에 정보가 입력되게 된다.
  * value값을 정하게 되면 value값으로 설정한 문구가 submit 버튼 위에 출력된다.

```
file:///C:/Users/student/raccooncho.github.io/index.html?name=%E3%85%81&age=1&phone=%E3%85%81%E3%84%B4&intro=%E3%85%81%E3%84%B4
```

* value값이 너무 많다.
  * 구글링을 하자
  * radio, date, checkbox
* select>option에서 하나를 고르게 하는 설정도 가능하다.
* autofocus를 넣으면 새로고침해도 focus가 autofocus값이 정해진 위치로 고정된다.

```html
 이름 : <input type="text" name="name" autofocus/>
```



##### form

* 하위 element를 박스로 묶는 역할을 한다. 
* action을 입력하면 form안에서 이루어진 정보가 action에 입력된 경로로 이동하게 된다.

```html
<form action="/index.html">
```



### 2. CSS

##### 스타일을 직접 적용하는 방법 (in line)

```html
<div style="border: 1px solid black;">
            <a style="color:green;" href="">I'm a link</a></div>
```

* html파일의 모든 element하나 하나에 스타일을 적용하면 된다.

```html
<body style="background-color:wheat; color: blue;">
```

* body(부모)에 적용한 style은 모든 element(자손)에 적용된다.



##### html 파일 전체에 적용하는 방법(head에 적용하기!)

* head tag 안에 style tag를 만들어서 거기에 적용하면 된다!

```html
 <head>
     <style>
         div {
             border: 1px solid black;
         }
     </style>
</head>
```

* 이대로 하면 style을 지정하는게 너무 길기 때문에 내용을 보기 힘들다...



##### CSS에서 class나 id의 이름은 지나치게 포괄적이거나, 어떻게 보여지는지를 나타내는 방법은 지양해야 한다.

* 어떻게 보여지는지를 나타낸다면 수정할 때 힘들어진다.

* 이름으로 가장 적절한 방법은 해당 class의 기능을 의미하도록 정하는 것이다.

  (ex.  alert, disabled, etc....)



##### id는 여러개가 중복되면 가장 첫번째 id만 적용된다.

* css에서 id값을 정하는 것은 권장되지 않는다.
* id값은 java-script에서 정하는게 좋다.
* css에서는 class정의를 주로 하는게 좋다.



##### Class명이 중복되서 입력된 경우 더 아래에 있는 class의 내용이 우선 출력된다.



##### 상속

* 아무것도 없으면 부모가 흘려보낸 style을 상속받게 된다.



##### 우선순위

* 브라우저 설정을 수동으로 설정한 경우
* id
* class
* 기본적인 selector
* 브라우저 기본 설정
* 같은 우선순위여도 좀 더 specific할 수록 우선순위가 올라간다.
* 같은 우선순위일 경우에는 css문서에서 아래위치에 작성된 selector가 우선순위를 가져가게 된다.

**! important**는 절대 쓰지 맙시다!!!