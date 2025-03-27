# NewsApi/Urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from NewsApi.views import (
    CustomUserViewSet, CategoryViewSet, AuthorViewSet, ArticleViewSet,
    CommentViewSet, TagViewSet, LikeViewSet, SubscriberViewSet, 
    NewsletterViewSet, RegisterView, LoginView, LogoutView, 
    UserProfileView
)

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'articles', ArticleViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'tags', TagViewSet)
router.register(r'likes', LikeViewSet)
router.register(r'subscribers', SubscriberViewSet)
router.register(r'newsletters', NewsletterViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
    path('auth/profile/', UserProfileView.as_view(), name='profile'),
]