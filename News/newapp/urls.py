# from django.urls.resolvers import URLPattern
from django.urls import path
from .views import *

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>/', PostDetail.as_view(), name='post_page'),
    path('search/', PostSearch.as_view(), name='search'),
    path('add/', PostCreate.as_view(), name='post_create'),
    path('edit/<int:pk>/', PostUpdate.as_view(), name='post_update'),
    path('delete/<int:pk>/', PostDelete.as_view(), name='post_delete'),
    path('<int:pk>/add_subscribe/', add_subscribe, name='add_subscribe'),
    path('<int:pk>/del_subscribe/', del_subscribe, name='del_subscribe'),
    ]
