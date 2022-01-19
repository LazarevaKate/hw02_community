from django.shortcuts import render, get_object_or_404

from .models import Post, Group

POST_COUNT = 10


def index(request):
    posts = Post.objects.order_by()[:POST_COUNT]
    context = {
        'text': "Это главная страница проекта Yatube",
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


    class Meta:
        ordering = ['-pub_date']


def group_posts(request, slug):
    """Здесь будет информация о группах проекта Yatube."""
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by()[:POST_COUNT]
    context = {
        'text': "Здесь будет информация о группах проекта Yatube",
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)

