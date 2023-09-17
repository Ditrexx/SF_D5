from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.core.paginator import Paginator
from .filters import PostFilter
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required


# Create your views here.

class NewsList(ListView):
    model = Post
    template_name = 'newapp/news.html'
    context_object_name = 'news'
    ordering = ['-dateCreation']
    paginate_by = 10


class NewsSearchView(ListView):
    model = Post
    template_name = 'newapp/news_search.html'
    context_object_name = 'news'
    ordering = ['-dateCreation']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        context['choices'] = Post.CATEGORY_CHOISES
        context['form'] = PostForm()
        return context


# представление, в котором будут детали конкретного поста
class NewsDetailView(DetailView):
    template_name = 'newapp/news_detail.html'
    queryset = Post.objects.all()


# дженерик для создания объекта
class NewsCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'newapp/news_create.html'
    form_class = PostForm
    permission_required = ('newapp.add_post')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        return super().get(request, *args, **kwargs)


# дженерик для редактирования объекта
class NewsUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'newapp/news_create.html'
    form_class = PostForm
    permission_required = ('newapp.change_post')

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


# дженерик для удаления товара
class NewsDeleteView(DeleteView):
    template_name = 'newapp/news_delete.html'
    queryset = Post.objects.all()
    success_url = reverse_lazy('newapp:news')


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'newapp/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_author'] = not self.request.user.groups.filter(name='authors').exists()
        return context


@login_required
def upgrade_me(request):
    user = request.user
    authors_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        authors_group.user_set.add(user)
    return redirect('/')
