from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import  (
    ProfileDetailView,
    CategoryDetailViews,
    NewsListView,
    NewsDetailView,
    CreateNewsView,
    EditNewsView,
    DeleteNewsView,
    ArticleListView,
    CreateArticleView,
    ArticleDetailView,
    EditArticleView,
    DeleteArticleView,
    ReviewListView,
    ReviewDetailView,
    CreateReviewView,
    EditReviewView,
    DeleteReviewView
)

urlpatterns = [
    # gets all user profiles and create a new profile
    # retrieves profile details of the currently logged in user
    path("profile/<int:pk>", ProfileDetailView.as_view(), name="profile"),

    path("news", NewsListView.as_view(), name="news"),
    path("news/<int:pk>", NewsDetailView.as_view(), name="news_detail"),
    path("news/create", CreateNewsView.as_view(), name="news_create"),
    path("news/edit/<int:pk>", EditNewsView.as_view(), name="news_edit"),
    path("news/delete/<int:pk>", DeleteNewsView.as_view(), name="news_delete"),

    path("article", ArticleListView.as_view(), name="article"),
    path("article/<int:pk>", ArticleDetailView.as_view(), name="article_detail"),
    path("article/create", CreateArticleView.as_view(), name="article_create"),
    path("article/edit/<int:pk>", EditArticleView.as_view(), name="article_edit"),
    path("article/delete/<int:pk>", DeleteArticleView.as_view(), name="article_delete"),

    path("review", ReviewListView.as_view(), name="review"),
    path("review/<int:pk>", ReviewDetailView.as_view(), name="review_detail"),
    path("review/create", CreateReviewView.as_view(), name="review_create"),
    path("review/edit/<int:pk>", EditReviewView.as_view(), name="review_edit"),
    path("review/delete/<int:pk>", DeleteReviewView.as_view(), name="review_delete"),


    path("category/detail/", CategoryDetailViews.as_view(), name="category_detail")
]
