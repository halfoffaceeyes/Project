"""
URL configuration for crud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.get_categories),
    path('categories/create/', views.create_category),
    path('categories/<int:category_pk>/delete/', views.delete_category),
    path('posts/', views.get_posts),
    path('post/<int:post_pk>/', views.get_post_item),
    path('comments/', views.get_comments),
    path('post/<int:post_pk>/comments/', views.create_comments),
    path('post/<int:post_pk>/comment/<int:comment_pk>/', views.delete_comment),
]
