from django import forms
from .models import Post
from django import forms
from django.contrib.auth.models import User, Group


class PostForm(forms.ModelForm):
    message = forms.Textarea()
    # group = forms.Select()
    group = forms.ModelChoiceField(queryset=Group.objects.all(),
                                   required=True)
    
    
    class Meta: 
        model = Post
        fields = ('message','group')
        
       
        widgets = {
            'message': forms.Textarea(attrs={'class':'form-control'}),
            
        }
        
        
