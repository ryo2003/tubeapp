from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from tube_extension.models import Video

# ListViewは一覧を簡単に作るためのView, video_list.html を探す
class Index(ListView):
    # 一覧するモデルを指定 -> `object_list`で取得可能
    model = Video

class Detail(DetailView):
    model = Video