from django import forms
from tube_extension.models import Video

class VideoForm(forms.Form):
    title = forms.CharField()

    def save(self):
        data=self.cleaned_data
        video = Video(title=data['title'])
        video.save()