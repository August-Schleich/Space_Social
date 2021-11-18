from django import forms
from .models import Post



class PostForm(forms.ModelForm):
    class Meta: 
        model = Post
        fields = ('message','group')
        
        widgets = {
            'message': forms.Textarea(attrs={'class':'form-control'}),
            'groups': forms.Select(attrs={'class':'form-control'})
        }