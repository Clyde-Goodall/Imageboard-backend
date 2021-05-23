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
        )

        model = Thread


class ReplySerializer(serializers.ModelSerializer):
    class meta:
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
