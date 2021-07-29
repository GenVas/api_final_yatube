from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

ADDING_DATE, PUBLICATION_DATE = 'Дата добавления', 'Дата публикации'
COMMENT_VERBOSE, COMMENTS_VERBOSE = "Комментарий", "Комментарии"
FOLLOW_VERBOSE, FOLLOWS_VERBOSE = "Подписка", "Подписки"
GROUP_VERBOSE, GROUPS_VERBOSE = "Группа", "Группы"
POST_VERBOSE, POSTS_VERBOSE = "Подписка", "Подписки"


class Group(models.Model):

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    class Meta:
        ordering = ['title']
        verbose_name = GROUP_VERBOSE
        verbose_name_plural = GROUPS_VERBOSE

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(PUBLICATION_DATE, auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True)
    group = models.ForeignKey(
        Group, on_delete=models.SET_NULL,
        related_name='posts', blank=True, null=True)

    class Meta:
        ordering = ['-pub_date']
        verbose_name = POST_VERBOSE
        verbose_name_plural = POSTS_VERBOSE

    def __str__(self):
        return (f"автор: {self.author.username}, группа: {self.group}, "
                f"дата: {self.pub_date}, текст:{self.text[:15]}.")


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(
        ADDING_DATE, auto_now_add=True, db_index=True)

    class Meta:
        ordering = ['-created']
        verbose_name = COMMENT_VERBOSE
        verbose_name_plural = COMMENTS_VERBOSE


class Follow(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="follower")
    following = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="following")

    class Meta:
        ordering = ['following']
        verbose_name = FOLLOW_VERBOSE
        verbose_name_plural = FOLLOWS_VERBOSE
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'], name='unique_follow')
        ]
