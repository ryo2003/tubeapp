from django.shortcuts import render


# Create your views here.

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from tube_extension.models import Video

# ListViewは一覧を簡単に作るためのView, video_list.html を探す
class Index(ListView):
    # 一覧するモデルを指定 -> `object_list`で取得可能
    model = Video


class Detail(DetailView):  #video_detail.html を探す
    model = Video
    
class Create(CreateView): #video_form.html を探す
    # Post用の投稿フォームが{{ form.as_p }}で自動的に生成されます。
    model = Video
    #template_name = "tube_extension/video_list.html"  # この行でテンプレート指定
    fields = ["title", "link"]
    
class Delete(DeleteView):#video_confirm_delete.html を探す
    model = Video
    success_url = "/"
    