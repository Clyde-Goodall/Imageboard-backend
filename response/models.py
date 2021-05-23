from django.db import models


def upload_to(instance, filename):
    return 'thread_img/{filename}'.format(filename=filename)


class Board(models.Model):

    name = models.CharField(max_length=50, unique=True)
    abbrev = models.CharField(max_length=4, unique=True)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.abbrev


class Thread(models.Model):
    # thread content will be added as initial commetn instead
    content = models.CharField(max_length=500, blank=True, default='')
    img = models.ImageField(null=False, upload_to=upload_to)
    time = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, default=1)
    reply_count = models.IntegerField(default=0)
    img_count = models.IntegerField(default=0)
    watch_count = models.IntegerField(default=0)

    def __str__(self):
        return self.content


class Replies(models.Model):
    content = models.CharField(max_length=500, blank=False, default='')
    img = models.ImageField(blank=True, default='')
    time = models.DateTimeField(auto_now_add=True)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.content
