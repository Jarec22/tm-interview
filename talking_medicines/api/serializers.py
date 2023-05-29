from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'author',
            'author_flair_text',
            'author_flair_text_color',
            'body',
            'id',
            'permalink',
            'score',
            'subreddit',
        ]