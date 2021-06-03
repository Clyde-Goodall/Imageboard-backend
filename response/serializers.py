from rest_framework import serializers
from .models import Thread, Board, Replies


class ThreadSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'content',
            'id',
            'img',
            'time',
            'reply_count',
            'img_count',
            'watch_count',
            'board',
        )

        model = Thread


class CreateThreadSerializer(serializers.ModelSerializer):
    board = serializers.CharField(max_length=5)
    img = serializers.ImageField()

    class Meta:
        fields = (
            'board',
            'img',
            'content',
        )

        model = Thread


class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'content',
            'img',
            'time',
        )

        model = Replies


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'abbrev',
        )

        model = Board
