from django.contrib import admin
from django.urls import path
from . import views
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# from django.conf.urls import url
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


urlpatterns = [
    path('', views.index, name='index'), # путь к главной странице сайта
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #path(r'^login/$', views.user_login, name='login'),
    path(r'^register/$', views.register, name='register')
    path('login/', 'django.contrib.auth.views.login', name='login'),
    path('logout/', 'django.contrib.auth.views.logout_view', name='logout'),
    path('logout-then-login/', 'django.contrib.auth.views.logout_then_login', name='logout_then_login'),
    path(r'^$', views.dashboard, name='dashboard'),
    path('password-change/', 'django.contrib.auth.views.password_change', name='password_change'),
    path('password-change/done/$', 'django.contrib.auth.views.password_change_done', name='password_change_done')
    path('movies_choice/', views.choose_movies(), name='movies')
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
]
