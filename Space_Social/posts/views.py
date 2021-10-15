from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
# Create your views here.
from django.http import Http404
from django.views import generic

from braces.views import SelectRelatedMixin 

from . import forms 
from django.contrib.auth import get_user_model
User = get_user_model()



class PostList(SelectRelatedMixin,generic.ListView):
    pass
    
