from django.urls import path
from .views import *

urlpatterns = [
    path('', AboutApiview.as_view(), name='about'),
    path('userr/', UserrApiView.as_view(), name='user'),
    path('category/', CategoryApiView.as_view(), name='category'),
    path('profile/', ProfileApiView.as_view(), name='profile'),
    path('team/', TeamApiView.as_view(), name='team'),
    path('books/', BooksApiView.as_view(), name='books'),
    path('social_media/', SocialMediaApiView.as_view(), name='social_media'),
]
