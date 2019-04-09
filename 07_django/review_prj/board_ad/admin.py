from django.contrib import admin
from .models import Posting, Comment

# Register your models here.

class PostingModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at') # 수정 불가
    list_display = ('id', 'title', 'created_at', 'updated_at') # 전체 리스트에서 보여지는 목록
    list_display_links = ('id', 'title') # 전체 리스트에서 링크로 표시되는 항목 설정

admin.site.register(Posting, PostingModelAdmin)


class CommentModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at') # 수정 불가
    list_display = ('id', 'posting', 'content', 'created_at', 'updated_at') # 전체 리스트에서 보여지는 목록
    list_display_links = ('id', 'content') # 전체 리스트에서 링크로 표시되는 항목 설정

admin.site.register(Comment, CommentModelAdmin)