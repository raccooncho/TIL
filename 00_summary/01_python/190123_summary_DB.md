## 190123 Summary DB

### 1. SQL column 추가

```sqlite
ALTER TABLE <table_name>
ADD COLUMN <col_name> DATATYPE;
```

* DATATYPE : T/F의 경우 SQL모듈마다 다른데, SQLite에서는 Bool타입을 지원하지 않는다.



#### 근데 Python에서 지원하는 모듈이 더 좋은게 많아서....

#### Codecademy에서 기초만 공부하고 다른걸 합시다///



### 2. DJango

* install

```bash
pip install django
```

* django-admin

  * 실행할 수 있는 명령어를 입력할 수 있다.

  ```bash
  django-admin startproject first_django
  ```

   * first_django라는 장고 폴더를 만든다.

* manage.py는 실행을 도와준다.

```bash
python manage.py runserver $IP:$PORT
```

​	를 입력해서 실행을 한다.

* 보안문제가 있어서 생성된 장고폴더 안에 first_django폴더 안에 settings.py를 들어가서 ALLOWED_HOSTS 리스트 안에 주소를 입력해야한다.
  * https://는 지워야 한다.
  * 마찬가지로 맨 뒤의 /도 지워야 한다.
* 새로운 app만들기

```bash
django-admin startapp home
```

​	 home은 새로 만든 app의 이름이다.

​	* 새로 만든 app의 이름은 settings.py의 INSTALLED_APPS에 추가해 줘야 한다.

* 주로 작업하는 곳은 views.py이다.

```python
from django.shortcuts import render, HttpResponse
def index(request):
    return HttpResponse('RACCOONCHO') #HttpResponse를 하지 않으면 오류가 난다. (번역기...)
```

​	이렇게 작업한 후에 first_django 폴더의 urls.py폴더에서 home/views.py를 import해준다

```python
# home app(dir)에서 views파일을 import
from home import views
```

​	그리고 urlpatterns에 views.py에서 만든 함수의 경로를 추가한다.

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
] # '/'는 경로 뒤에 붙인다 (ex. lotto/)
```

* 유동적인 경로를 입력하려면

```python
path('hello/<name>', views.hello), # 경로를 이렇게 입력하고 
```

```python
def hello(request, name):  # 인풋값을 설정해 주면 된다.
    return HttpResponse('Hello ' + name)
```



#### html파일 연결시키기...

* 하지만 html을 연결시켜 주는게 더 좋기 때문에, home/templates폴더에 html파일을 만들어준다.

  * html파일의 이름은 views.py에서 만드는 함수의 이름과 동일한 것이 컨벤션이다.

* settings.py파일에서 `BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))`

  아래에 templates를 입력해야 한다.

```python
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
```

 * 그리고 아래 TEMPLATES라는 list안에서 DIRS라는 key값의 value로 [TEMPLATES_DIR]을 입력해준다.
    * settings.py에서 LANGUAGE_CODE = 'ko-kr' / TIME_ZONE = 'Asia/Seoul' 권장!
 * views.py에서

```python
def index(request):
    return render(request, 'index.html')
```

​	로 함수에 html파일을 입력시킨다.

