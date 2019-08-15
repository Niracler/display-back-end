from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Article, Category


class CategorySerializer(serializers.ModelSerializer):
    """文章类别的序列化函数"""

    class Meta:
        model = Category
        fields = "__all__"


class ArticleSerializer(serializers.ModelSerializer):
    """文章的序列化函数"""

    class Meta:
        model = Article
        fields = "__all__"


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """用户的序列化函数"""

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    """用户组的序列化函数"""

    class Meta:
        model = Group
        fields = ['url', 'name']
