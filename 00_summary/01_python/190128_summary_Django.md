# 190128 Summary Django



migrate 삭제

```sqlite
 python manage.py migrate boards zero
```



json 파일로 만들기

```python
from django.shortcuts import render, HttpResponse
from .models import Article
from django.http import JsonResponse

def detail(request, id):
    article = Article.objects.get(id=id)
    return JsonResponse({
        'id':article.id,
        'title':article.title, 
        'content': article.content,
    })
```

I want to go H.O.M.E N.O.W !