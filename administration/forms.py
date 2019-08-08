from django import forms
from website.models import FlashInfo, Article, User

class FlashInfoForm(forms.ModelForm):
    class Meta:
        model = FlashInfo
        fields = ('title', 'content')

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'content')

class UserLocationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('longitude', 'latitude')