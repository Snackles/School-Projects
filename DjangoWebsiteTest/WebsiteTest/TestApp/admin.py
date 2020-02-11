from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'body', 'postDate', 'visible')
    list_filter = ('visible', 'postDate')
    search_fields = ('author', 'body')
    actions = ['show_selected_comments', 'hide_selected_comments']

    def show_selected_comments(self, request, queryset):
        queryset.update(visible=True)

    def hide_selected_comments(self, request, queryset):
        queryset.update(visible=False)
