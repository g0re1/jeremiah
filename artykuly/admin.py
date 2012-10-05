from django.contrib import admin
from artykuly.models import Art, Comment, User


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('tytul', 'date')
    prepopulated_fields = {'slug': ('tytul',)}


class CommentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['art', 'login', 'email', 'content']}),
    ]
    list_display = ('art', 'login', 'content')
 
 
admin.site.register(Comment, CommentAdmin)
admin.site.register(Art, ArticleAdmin)
admin.site.register(User)
