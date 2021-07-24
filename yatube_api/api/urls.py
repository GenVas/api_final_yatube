from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, GroupViewSet, PostViewSet

router = DefaultRouter()

router.register('posts', PostViewSet, basename='posts')
router.register('groups', GroupViewSet, basename='groups')
router.register(
    'posts/(?P<post_id>\\d+)/comments',
    CommentViewSet, basename='comments')
urlpatterns = [
    # path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/', include(router.urls)),
]


urlpatterns += [
    # Djoser создаст набор необходимых эндпоинтов.
    # базовые, для управления пользователями в Django:
    path('v1/auth/', include('djoser.urls')),
    # JWT-эндпоинты, для управления JWT-токенами:
    path('v1/auth/', include('djoser.urls.jwt')),
]
