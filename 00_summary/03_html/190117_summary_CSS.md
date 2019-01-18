# 190117 summary_css



### 1. Selector

* a[href]
  * a tag elements 중에 href 어트리뷰트를 갖는 모든 element에 적용됨
* a[target="_blank"]
  * a tag elements 중에 target의 값을 _blank로 갖는 모든 element에 적용됨
* p[title~="first"]
  * p tag elements 중에 title 어트리뷰트의 값으로 first를 갖는 모든 element에 적용됨
  * 단, first 앞 뒤가 공백으로 구분되어 있어야 한다.
* p[title|="second"]
  * p tag elements 중에 title 어트리뷰트의 값이 second 이거나 second뒤에 '-'로 이어지는 모든 element에 적용됨
* p[title^="second"]
  * p tag elements 중에 title 어트리뷰트의 값이 second로 시작하는 모든 element에 적용됨
* a[href$=".net"]
  * a tag elements 중에 href 어트리뷰트의 값이 .net로 끝나는 모든 element에 적용됨
* p[title*="first"]
  * p tag elements 중에 title어트리뷰트의 값에 first가 포함되어 있는 모든 element에 적용됨

##### 후손 셀렉터

* 