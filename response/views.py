from django.db.models.fields import GenericIPAddressField
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
import json

from .models import Thread, Board, Replies
from .serializers import ThreadSerializer, CreateThreadSerializer, BoardSerializer


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


# class DetailReplies(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Thread.objects.all()
#     serializer_class = ThreadSerializer

###########################################################################

# BOARDS


class ListBoard(generics.ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer


# class DetailThreadBoard(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Board.objects.all()
#     serializer_class = BoardSerializer

###########################################################################

# POSTS


class CreateThreadView(APIView):
    serializer = CreateThreadSerializer

    def post(self, request, format=None):

        ser = self.serializer(data=request.data)
        try:

            if ser.is_valid():
                # print(ser.errors)
                print(ser.data)
                board = ser.data['board']
                img = ser.data['img']
                content = ser.data['content']
                get_board = Board.objects.get(abbrev=board)
                print(img)
                thread = Thread(board=get_board, img=img, content=content)
                thread.save()
                print("thread saved")

                auto_reply = Replies(img=img, content=content, thread=thread)
                auto_reply.save()
                print("reply saved")

                return Response("Submitted thread")

            return Response(ser.errors)
        except Exception as e:
            print("error:", e)
            return Response("Error submiting")
