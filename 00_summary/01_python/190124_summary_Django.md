## 190124 Summary Django

### 1. Django

##### urls 를 프로젝트 폴더 안에 있는 urls.py에 몰아 넣으면 복잡하다.

* 그래서 각 app폴더 안에 urls.py를 만들어서 url을 생성한다.

```python
from django.urls import path
from . import views

urlpatterns = [
]
```

이렇게 적고 시작한다..



httpsresponse로 하면 표현할수 있는것도 적고 안좋으니까 html로 경로를 바꿉시다..

settings.py -> TEMPLATES 위에 TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates') 을 입력하고 app폴더 안에 templates폴더를 만들어서 html파일을 관리한다.



#### 장고의 특수한 기능으로 html에서 python에서 작업한 내용을 받을 수 있다.

* 단 python파일에서 리턴값에 원하는 contents를 dict형태로 포함시켜 줘야 한다.

```python
 return render(request, 'square.html', { 'result': result })
```

그러면 result값으로 html에서 받을 수 있다.

* Template Variable

```html
<h4>{{ result }}</h4>
```



* Template Tag
  * html에서 파이썬의 로직을 약간 사용할 수 있게 된다..

```html
<ol>
    {% for number in lotto %}
   		<li>{{ number }}</li>
    {% endfor %}
</ol>
```

 * if 문도 가능하다

```html
<ul>
    {% for s in ss3 %}
        {% if s == name %}
        	<li><strong>{{ s }}</strong></li>
        {% else %}
       		<li> {{ s }} </li>
        {% endif %}
    {% endfor %}
</ul>
```



* 형식을 만들어서 모든 파일에 적용할 수 있다.

  * 형식이 되는 파일을 만든다 

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <title>
          Home - {% block title %}{% endblock %}
      </title>
  </head>
  <body>
      {% block content %}
      {% endblock %}
  </body>
  </html>
  ```

  * 해당 파일의 양식을 다른 파일에 적용시킨다.

  ```html
  {% extends 'base.html' %}
  
  {% block title %}
      index
  {% endblock %}
      
  {% block content %}
      <h1>It is INDEXPAGE of raccooncho's page</h1>
  {% endblock %}
  ```

  * 이렇게 하면 title이 home - index로 자동으로 바뀌게 된다.

  * but, 에러가 없어서 어렵다........(오타나면 그냥 화면에 안보임....)



* db를 관리하는 것은 models.py에서 작업한다.

  * models.py에는 class만 작성한다. (artist app)

  ```python
  class Band(models.Model):
      name = models.CharField(max_length=50)  # charfield == 문자를 받음,max를 정해줘야함
      debut = models.IntegerField()
      is_active = models.BooleanField(default=True)
      description = models.TextField(default='No description yet..')
  ```

* settings.py에서 artist를 추가한 후 bash에서 `$python manage.py makemigrations artist`을 입력하면 artist>migrations>0001_initial.py가 생성되고 models.py에서 입력한 내용이 적용되었음을 확인할 수 있다.

* `$python manage.py sqlmigrate artist 0001`처럼 생성된 db의 번호를 입력해주면 테이블이 생성된다.

* `$python manage.py migrate`을 입력해줘야 db가 적용된다.

* `$python manage.py shell`로 들어가서 `from artist.models import Band`을 입력하고 
* `b = Band(name='Queen')`를 입력해서 새로운 데이터를 입력한다.
* `b.save()`로 저장이 되어야 하지만 debut항목이 입력되지 않았으므로 오류가 발생한다.
* ` $ python manage.py dbshell`을 통해서 DB shell을 갈 수 있고
* 여기서 `SELECT * FROM artist_band`을 통해서 생성한 db를 확인할 수 있다.

* 새로 shell을 킬 때 마다 `from artist.models import Band`를 통해서 import해줘야 한다

  (shell을 나가는 방법은 ctrl + d 혹은 exit)

* shell에서 `Band.objects.all()`을 입력하면 현재 Band table에 있는 value들을 볼 수 있다.

  * `Band.objects.get(id=1)`로 검색할 수도 있다.
  * `Band.objects.filter(name__startswith='Qu')`로 조건문을 검색할 수도 있다.

#### 슈퍼 유저 설정

`$ python manage.py createsuperuser`을 입력하면 사용자 이름, email, password, password confirmation을 할 수 있다. 

* admin 페이지에서 로그인한 후 관리할 수 있다.
* DB를 관리하던 APP인 artist app에서 admin.py에

```python
from django.contrib import admin

from .models import Band
# Register your models here.

admin.site.register(Band)
```

이런 식으로 Band table을 설정하면 admin페이지에서 db를 관리할 수 있게 된다.