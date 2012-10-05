from django.contrib import admin
from news.models import Comment, User, News


class NewsAdmin(admin.ModelAdmin):
    list_display = ('tytul', 'date')
    prepopulated_fields = {'slug': ('tytul',)}


class CommentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['news', 'login', 'email', 'content']}),
    ]
    list_display = ('news', 'login', 'content')


admin.site.register(Comment, CommentAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(User)
