from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from rest_framework import routers
from .views import UserViewSet

app_name = 'common'

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('', include(router.urls)),
]