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
from rest_framework.decorators import api_view

def views_login(request):
    return render(request, 'login.html')

def views_register(request):
    return render(request, 'register.html')

def views_articles(request):
    return render(request, 'articles.html')

def views_post_article(request):
    return render(request, 'post_article.html')

def views_single_article(request, article_id):
    context = { 'article_id': article_id }
    return render(request, 'single_article.html', context)

def views_edit_article(request, article_id):
    context = { 'article_id': article_id }
    return render(request, 'edit_article.html', context)


# view & api split ==========================================================================
# @api_view(('GET',))
# def article_title_exist(self, title):
# # try:
#     articles = list(Article.objects.filter(title=title).values())
#     if len(articles) == 0:
#         return Response(data={ "exist": False }, status=status.HTTP_200_OK)
#     # finally:
#     return Response(data={ "exist": True }, status=status.HTTP_200_OK)


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

    def create(self, request, article_id=None):
        data = {
            # 'content': request.POST.get('content')
            'content': request.POST['content']
        }
        _serializer = self.serializer_class(data=data)
        if _serializer.is_valid():
            _serializer.save(user=User.objects.get(pk=self.request.user.id), article=Article.objects.get(pk=article_id))
        print(_serializer.data)
        return Response(data=_serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request, article_id=None):
        queryset = Comment.objects.filter(article_id=article_id)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request):
        data = {
                'username': request.POST['username'],
                'email': request.POST['email'],
                'password': request.POST['password'],
        }
        _serializer = self.serializer_class(data=data)
        if _serializer.is_valid():
            _serializer.save()
        return Response(data=_serializer.data, status=status.HTTP_201_CREATED)





















