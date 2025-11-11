from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('',views.post_list,name="blog_list"),
    path('<slug:post>', views.post_detail, name='blog_detail')
]
