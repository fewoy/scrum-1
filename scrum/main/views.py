from django.shortcuts import render
from django.template import loader
from .models import User

from django.http import HttpResponse


def index(request):
    users = User.objects.order_by('username')
    output = ", ".join([u.username for u in users])
    template = loader.get_template('main/index.html')
    context = {
        'output': output,
    }
    return HttpResponse(template.render(context, request))

def tags(request):
    return HttpResponse("Tags")

def categories(request):
    return HttpResponse("Categories")

def points(request):
    return HttpResponse("Points")

def leaderboard(request):
    return HttpResponse("Leaderboard")

def backlog(request):
    return HttpResponse("Backlog")

def story(request, story_id):
    return HttpResponse("Story")

def stories(request):
    return HttpResponse("Stories")

def sprint(request, sprint_id):
    return HttpResponse("Sprint")

def sprints(request):
    return HttpResponse("Sprints")

def user(request, user_id):
    return HttpResponse("User")

def users(request):
    return HttpResponse("Users")

def release(request, release_id):
    return HttpResponse("Release")

def releases(request):
    return HttpResponse("Releases")

def retrospective(request, release_id):
    return HttpResponse("Release retrospective")