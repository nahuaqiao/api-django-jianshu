from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from django.http import HttpResponse
from articles.models import Article, Comment
from articles.serializers import ArticleSerializer, UserSerializer, CommentSerializer
from articles.permissions import IsOwnerOrReadOnly


from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from django.shortcuts import render


def views_login(request):
    return render(request, 'login.html')


def views_articles(request):
    return render(request, 'articles.html')



class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=User.objects.get(pk=self.request.user.id))


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    
#    def create(self, request, *args, **kwargs):
#        user = request.user
#        data = {
#            'user': user,
#            'article': kwargs['article_id'],
#            'content': request.POST['content']
#        }
#        _serializer = self.serializer_class(data=data)
#        if _serializer.is_valid():
#            _serializer.save()
#            return Response(data=_serializer.data, status=status.HTTP_201_CREATED)
#        else:
#            return Response(data=_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#    def perform_create(self, serializer, *args, **kwargs):
#        serializer.save(user=self.request.user)


    def create(self, request, *args, **kwargs):
        data = {
            'content': request.POST['content']
        }
        _serializer = self.serializer_class(data=data)
        if _serializer.is_valid():
            _serializer.save(user=User.objects.get(pk=request.user.id), article=Article.objects.get(pk=kwargs['article_id']))
        return Response(data=_serializer.data, status=status.HTTP_201_CREATED)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
  
