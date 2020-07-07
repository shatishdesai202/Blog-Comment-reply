from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('blog/', views.blog, name="blog"),
    path('search/', views.search, name="search"),
    path('postpage/<id>/', views.postPage, name="postpage"),
    path('handleLogin/', views.handleLogin, name="handleLogin"),
    path('handleSignup/', views.handleSignup, name="handleSignup"),
    path('handleLogout/', views.handleLogout, name="handleLogout"),
   
]
