from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Index")

def tags(request):
    return HttpResponse("Tags")

def categories(request):
    return HttpResponse("Categories")

def points(request):
    return HttpResponse("Points")

def leaderboard(request):
    return HttpResponse("Leaderboard")

def product_backlog(request):
    return HttpResponse("Product backlog")

def retrospective(request, release_id):
    return HttpResponse("Release retrospective")

def story(request, story_id):
    return HttpResponse("Story")

def sprint(request, sprint_id):
    return HttpResponse("Sprint")

def users(request):
    return HttpResponse("Users")

def user(request, user_id):
    return HttpResponse("User")

def release(request, release_id):
    return HttpResponse("Release")