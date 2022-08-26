from django.urls import path
from rest_framework_simplejwt.views import (TokenVerifyView, TokenObtainPairView, TokenRefreshView,)
from articles.views import ArticleViewSet, UserViewSet, CommentViewSet
from articles.views import *

article_list = ArticleViewSet.as_view({ 'get': 'list', 'post': 'create'})

article_detail = ArticleViewSet.as_view({ 'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy' })


comment_list = CommentViewSet.as_view({ 'get': 'list', 'post': 'create' })

user_list = UserViewSet.as_view({ 'post': 'create' })

urlpatterns = [
    path('api/articles/', article_list, name='article-list'),
    path('api/articles/<int:pk>/', article_detail, name='article-detail'),
    path('api/articles/<int:article_id>/comments/', comment_list, name='comment-list'),
    # path('api/articles/verify/<str:title>/', article_title_exist, name='article_title_exist'),
    path('api/users/', user_list, name='user-list'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('views/login/', views_login, name='views_login'),
    path('views/register/', views_register, name='views_register'),
    path('views/articles/', views_articles, name='views_articles'),
    path('views/articles/post/', views_post_article, name='views_post_article'),
    path('views/articles/<int:article_id>/', views_single_article, name='views_single_article'),
    path('views/articles/<int:article_id>/edit/',views_edit_article, name='views_edit_article'),
]
