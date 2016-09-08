from django.contrib import admin
from .models import Snippet


class SnippetAdmin(admin.ModelAdmin):
    list_display = ('created', 'title', 'code', 'linenos', 'language', 'style')
    list_display_links = ('title',)


admin.site.register(Snippet, SnippetAdmin)
