from django import forms
from .models import Article, Author

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'author']

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']