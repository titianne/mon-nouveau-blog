from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_list.html', {})   #a view on post_list html file 

# Create your views here.
