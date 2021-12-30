from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import Http404
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse
from braces.views import SelectRelatedMixin
from .forms import PostForm
from . import forms
from . import models
 
from django.contrib.auth import get_user_model
User = get_user_model()


class PostList(SelectRelatedMixin, generic.ListView):
    model = models.Post
    select_related = ("user", "group")
    ordering = ['-created_at']
  


class UserPosts(generic.ListView):
    model = models.Post
    select_related = ("user", "group")
    template_name = "posts/user_post_list.html"
    ordering = ['-created_at']
    
    def get_queryset(self):
       
        try:
            self.post_user = User.objects.prefetch_related("posts").get(
                username__iexact=self.kwargs.get("username")
            )
        except User.DoesNotExist:
            raise Http404
        else:
            qr =  self.post_user.posts.order_by('-created_at')
            return qr.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_user"] = self.post_user
        return context


class PostDetail(SelectRelatedMixin, generic.DetailView):
    model = models.Post
    select_related = ("user", "group")
    ordering = ['-created_at']
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
            user__username__iexact=self.kwargs.get("username")
        )


class CreatePost(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    model = models.Post
    form_class= forms.PostForm
    select_related = ("user", "group")
    username = 'username'
    success_url = reverse_lazy("posts:all")
    
    #     kwargs = super().get_form_kwargs()
    #     kwargs.update({"user": self.request.user})
    #     return kwargs

    




    def form_valid(self, form):
        
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        if self.object.user in self.object.group.members.iterator():
            self.object.save()
            return super().form_valid(form)
        else:
            messages.warning(self.request, 'Not a member of this group!')
        return self.form_invalid(form)
  
        

class DeletePost(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
    model = models.Post
    select_related = ("user", "group")
    success_url = reverse_lazy("posts:all" )
    

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Post Deleted")
        return super().delete(*args, **kwargs)
     
    
 