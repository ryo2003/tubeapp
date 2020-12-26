from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.VideoFormView.as_view(), name="index"),
    path('video/<pk>', views.WatchVideoView.as_view(), name="detail")
    
    ]