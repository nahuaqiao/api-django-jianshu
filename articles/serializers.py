from rest_framework import serializers
from articles.models import Article, Comment
from django.contrib.auth.models import User
from rest_framework.fields import CurrentUserDefault
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class ArticleSerializer(serializers.ModelSerializer):
   
    user = serializers.ReadOnlyField(source='owner.username')
    comments = serializers.SlugRelatedField(many=True, read_only=True, slug_field='content')

    class Meta:
        model = Article
        fields = ['id', 'title', 'content','cover', 'created', 'user', 'comments']


class CommentSerializer(serializers.ModelSerializer):
    
    article = serializers.ReadOnlyField(source='article.title')
    user = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Comment
        fields = ['id', 'content', 'article', 'user', 'created']


class UserSerializer(serializers.ModelSerializer):
#    articles = serializers.PrimaryKeyRelatedField(many=True, queryset=Article.objects.all())
#    comments = serializers.PrimaryKeyRelatedField(many=True, queryset=Comment.objects.all())
    
    class Meta:
        model = User
#        fields = ['id', 'username', 'email', 'password']
        fields = ['id', 'username']

"""
class RegisterSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(
    required=True,
    validators=[UniqueValidator(queryset=User.objects.all())]
  )
  password = serializers.CharField(
    write_only=True, required=True, validators=[validate_password])
  password2 = serializers.CharField(write_only=True, required=True)
  class Meta:
    model = User
    fields = ('username', 'password', 'password2',
         'email', 'first_name', 'last_name')
    extra_kwargs = {
      'first_name': {'required': True},
      'last_name': {'required': True}
    }
  def validate(self, attrs):
    if attrs['password'] != attrs['password2']:
      raise serializers.ValidationError(
        {"password": "Password fields didn't match."})
    return attrs
  def create(self, validated_data):
    user = User.objects.create(
      username=validated_data['username'],
      email=validated_data['email'],
      first_name=validated_data['first_name'],
      last_name=validated_data['last_name']
    )
    user.set_password(validated_data['password'])
    user.save()
    return user

"""
