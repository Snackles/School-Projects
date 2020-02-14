from .forms import CommentForm
from .models import Comment
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers


import json


# Create your views here.
def index(request):
        context = {}
        return render(request, 'templates/TestApp/index.html', context)


def add_comment(request):
    comments = Comment.objects.all().filter(visible=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Save the comment to the database
            new_comment.save()
            return HttpResponseRedirect("show_comments")
    comment_form = CommentForm()
    return render(request, 'templates/TestApp/add_comment.html', {'comment_form': comment_form})


def show_comments(request):
    comments = Comment.objects.all().filter(visible=True)
    return render(request, 'templates/TestApp/show_comments.html', {'comments': comments})


def get_comments(request):
    data = serializers.serialize('json', Comment.objects.all())
    return HttpResponse(data)
