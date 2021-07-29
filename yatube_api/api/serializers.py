from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from posts.models import Comment, Group, Post, Follow, User


NO_SELF_SUBSCRIPTION_MESSAGE = 'Нельзя подписаться на самого себя'
ALREADY_SUBSCRIBED_MESSAGE = 'Вы уже подписаны'


class CommentSerializer(serializers.ModelSerializer):
    post = serializers.SlugRelatedField(read_only=True, slug_field='pk')
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username')

    class Meta:

        fields = '__all__'
        model = Comment


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    following = serializers.SlugRelatedField(
        slug_field='username', queryset=User.objects.all()
    )
    user = serializers.SlugRelatedField(
        slug_field='username', queryset=User.objects.all(),
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Follow
        fields = '__all__'

    def validate(self, data):
        user = self.context['request'].user
        following = data['following']
        if user == following:
            raise serializers.ValidationError(NO_SELF_SUBSCRIPTION_MESSAGE)
        if Follow.objects.filter(user=user, following=following).exists():
            raise serializers.ValidationError(ALREADY_SUBSCRIBED_MESSAGE)
        return data
