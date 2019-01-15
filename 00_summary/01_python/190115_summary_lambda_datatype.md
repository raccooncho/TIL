# 190115 summary_datatype_lambda



### 1. data type

##### ordered / unordered

* ordered(순서가 있음, index접근이 가능) : string [list] (tuple) range()
* unordered(순서가 없음, index접근이 불가능) : {set} {dictionary:}
  * dict는 순서가 있지만 공식문서에서 인정을 안함(py3.6) / py 3.7부터는 순서가 있는것을 공식문서에서 인정함. / py 3.6 이전에선 dict의 순서가 랜덤하게 나왔었음..



##### immutable / mutable

* immutable(원본이 변형되지 않음) : 'string' (tuple) range()
* mutable(원본이 변형될 수 있음) : [list] {set} {dictionary}



### 2. Lambda

##### lambda 표현식

> 함수를 한 줄로 줄여보자!

1. `def`를 삭제합니다.
2. 함수 이름과 인자 사이에 `=`을 넣습니다.

3. 마법의 단어 `lambda`를 씁니다.

4. 인자에서 `()`를 지웁니다.

5. `\n`을 지웁니다.

6. `return`도 지웁니다.

* 1회성 함수들에 대해서 lambda 자체를 인자로 넣기 위해 사용한다.

```python
def cube(n):
    return n ** 3

==

cube = lambda n: n ** 3
```

```python
fact = lambda n: 1 if n==1 else n * fact(n-1)
# 재귀함수랑 3항연산자도 됨
```

```python
my_add = lambda a, b, c: a + b + c
# 인자가 여러개여도 됨
```
