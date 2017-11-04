from django.shortcuts import render
from django.template import loader
from django.utils import timezone
from .models import *

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
    if request.method == 'GET':
        tags = Tag.objects.order_by('name')
        output = ", ".join([t.name for t in tags])
        template = loader.get_template('main/tags.html')
        context = {
            'output': output,
        }
        form = TagForm()
    else:
        form = TagForm(request.POST)
        if form.is_valid():

            tag = Tag.objects.create(
                name=form.cleaned_data['name'],
            )
            tag.save()

            return render(request, 'main/tags.html', {})

    return render(request, 'main/tags.html', {
        'form': form,
    })

def categories(request):
    if request.method == 'GET':
        categories = Category.objects.order_by('name')
        output = ", ".join([c.name for c in categories])
        template = loader.get_template('main/categories.html')
        context = {
            'output': output,
        }
        form = CategoryForm()
    else:
        form = CategoryForm(request.POST)
        if form.is_valid():

            category = Category.objects.create(
                name=form.cleaned_data['name'],
            )
            category.save()

            return render(request, 'main/categories.html', {})

    return render(request, 'main/categories.html', {
        'form': form,
    })

def points(request):
    if request.method == 'GET':
        points = Point.objects.order_by('name')
        output = ", ".join([p.amount for p in points])
        template = loader.get_template('main/points.html')
        context = {
            'output': output,
        }
        form = PointForm()
    else:
        form = PointForm(request.POST)
        if form.is_valid():

            point = Point.objects.create(
                amount=form.cleaned_data['amount'],
            )
            point.save()

            return render(request, 'main/points.html', {})

    return render(request, 'main/points.html', {
        'form': form,
    })

def leaderboard(request):
    return HttpResponse("Leaderboard")

def backlog(request):
    return HttpResponse("Backlog")

def story(request, story_id):
    return HttpResponse("Story")

def stories(request):
    if request.method == 'GET':
        stories = UserStory.objects.order_by('name')
        output = ", ".join([s.name for s in stories])
        template = loader.get_template('main/stories.html')
        context = {
            'output': output,
        }
        form = UserStoryForm()
    else:
        form = UserStoryForm(request.POST)
        if form.is_valid():

            story = UserStory.objects.create(
                sprint=form.cleaned_data['sprint'],
                role=form.cleaned_data['role'],
                feature=form.cleaned_data['feature'],
                benefit=form.cleaned_data['benefit'],
                category=form.cleaned_data['category'],
                owners=form.cleaned_data['owners'],
                tags=form.cleaned_data['tags'],
                required=form.cleaned_data['required'],
                points=form.cleaned_data['points'],
                due_date=form.cleaned_data['due_date'],
                created_date=form.cleaned_data['created_date'],
                last_updated_date=form.cleaned_data['last_updated_date'],
            )
            story.save()

            return render(request, 'main/stories.html', {})

    return render(request, 'main/stories.html', {
        'form': form,
    })

def sprint(request, sprint_id):
    return HttpResponse("Sprint")

def sprints(request):
    if request.method == 'GET':
        sprints = Sprint.objects.order_by('name')
        output = ", ".join([s.name for s in sprints])
        template = loader.get_template('main/sprints.html')
        context = {
            'output': output,
        }
        form = SprintForm()
    else:
        form = SprintForm(request.POST)
        if form.is_valid():

            sprint = Sprint.objects.create(
                name=form.cleaned_data['name'],
                start_date=form.cleaned_data['start_date'],
                due_date=form.cleaned_data['due_date'],
            )
            sprint.save()

            return render(request, 'main/sprints.html', {})

    return render(request, 'main/sprints.html', {
        'form': form,
    })

def user(request, user_id):
    return HttpResponse("User")

def users(request):
    if request.method == 'GET':
        users = User.objects.order_by('name')
        output = ", ".join([u.name for u in users])
        template = loader.get_template('main/users.html')
        context = {
            'output': output,
        }
        form = UserForm()
    else:
        form = UserForm(request.POST)
        if form.is_valid():

            user = User.objects.create(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
                admin=form.cleaned_data['admin'],
            )
            user.save()

            return render(request, 'main/users.html', {})

    return render(request, 'main/users.html', {
        'form': form,
    })

def release(request, release_id):
    return HttpResponse("Release")

def releases(request):
    if request.method == 'GET':
        releases = Release.objects.order_by('name')
        output = ", ".join([r.name for r in releases])
        template = loader.get_template('main/releases.html')
        context = {
            'output': output,
        }
        form = ReleaseForm()
    else:
        form = ReleaseForm(request.POST)
        if form.is_valid():

            release = Release.objects.create(
                name=form.cleaned_data['name'],
                start_date=form.cleaned_data['start_date'],
                due_date=form.cleaned_data['due_date'],
            )
            release.save()

            return render(request, 'main/releases.html', {})

    return render(request, 'main/releases.html', {
        'form': form,
    })

def retrospective(request, release_id):
    return HttpResponse("Release retrospective")

def roles(request):
    if request.method == 'GET':
        roles = Role.objects.order_by('name')
        output = ", ".join([r.name for r in roles])
        template = loader.get_template('main/roles.html')
        context = {
            'output': output,
        }
        form = RoleForm()
    else:
        form = RoleForm(request.POST)
        if form.is_valid():

            role = Role.objects.create(
                name=form.cleaned_data['name'],
            )
            role.save()

            return render(request, 'main/roles.html', {})

    return render(request, 'main/roles.html', {
        'form': form,
    })