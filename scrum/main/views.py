from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required
def home(request):

    return render(request, "main/home.html", {
        'title': "Home",
    })

@login_required
def tags(request):

    if request.method == 'GET':

        form = TagForm()
        tags = Tag.objects.order_by('name')

        return render(request, "main/tags.html", {
            'tags': tags,
            'form': form,
            'title': "Tags",
        })

    else:

        form = TagForm(request.POST)

        if form.is_valid():

            form.save()

            return HttpResponseRedirect("/tags/")

@login_required
def categories(request):

    if request.method == 'GET':

        form = CategoryForm()
        categories = Category.objects.order_by('name')

        return render(request, "main/categories.html", {
            'categories': categories,
            'form': form,
            'title': "Categories",
        })

    else:

        form = CategoryForm(request.POST)

        if form.is_valid():

            form.save()

            return HttpResponseRedirect("/categories/")

@login_required
def points(request):

    if request.method == 'GET':

        form = PointForm()
        points = Point.objects.order_by('amount')

        return render(request, "main/points.html", {
            'points': points,
            'form': form,
            'title': "Points",
        })

    else:

        form = PointForm(request.POST)

        if form.is_valid():

            form.save()

            return HttpResponseRedirect("/points/")

@login_required
def leaderboard(request):

    return render(request, "main/leaderboard.html", {
        'title': "Leaderboard",
    })

@login_required
def backlog(request):

    stories = UserStory.objects.order_by('name')

    if request.method == 'GET':

        form = UserStoryForm()

        return render(request, "main/backlog.html", {
            'stories': stories,
            'form': form,
            'title': "Backlog",
        })

    else:

        form = UserStoryForm(request.POST)

        if form.is_valid():

            form.save()

            return HttpResponseRedirect("/stories/")

@login_required
def priorities(request):

    priorities = Priority.objects.order_by('rank')

    if request.method == 'GET':

        form = PriorityForm()

        return render(request, "main/priorities.html", {
            'priorities': priorities,
            'form': form,
            'title': "Priorities",
        })

    else:

        form = PriorityForm(request.POST)

        if form.is_valid():

            form.save()

            return HttpResponseRedirect("/priorities/")

@login_required
def story(request, story_id):

    return render(request, "main/story.html", {
        'title': "Story",
    })

@login_required
def stories(request):

    stories = UserStory.objects.order_by('name')

    if request.method == 'GET':

        form = UserStoryForm()

        return render(request, "main/stories.html", {
            'output': stories,
            'form': form,
            'title': "Stories",
        })

    else:

        form = UserStoryForm(request.POST)

        if form.is_valid():

            form.save()

            return HttpResponseRedirect("/stories/")

@login_required
def sprint(request, sprint_id):

    return render(request, "main/sprint.html", {
        'title': "Sprint",
    })

@login_required
def sprints(request):

    if request.method == 'GET':

        form = SprintForm()
        sprints = Sprint.objects.order_by('name')

        return render(request, "main/sprints.html", {
            'sprints': sprints,
            'form': form,
            'title': "Sprints",
        })

    else:

        form = SprintForm(request.POST)

        if form.is_valid():

            form.save()

            return HttpResponseRedirect("/sprints/")

@login_required
def user(request, user_id):

    return render(request, "main/user.html", {
        'title': "User",
    })

@login_required
def users(request):

    if request.method == 'GET':

        form = UserForm()
        users = User.objects.order_by('username')

        return render(request, "main/users.html", {
            'users': users,
            'form': form,
            'title': "Users",
        })

    else:

        form = UserForm(request.POST)

        if form.is_valid():

            form.save()

            return HttpResponseRedirect("/users/")

@login_required
def release(request, release_id):

    return render(request, "main/release.html", {
        'title': "Release",
    })

@login_required
def releases(request):

    if request.method == 'GET':

        form = ReleaseForm()
        releases = Release.objects.order_by('name')

        return render(request, "main/releases.html", {
            'releases': releases,
            'form': form,
            'title': "Releases",
        })

    else:

        form = ReleaseForm(request.POST)

        if form.is_valid():

            form.save()

            return HttpResponseRedirect("/releases/")

@login_required
def retrospective(request, release_id):

    return render(request, "main/retrospective.html", {
        'title': "Retrospective",
    })

@login_required
def roles(request):

    if request.method == 'GET':

        form = RoleForm()
        roles = Role.objects.order_by('name')

        return render(request, "main/roles.html", {
            'roles': roles,
            'form': form,
            'title': "Roles",
        })

    else:

        form = RoleForm(request.POST)

        if form.is_valid():

            form.save()

            return HttpResponseRedirect("/roles/")

@login_required
def logout_page(request):

    logout(request)

    return HttpResponseRedirect("/login")