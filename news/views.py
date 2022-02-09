from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView
)
from django.db.models import Count
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import User, News, Article, Review, Category
from .permissions import IsOwnerProfileOrReadOnly, IsAuthorOrReadOnly
from .serializers import (
    ProfileSerializer,
    NewsSerializer,
    NewsDetailSerializer,
    CategoryDetailSerializer,
    ArticleSerializer,
    ArticleDetailSerializer,
    ReviewSerializer,
    ReviewDetailSerializer
)


class UserProfileListCreateView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


class ProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerProfileOrReadOnly, IsAuthenticated]


class CategoryDetailViews(ListCreateAPIView):
    queryset = Category.objects.annotate(
        cnt=Count('news__title',
                  distinct=True) + Count('article__title',
                                         distinct=True) + Count('review__title',
                                                                distinct=True)).values('name', 'cnt')
    serializer_class = CategoryDetailSerializer


class NewsListView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsDetailView(RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = News.objects.all()
    serializer_class = NewsDetailSerializer


class CreateNewsView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = NewsSerializer
    queryset = News.objects.all()

    def perform_create(self, serializer):
        author = self.request.user
        serializer.save(user=author)


class EditNewsView(UpdateAPIView):
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    serializer_class = NewsSerializer
    queryset = News.objects.all()


class DeleteNewsView(DestroyAPIView):
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    serializer_class = NewsSerializer
    queryset = News.objects.all()


class ArticleListView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetailView(RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer


class CreateArticleView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

    def perform_create(self, serializer):
        author = self.request.user
        serializer.save(user=author)


class EditArticleView(UpdateAPIView):
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


class DeleteArticleView(DestroyAPIView):
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


class ReviewListView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewDetailView(RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = Review.objects.all()
    serializer_class = ReviewDetailSerializer


class CreateReviewView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()

    def perform_create(self, serializer):
        author = self.request.user
        serializer.save(user=author)


class EditReviewView(UpdateAPIView):
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()


class DeleteReviewView(DestroyAPIView):
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
