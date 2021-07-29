from django.contrib import admin

from .models import Comment, Follow, Group, Post

EMPTY_TEXT = "-пусто-"


class PostAdmin(admin.ModelAdmin):

    list_display = ('pk', 'text', 'pub_date', 'author', 'group')
    search_fields = ('text',)
    list_filter = ("pub_date",)
    empty_value_display = EMPTY_TEXT


class GroupAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'description')
    prepopulated_fields = {"slug": ("title",)}
    search_field = ('title')
    list_filter = ('title',)
    empty_value_display = EMPTY_TEXT


class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'text', 'created')
    search_field = ('author')
    list_filter = ('post',)
    empty_value_display = EMPTY_TEXT


class FollowAdmin(admin.ModelAdmin):
    list_display = ('user', 'following')
    search_field = ('following')
    list_filter = ('user',)
    empty_value_display = EMPTY_TEXT


admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Follow, FollowAdmin)
