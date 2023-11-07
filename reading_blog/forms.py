from django import forms
from .models import Post, Comment, Tag

class PostForm(forms.ModelForm):
    title = forms.CharField(label="제목", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label="내용", widget=forms.Textarea(attrs={'class': 'form-control'}))
    image_upload = forms.ImageField(label="이미지 업로드", required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,)
    
    class Meta:
        model = Post
        fields = ['title', 'content', 'image_upload', 'tags']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message']


class TagForm(forms.ModelForm):
    name = forms.ModelChoiceField(
        queryset=Tag.objects.all(),
        empty_label="Select a tag",
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="태그"
    )

    class Meta:
        model = Tag
        fields = ['name']





