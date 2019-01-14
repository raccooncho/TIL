# 190114 summary_html



### 1. Web

* world wide web : www

* Web service?

  클라이언트 (Client) --> 요청 (request) --> 서버 (server) --> 응답 (response) --> 클라이언트 (Client)

  유저 (user) --> 요청 (request) --> **프로그램 (program)** --> 응답 (response) --> 유저 (user)

* Server computer한대가 여러 클라이언트에게 service를 제공함.

* 개발 환경이 다르다.

  * Pc
    * 나에게 필요한 프로그램들이 깔려 있다.
    * 내가 쓰는 용도에 맞는 성능을 가진다.
    * 보안에 있어 공격대상이 되기 쉽다.
    * 가끔 꺼진다.
  * 서버 컴퓨터
    * 서버 역할을 위해 필요한 프로그램**만** 깔려있다.
    * 클라이언트 사용량에 맞는 성능을 가진다.
    * 보안에 있어 공격대상이 되기 쉽다.
    * **절대 꺼지지도, 인터넷 연결이 끊겨서도 안된다. **

  * PC에서 (서버 컴퓨터와 환경을 맞추고) 개발을 한 후 서버 컴퓨터로 프로그램을 이동시킨다!!
    * git을 이용해서 옮기는게 가장 편한 방법이다.
  * 서버 컴퓨터를 빌리거나(C9) 직접 운영하거나...



### 2. HTML

* HyperText Markup Language
  * HyperLink를 통해서 text간 이동이 자유로움
* Hyper Text Transfer Protocol을 지켜야 함(HTTP)
* Markup : 각 Text간 역할을 규칙에 따라 지정함 (`<h1>`, `<p>`...etc..)



##### CSS

* Cascading Style Sheet



##### W3C

* world wide web consortium
* 인터넷 표준을 정해주는 기구이다.



##### Static web

* 입력한 주소가 정확히 맞아야만 페이지가 출력되는 web
  * 사서없는 도서관..
  * 단순한 directory의 나열



##### Dynamic web

* Web application program(web APP)



##### URI

* url : uniform resource locator
  * 네트워크 상에서 자원이 어디있는지를 알려주기 위한 고유 규약이다.
  * 웹사이트 주소 뿐만 아니라 컴퓨터 네트워크 상의 자원을 모두 나타낼 수 있다.



#### HTML 실습

(html validator에서 오류를 체크할 수 있음.)

* 선언

```html
<!DOCTYPE html>
```

* element 

  * tag와 content를 합쳐서 element라고 부른다

  ```html
  <h1>Comming Soon.....</h1>
  ```

  `<h1> </h1>` -> tag, `Comming soon.....` -> content

* `<div>`

  * html4까지는 div를 이용해서 그룹화 시켰다.

  * html5에서는 div의 의미를 명확히 하기 위해서 새로운 태그가 추가되었다.

    ```html
    <header></header>
    <nav></nav>
    <aside></aside>
    <section></section>
    <article></article>
    <footer></footer> 등등..
    ```

* 진한글씨 : `<strong>`=> 원래는 `<b>`였는데 html5에서 의미를 강조하기 위해 새로 생김

* 기울어진 글씨 : `<em>` => 원래는 `<i>`였는데 html5에서 의미를 강조하기 위해 새로 생김

* 인용구 : `<blockquote>`

* url 링크

  * `<a href=""> </a>` : href에 url 주소를 입력하고 a 사이에 문구를 입력하면 문구를 클릭할 시 해당 url로 이동하게 된다.
  * target="blank"를 추가하면 현재 창이 아니라 새 창에서 url링크로 이동하게 된다.

* img

  * `<img src="" alt="" />` : src에 image의 경로(url포함이지만 local에 있는 파일이 더 좋음)를 넣고 alt에 넣은 내용으로 image를 출력할 수 없을 경우에 그 내용이 대신 출력됨.

* 수평선

  * `<hr />`으로 하면 된다.

* 리스트

  * `<ol>`: 순서가 있는 리스트 이다.
  * `<ul>` : 순서가 없는 리스트 이다.
  * li * 숫자 + tab을 하면 해당 숫자만큼 li tag가 생긴다.

* 동영상

  * `<iframe>`을 이용해서 할 수 있다.

* 표

  ```html
  <table>
      <thead>
          <td>점심메뉴</td>
      </thead>
      <tr>
          <th></th>
          <th>월</th>
          <th>화</th>
          <th>수</th>
      </tr>
      <tr>
          <td>특식</td>
          <td>초밥</td>
          <td>바베큐</td>
          <td>삼겹살</td>
      </tr>
      <tr>
          <td>한식</td>
          <td>육개장</td>
          <td>미역국</td>
          <td>삼계탕</td>
      </tr>
  </table>
  ```

  * thead는 표의 제목이다.(표 안에 들어가는 내용이 아니다.)
  * tr : 가로 줄을 의미함
    * th : 맨 윗줄 즉, 헤더를 의미함.
    * td : 테이블의 데이터를 의미함.

  * table>tr>th*3 같은 식으로 한번에 만들수도 있음.
  * colspan : 차지하는 표의 칸 수 (가로)
  * rowspan : 차지하는 표의 칸 수 (세로)

  * 표에 줄을 긋기 위해선 ! 

    * head에서 style tag를 만든다

      ```html
      <style>
                  table, tr, td {
                      border: 1px solid darkgray
                  }
      </style>
      ```

      