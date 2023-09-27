from django.shortcuts import render
from .models import Post
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic import (
    ListView,
    DetailView,
    FormView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .forms import PostForm
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
)


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "Ali"
        context["posts"] = Post.objects.all()
        return context

class PostListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    # model = Post
    queryset = Post.objects.all()
    permission_required = "blog.view_post"
    context_object_name = "posts"
    # paginate_by = 2
    ordering = ["id"]

    # def get_queryset(self):
    #     posts = Post.objects.filter(status=True)
    #     return posts


class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post


"""
class PostCreateView(FormView):
    form_class = PostForm
    template_name = 'contact.html'
    success_url = '/blog/post/'
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
"""


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    success_url = "/blog/post/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostEditView(UpdateView):
    model = Post
    form_class = PostForm
    success_url = "/blog/post/"


class PostDeleteView(DeleteView):
    model = Post
    success_url = "/blog/post/"
