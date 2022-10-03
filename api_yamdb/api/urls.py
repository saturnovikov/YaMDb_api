from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (CategoryViewSet, CommentViewSet, GenresViewSet,
                       ReviewViewSet, TitleViewSet, UserViewSet, signup, token)

router_v1 = DefaultRouter()

router_v1.register('users', UserViewSet, basename='users')
router_v1.register('categories', CategoryViewSet, basename='categories')
router_v1.register('genres', GenresViewSet, basename='genres')
router_v1.register('titles', TitleViewSet, basename='titles')
router_v1.register(
    r'titles\/(?P<title_id>\d+)/reviews',
    ReviewViewSet, basename='reviews'
)
router_v1.register(
    r'titles\/(?P<title_id>\d+)/reviews\/(?P<review_id>\d+)/comments',
    CommentViewSet, basename='comments'
)

jwt_patterns = [
    path('signup/', signup, name='signup'),
    path('token/', token, name='token')
]

urlpatterns = [
    path('', include(router_v1.urls)),
    path('auth/', include(jwt_patterns)),
]
