from rest_framework import routers
from django.urls import include, path
from rest_framework.authtoken import views

from api.views import PostViewSet, CommentViewSet, GroupViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comment'
)
router.register(r'groups', GroupViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token),
]
