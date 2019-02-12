from django.contrib import admin
from .models import Movie
# Register your models here.


class MovieModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')


admin.site.register(Movie, MovieModelAdmin)