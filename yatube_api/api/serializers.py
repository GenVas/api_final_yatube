from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator

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
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=['following', 'user'],
                message=ALREADY_SUBSCRIBED_MESSAGE
            )
        ]

    # lazy evaluation technique
    # def validate(self, data):
    #     if (self.context['request'].method == 'POST'
    #             and self.context['request'].user == data['following']):
    #         raise serializers.ValidationError(NO_SELF_SUBSCRIPTION_MESSAGE)
    #     return data

    # bloack guard technique
    def validate(self, data):
        if self.context['request'].method != 'POST':
            return data
        if self.context['request'].user == data['following']:
            raise serializers.ValidationError(NO_SELF_SUBSCRIPTION_MESSAGE)
        return data
