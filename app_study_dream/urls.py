from django.contrib import admin
from django.urls import path
from .views import *
from app_study_dream import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
#이거바꿔보자
urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'), # 접속 시, 로그인 페이지 등장
    path('list_page/', views.list_page, name='list_page'), # 로그인 성공 시, settings.py 에서 지정한 LOGIN_REDIRECT_URL 인 list_page/ 로 이동시 나오는 url 설정
    path('post/<int:id>', views.detail, name='detail'),
    path('write_post', views.write_post, name='write_post'),
]