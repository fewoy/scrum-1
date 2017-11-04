from django.db import models
from django.forms import ModelForm

class Role(models.Model):
    name = models.CharField(max_length=200)

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)

class Tag(models.Model):
    name = models.CharField(max_length=200, db_index=True)

class Point(models.Model):
    amount = models.IntegerField()

class Release(models.Model):
    name = models.CharField(max_length=200, unique=True)
    start_date = models.DateField(null=True, db_index=True)
    due_date = models.DateField(null=True, db_index=True)

class Sprint(models.Model):
    name = models.CharField(max_length=200, unique=True)
    release = models.ForeignKey(Release)
    due_date = models.DateField(null=True, db_index=True)
    start_date = models.DateField(null=True, db_index=True)

class User(models.Model):
    username = models.CharField(max_length=200, unique=True, db_index=True)
    email = models.CharField(max_length=200, unique=True, db_index=True)
    password = models.CharField(max_length=200)
    admin = models.BooleanField(default=False, editable=False, db_index=True)
    def __str__(self):
        return self.username

class UserStory(models.Model):
    name = models.CharField(max_length=200)
    sprint = models.ForeignKey(Sprint, null=True, db_index=True)
    role = models.ForeignKey(Role, db_index=True)
    feature = models.TextField()
    benefit = models.TextField()
    category = models.ForeignKey(Category, db_index=True)
    owners = models.ManyToManyField(User, db_index=True)
    tags = models.ManyToManyField(Tag, db_index=True)
    required = models.ManyToManyField("self", db_index=True)
    points = models.IntegerField()
    due_date = models.DateField(null=True, db_index=True)
    created_date = models.DateTimeField(auto_now_add=True, editable=False, db_index=True)
    last_updated_date = models.DateTimeField(auto_now=True, editable=False, db_index=True)

class StoryLog(models.Model):
    owner = models.ForeignKey(User, editable=False, db_index=True)
    story = models.ForeignKey(UserStory, editable=False, db_index=True)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True, editable=False, db_index=True)
    def __str__(self):
        return self.owner.username + " " + self.message

class UserStoryForm(ModelForm):
    class Meta:
        model = UserStory
        fields = '__all__'
        exclude = ['created_date', 'last_updated_date']