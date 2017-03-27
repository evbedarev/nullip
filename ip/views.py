from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def post_list(request):
    object_list = Post.objects.order_by('-intstates')

    paginator = Paginator(object_list, 50)

    page = request.GET.get('page')

    try:
        posts = paginator.page(page)

    except PageNotAnInteger:
        posts = paginator.page(1)
    return render(request,
                  'ip/post/list.html',
                  {'page': page,
                   'posts': posts})


# Create your views here.