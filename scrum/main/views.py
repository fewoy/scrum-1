from django.shortcuts import render, redirect
from django.utils import timezone
from .models import *
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

@login_required
def index(request):
    users = User.objects.order_by('username')
    output = ", ".join([u.username for u in users])
    context = {
        'output': output,
        'title': "Home",
    }
    return render(request, "main/index.html", context)

@login_required
def tags(request):
    tags = Tag.objects.order_by('name')
    output = ", ".join([t.name for t in tags])

    if request.method == 'GET':
        form = TagForm()
        context = {
            'output': output,
            'form': form,
            'title': "Tags",
        }

        return render(request, "main/tags.html", context)
    else:
        form = TagForm(request.POST)
        if form.is_valid():

            tag = Tag.objects.create(
                name=form.cleaned_data['name'],
            )
            tag.save()

            return HttpResponseRedirect("/tags/")

@login_required
def categories(request):
    categories = Category.objects.order_by('name')
    output = ", ".join([t.name for t in categories])

    if request.method == 'GET':
        form = CategoryForm()
        context = {
            'output': output,
            'form': form,
            'title': "Categories",
        }

        return render(request, "main/categories.html", context)
    else:
        form = CategoryForm(request.POST)
        if form.is_valid():

            category = Category.objects.create(
                name=form.cleaned_data['name'],
            )
            category.save()

            return HttpResponseRedirect("/categories/")

@login_required
def points(request):
    points = Point.objects.order_by('amount')
    output = ", ".join([str(p.amount) for p in points])

    if request.method == 'GET':
        form = PointForm()
        context = {
            'output': output,
            'form': form,
            'title': "Points",
        }

        return render(request, "main/points.html", context)
    else:
        form = PointForm(request.POST)
        if form.is_valid():

            point = Point.objects.create(
                amount=form.cleaned_data['amount'],
            )
            point.save()

            return HttpResponseRedirect("/points/")

@login_required
def leaderboard(request):
    return HttpResponse("Leaderboard")

@login_required
def backlog(request):
    return HttpResponse("Backlog")

@login_required
def story(request, story_id):
    return HttpResponse("Story")

@login_required
def stories(request):
    stories = UserStory.objects.order_by('name')
    output = ", ".join([s.name for s in stories])

    if request.method == 'GET':
        form = UserStoryForm()
        context = {
            'output': output,
            'form': form,
            'title': "Stories",
        }

        return render(request, "main/stories.html", context)
    else:
        form = UserStoryForm(request.POST)
        if form.is_valid():

            story = UserStory.objects.create(
                name=form.cleaned_data['name'],
                sprint=form.cleaned_data['sprint'],
                role=form.cleaned_data['role'],
                feature=form.cleaned_data['feature'],
                benefit=form.cleaned_data['benefit'],
                category=form.cleaned_data['category'],
                points=form.cleaned_data['points'],
                due_date=form.cleaned_data['due_date'],
                created_date=timezone.now,
                last_updated_date=timezone.now,
            )
            story.save()
            # ManyToMany relationships must be added after story is persisted
            story.required.add(form.cleaned_data['required'])
            story.owners.add(form.cleaned_data['owners'])
            story.tags.add(form.cleaned_data['tags'])

            return HttpResponseRedirect("/stories/")

@login_required
def sprint(request, sprint_id):
    return HttpResponse("Sprint")

@login_required
def sprints(request):
    sprints = Sprint.objects.order_by('name')
    output = ", ".join([s.name for s in sprints])

    if request.method == 'GET':
        form = SprintForm()
        context = {
            'output': output,
            'form': form,
            'title': "Sprints",
        }

        return render(request, "main/sprints.html", context)
    else:
        form = SprintForm(request.POST)
        if form.is_valid():

            sprint = Sprint.objects.create(
                name=form.cleaned_data['name'],
                release=form.cleaned_data['release'],
                start_date=form.cleaned_data['start_date'],
                due_date=form.cleaned_data['due_date'],
            )
            sprint.save()

            return HttpResponseRedirect("/sprints/")

@login_required
def user(request, user_id):
    return HttpResponse("User")

@login_required
def users(request):
    users = User.objects.order_by('username')
    output = ", ".join([u.username for u in users])

    if request.method == 'GET':
        form = UserForm()
        context = {
            'output': output,
            'form': form,
            'title': "Users",
        }

        return render(request, "main/users.html", context)
    else:
        form = UserForm(request.POST)
        if form.is_valid():

            user = User.objects.create(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                email=form.cleaned_data['email'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
            )
            user.save()

            return HttpResponseRedirect("/users/")

@login_required
def release(request, release_id):
    return HttpResponse("Release")

@login_required
def releases(request):
    releases = Release.objects.order_by('name')
    output = ", ".join([r.name for r in releases])

    if request.method == 'GET':
        form = ReleaseForm()
        context = {
            'output': output,
            'widget_type_map': WIDGET_TYPE_TO_CLASS,
            'form': form,
            'title': "Releases",
        }

        return render(request, "main/releases.html", context)
    else:
        form = ReleaseForm(request.POST)
        if form.is_valid():

            release = Release.objects.create(
                name=form.cleaned_data['name'],
                start_date=form.cleaned_data['start_date'],
                due_date=form.cleaned_data['due_date'],
            )
            release.save()

            return HttpResponseRedirect("/releases/")

@login_required
def retrospective(request, release_id):
    return HttpResponse("Release retrospective")

@login_required
def roles(request):
    roles = Role.objects.order_by('name')
    output = ", ".join([r.name for r in roles])

    if request.method == 'GET':
        form = RoleForm()
        context = {
            'output': output,
            'form': form,
            'title': "Roles",
        }

        return render(request, "main/roles.html", context)
    else:
        form = RoleForm(request.POST)
        if form.is_valid():

            role = Tag.objects.create(
                name=form.cleaned_data['name'],
            )
            role.save()

            return HttpResponseRedirect("/roles/")

@login_required
def logout_page(request):
    logout(request)

    return HttpResponseRedirect("/login")