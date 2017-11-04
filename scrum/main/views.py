from django.shortcuts import render
from django.template import loader
from django.utils import timezone
from .models import User, UserStory, UserStoryForm

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
    if request.method == 'GET':
        form = UserStoryForm()
    else:
        form = UserStoryForm(request.POST)
        if form.is_valid():
            sprint = form.cleaned_data['sprint']
            role = form.cleaned_data['role']
            feature = form.cleaned_data['feature']
            benefit = form.cleaned_data['benefit']
            category = form.cleaned_data['category']
            owners = form.cleaned_data['owners']
            tags = form.cleaned_data['tags']
            required = form.cleaned_data['required']
            points = form.cleaned_data['points']
            due_date = form.cleaned_data['due_date']
            created_date = timezone.now()
            last_updated_date = timezone.now()

            story = UserStory.objects.create(
                sprint=sprint,
                role=role,
                feature=feature,
                benefit=benefit,
                category=category,
                owners=owners,
                tags=tags,
                required=required,
                points=points,
                due_date=due_date,
                created_date=created_date,
                last_updated_date=last_updated_date,
            )
            story.save()

            return render(request, 'main/stories.html', {})

    return render(request, 'main/stories.html', {
        'form': form,
    })

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