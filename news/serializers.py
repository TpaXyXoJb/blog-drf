from rest_framework import serializers
from .models import User, News, Article, Review, Category
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class ProfileSerializer(serializers.ModelSerializer):
    description = serializers.CharField(max_length=128)
    image = serializers.ImageField()

    class Meta:
        model = User
        fields = ['username', 'email', 'description', 'image', ]


class NewsSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField("username", read_only=True)

    class Meta:
        model = News
        fields = ['title', 'image', 'publish_date', 'author']


class NewsDetailSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)

    class Meta:
        model = News
        fields = "__all__"


class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField("username", read_only=True)

    class Meta:
        model = Article
        fields = ['title', 'image', 'publish_date', 'author']


class ArticleDetailSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)

    class Meta:
        model = Article
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField("username", read_only=True)

    class Meta:
        model = News
        fields = ['title', 'image', 'publish_date', 'author']


class ReviewDetailSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)

    class Meta:
        model = Review
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class CategoryDetailSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=128)
    cnt = serializers.CharField()

    class Meta:
        model = Category
        fields = "__all__"
