from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.views.generic import ListView, DeleteView, UpdateView, DetailView, CreateView
from .models import Post, Comment
from .forms import PostForm, CommentForm, TagForm
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


class PostList(ListView):
    model = Post
    ordering = '-pk'

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q', '')
        if q:
            qs = qs.filter(title__icontains=q)
        return qs

post_list = PostList.as_view()


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('reading_blog:post_list')
    template_name = 'reading_blog/form.html'

    def form_valid(self, form):
        video = form.save(commit=False)
        video.author = self.request.user
        return super().form_valid(form)

post_new = PostCreate.as_view()


class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context
    
    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        post = Post.objects.get(pk=pk)
        post.view_count += 1
        post.save()
        return super().get_object(queryset)

post_detail = PostDetail.as_view()


class PostUpdate(UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('reading_blog:post_list')
    template_name = 'reading_blog/form.html'

    def test_func(self):
        return self.get_object().author == self.request.user

post_edit = PostUpdate.as_view()


class PostDelete(UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('reading_blog:post_list')

    def test_func(self):
        return self.get_object().author == self.request.user

post_delete = PostDelete.as_view()


@login_required
def comment_new(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('reading_blog:post_detail', pk)
    else:
        form = CommentForm()
    return render(request, 'reading_blog/form.html', {
        'form': form,
    })


def posttag(request, tag):
    posts = Post.objects.filter(tags__name__iexact=tag)
    return render(request, 'reading_blog/post_list.html', {'post_list': posts, 'tag': tag})