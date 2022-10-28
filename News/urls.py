from django.urls import path
from django.views.generic import RedirectView
from .views import *

urlpatterns = [

   path('', PostList.as_view(), name= 'post_list'),
   path('<int:pk>', PostDetail.as_view(), name = 'post_detail'),
   path('create/', PostCreate.as_view(), name = 'post_create'),
   path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('search/', PostSearcher.as_view(), name='post_search'),
   path('articles/create/', PostCreate.as_view(), name='articles_create'),
   path('articles/<int:pk>/edit/', PostUpdate.as_view(), name='articles_edit'),
   path('articles/<int:pk>/delete/', PostDelete.as_view(), name='articles_delete'),


]


