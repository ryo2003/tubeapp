from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('video/<pk>', views.WatchVideoView.as_view(), name="detail"),
    path("", login_required(views.VideoFormView.as_view()), name="index"),

    
    ]