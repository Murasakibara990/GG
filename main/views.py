from rest_framework import generics
from .models import (Comment,
                     Userr,
                     Profile,
                     About,
                     Team,
                     ScoialMedia,
                     Books,
                     Category)

from .seri import (CommentSerializer,
                   AboutSerializer,
                   UserrSerializer,
                   TeamSerializer,
                   ProfileSerializer,
                   CategorySerializer,
                   BooksSerializer,
                   SocialMediaSerializer)


class CommentApiView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class UserrApiView(generics.ListCreateAPIView):
    queryset = Userr.objects.all()
    serializer_class = UserrSerializer


class AboutApiview(generics.ListCreateAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class ProfileApiView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class CategoryApiView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SocialMediaApiView(generics.ListCreateAPIView):
    queryset = ScoialMedia.objects.all()
    serializer_class = SocialMediaSerializer


class BooksApiView(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


class TeamApiView(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
