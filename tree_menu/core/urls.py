from django.urls import path, re_path
from django.conf import settings
from . import views


urlpatterns = [
    re_path(rf'^{settings.MENU_URL_PREFIX}', views.get_menu, name='get-menu'),
    path('check/', views.check_menu, name='check-menu'),
]
