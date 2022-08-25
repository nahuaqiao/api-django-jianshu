from django.urls import path
# from articles.views import UserDetailAPI, RegisterUserAPIView
from articles.views import ArticleViewSet, UserViewSet, CommentViewSet
from articles.views import views_login, views_articles

article_list = ArticleViewSet.as_view({ 'get': 'list', 'post': 'create'})

article_detail = ArticleViewSet.as_view({ 'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy' })


comment_list = CommentViewSet.as_view({ 'get': 'list', 'post': 'create' })

user_list = UserViewSet.as_view({ 'get': 'list', 'post': 'create' })
user_detail = UserViewSet.as_view({ 'get': 'retrieve' })

urlpatterns = [
    path('', views_login),
    path('views_articles/', views_articles),
    path('articles/', article_list, name='article-list'),
    path('articles/<int:pk>/', article_detail, name='article-detail'),
    path('articles/<int:article_id>/comments/', comment_list, name='comment-list'),
    path('users/', user_list, name='user-list'),
  #  path('register/', RegisterUserAPIView.as_view()),
]
