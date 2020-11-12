from django.urls import path, include
from .views import my_view, post_list
from django.conf.urls import url
from . import views as s, views
from django.conf.urls.static import static
from django.conf import settings

from .views import (
    BlogDeleteView,
)



urlpatterns = [
    path('', my_view, name='my-view'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post_author/', views.post_author, name='post_author'),
    path('post/<int:pk>/delete/',BlogDeleteView.as_view(), name='post_delete'),
    path('post/new/', views.post_new, name='post_new'),
    #path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup', s.signup, name='signup'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


