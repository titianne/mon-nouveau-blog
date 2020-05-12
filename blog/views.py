from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') #les posts (querysets) rangés par date de publication
    return render(request, 'blog/post_list.html', {'posts':posts})   #a view on post_list html file ,request=tout ce qui est reçu de la part ,un utilisateur via internet

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
# Create your views here.
