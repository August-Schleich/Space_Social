from django import forms
from .models import Post
from django import forms
from django.contrib.auth.models import User, Group
from . import models
from django.db import models


class PostForm(forms.ModelForm):
    message = forms.Textarea()
    group = forms.Select()

    required=True
    
    

    class Meta: 
        model = Post
        fields = ('message','group')
       

 
    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        if user is not None:
            self.fields["group"].queryset = models.Group.objects.filter(members = user)
        
