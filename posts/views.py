from django.views.generic import CreateView, DeleteView, ListView
from django.urls import reverse_lazy
from .models import Post, Comment
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CommentForm
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import PostForm

from django.db.models import Q


class PostListView(ListView):
    model = Post
    template_name = 'posts/home.html'
    queryset = Post.objects.all()

    def get_queryset(self, *args, **kwargs): # this ordered my list view last to first
        qs = super(PostListView, self).get_queryset(*args, **kwargs)
        qs = qs.order_by("-id")
        return qs


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_new.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'posts/post_delete.html'
    success_url = reverse_lazy('home')


#######################################
## Functions that require a pk match ##
#######################################
# def home_view(request):
#     qs = Post.objects.all()
#     context = {
#         'queryset_list': qs,
#     }
#     return render(request, 'home.html', context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    is_favourite = False
    if post.favourite.filter(pk=request.user.pk).exists():
        is_favourite = True
    is_bookmark = False
    if post.bookmark.filter(pk=request.user.pk).exists():
        is_bookmark = True
    context = {
        'post': post,
        'is_favourite': is_favourite,
        'is_bookmark': is_bookmark,
        'total_favourites': post.total_favourites(),
    }
    return render(request, "posts/post_detail.html", context)


def search(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(content__icontains=query)
        )
        results = Post.objects.filter(qset).distinct()
    else:
        results = []
    # template = "search.html"
    context = {
        "results": results,
        "query": query
    }
    return render(request, "posts/search.html", context)


def favourite_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.favourite.filter(pk=request.user.pk).exists():
        post.favourite.remove(request.user)
    else:
        post.favourite.add(request.user)
    return HttpResponseRedirect(post.get_absolute_url())


def bookmark_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.bookmark.filter(pk=request.user.pk).exists():
        post.bookmark.remove(request.user)
    else:
        post.bookmark.add(request.user)
    return HttpResponseRedirect(post.get_absolute_url())


def bookmark_post_list(request):
    user = request.user
    bookmark_posts = user.bookmark.all()
    context = {
        'bookmark_posts': bookmark_posts,
    }
    return render(request, 'posts/bookmark_post_list.html', context)


@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('home')
    else:
        form = CommentForm()
    return render(request, 'posts/comment_new.html', {'form': form})


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    # post_pk = comment.post.pk
    comment.delete()
    return redirect('home')
