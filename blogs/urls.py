from django.conf.urls import include, url
from django.conf import settings

from . import views

urlpatterns = [
    url(r'^blog-list/', views.BlogList.as_view(), name='blog-list'),
    url(r'^blog/', views.Blog.as_view(), name='blog'),
    url(r'^comment/', views.Comment.as_view(), name='comment'),
]