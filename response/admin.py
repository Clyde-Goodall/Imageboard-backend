from django.contrib import admin
from .models import Thread, Board, Replies

admin.site.register(Thread)
admin.site.register(Board)
admin.site.register(Replies)
