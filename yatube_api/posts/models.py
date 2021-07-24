from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, related_name='posts', blank=True, null=True)
    
    class Meta:
        ordering = ['-pub_date']
    
    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)

    class Meta:
        ordering = ['-created']

# В проекте должна быть описана модель Follow,
# в ней должно быть два поля — user (кто подписан) и following (на кого подписан).
# Для этой модели в документации уже описан эндпоинт /follow/ и два метода:


class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="follower") # (кто подписан)
    following = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="following") # (на кого подписан)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['following', 'follower'], name='unique_follow')
        ]


class CommentPost(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.comment} {self.post}'
