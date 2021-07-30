from django.contrib import admin

from .models import Comment, Follow, Group, Post

EMPTY_TEXT = "-пусто-"


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ('pk', 'text', 'pub_date', 'author', 'group')
    search_fields = ('text',)
    list_filter = ("pub_date",)
    empty_value_display = EMPTY_TEXT


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'description')
    prepopulated_fields = {"slug": ("title",)}
    search_field = ('title')
    list_filter = ('title',)
    empty_value_display = EMPTY_TEXT


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'text', 'created')
    search_field = ('author')
    list_filter = ('post',)
    empty_value_display = EMPTY_TEXT


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('user', 'following')
    search_field = ('following')
    list_filter = ('user',)
    empty_value_display = EMPTY_TEXT
