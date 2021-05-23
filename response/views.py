from django.db.models.fields import GenericIPAddressField
from django.shortcuts import render
from rest_framework import generics

from .models import Thread, Board, Replies
from .serializers import ThreadSerializer, BoardSerializer


# THREADS

class ListThread(generics.ListCreateAPIView):

    def get_queryset(self):

        abbrev = self.kwargs['abbrev']
        print(abbrev)
        return Thread.objects.filter(board__abbrev=abbrev)

    # queryset = Thread.objects.all()
    serializer_class = ThreadSerializer


class DetailThread(generics.RetrieveUpdateDestroyAPIView):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer


###########################################################################

# INDIVIDUAL THREADS

class ListReplies(generics.ListCreateAPIView):

    def get_queryset(self):

        id = self.kwargs['id']
        print(id)
        return Replies.objects.filter(thread__id=id)

    # queryset = Thread.objects.all()
    serializer_class = ThreadSerializer


class DetailReplies(generics.RetrieveUpdateDestroyAPIView):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer

###########################################################################

# BOARDS


class ListBoard(generics.ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer


class DetailThreadBoard(generics.RetrieveUpdateDestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
