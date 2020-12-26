from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index.as_view(), name="index"),
    path('detail/<pk>', views.Detail.as_view(), name="detail"),
    path('create', views.Create.as_view(), name="create"),
    path('delete/<pk>', views.Delete.as_view(), name="delete"),
    
    ]