from django import forms
from .models import Post, Comment

'''These are the post form and comment form models'''

class PostForm(forms.ModelForm):
	
	class Meta:
		model = Post
		fields = ('title', 'text')
		
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)