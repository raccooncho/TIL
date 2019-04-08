### 1급 객체

* 변수에 저장 / 바인딩 가능하다.
* 함수의 인자로 넘길 수 있다.
* 함수의 return 뒤에 있을 수 있다.

* 함수도 1급 객채다

```python
def Func():
    print('JaeDoo')


my_func = lambda x, y: x  # 변수에 저장 / 바인딩 가능

a = my_func(Func, 1)  # 함수의 인자로 넘길 수 있고, 마찬가지로 리턴도 가능.
a()
```

```python
def fco(): return lambda n: n + 1


num_100 = 100
num_101 = fco()(num_100)

print(num_101)
```

