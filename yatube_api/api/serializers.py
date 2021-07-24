from rest_framework import serializers
from rest_framework.fields import CharField
from rest_framework.relations import SlugRelatedField


from posts.models import Comment, CommentPost, Group, Post, Follow


class CommentSerializer(serializers.ModelSerializer):
    post = serializers.SlugRelatedField(read_only=True, slug_field='pk')
    author = serializers.SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        fields = '__all__'
        model = Comment


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)
    # text = CharField(required=True)
    comments = CommentSerializer(many=True, required=False)

    class Meta:
        fields = '__all__'
        model = Post

    def create(self, validated_data):
        if 'comments' not in self.initial_data:
            post = Post.objects.create(**validated_data)
            return post
        else:
            comments = validated_data.pop('comments')
            post = Post.objects.create(**validated_data)
            for comment in comments:
                current_comment, status = Comment.objects.get_or_create(
                    **comments)
                CommentPost.objects.create(
                    comment=current_comment, post=post)
            return post


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = '__all__'
