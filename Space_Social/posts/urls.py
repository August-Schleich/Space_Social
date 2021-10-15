
from django.views.generic.edit import DeleteView 
from . import views
from django.urls import path,include 



app_name = 'posts'

urlpatterns = [
    path('',views.PostList.as_view(),name='all'),
    path('new/',views.CreatePost.as_view(),name='create'),
    path('by/(?p<username>[-\w+]',views.UserPosts.as_view(),name='for_user'),
    path('by/(?p<username>[-\w+](?p<pk>\d+)/$',views.PostDetail.as_view(),name='single'),
    path('delete/(?p<pk>\d+)/$',views.DeletePost.as_view(),name='delete'),
]