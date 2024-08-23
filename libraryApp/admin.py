from django.contrib import admin
from . import models

# Register your models here.
class authorAdmin(admin.ModelAdmin):
    list_display = ['id', 'author_name', 'city']
    search_fields = ('author_name', 'city')
admin.site.register(models.Author, authorAdmin)  

class bookAdmin(admin.ModelAdmin):
    list_display = ['id', 'book_name', 'launchdate']
    search_fields = ('book_name', 'launchdate')
admin.site.register(models.Book, bookAdmin)
