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
        output = ", ".join([t.name for t in tags])

        return render(request, "main/tags.html", {
            'output': output,
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
        output = ", ".join([t.name for t in categories])

        return render(request, "main/categories.html", {
            'output': output,
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
        output = ", ".join([str(p.amount) for p in points])

        return render(request, "main/points.html", {
            'output': output,
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

    return render(request, "main/backlog.html", {
        'title': "Backlog",
    })

@login_required
def story(request, story_id):

    return render(request, "main/story.html", {
        'title': "Story",
    })

@login_required
def stories(request):

    stories = UserStory.objects.order_by('name')
    output = ", ".join([s.name for s in stories])

    if request.method == 'GET':

        form = UserStoryForm()

        return render(request, "main/stories.html", {
            'output': output,
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
        output = ", ".join([s.name for s in sprints])

        return render(request, "main/sprints.html", {
            'output': output,
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
        output = ", ".join([u.username for u in users])

        return render(request, "main/users.html", {
            'output': output,
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
        output = ", ".join([r.name for r in releases])

        return render(request, "main/releases.html", {
            'output': output,
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
        output = ", ".join([r.name for r in roles])

        return render(request, "main/roles.html", {
            'output': output,
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