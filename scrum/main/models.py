from django.db import models
from django.forms import ModelForm, TextInput
from django.contrib.auth.models import User

WIDGET_TYPE_TO_CLASS = {
    "text": "textfield"
}

class Role(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    def __str__(self):
        return self.name

class Point(models.Model):
    amount = models.IntegerField()
    def __str__(self):
        return self.amount

class Release(models.Model):
    name = models.CharField(max_length=200, unique=True)
    start_date = models.DateField(null=True, db_index=True)
    due_date = models.DateField(null=True, db_index=True)
    def __str__(self):
        return self.name

class Sprint(models.Model):
    name = models.CharField(max_length=200, unique=True)
    release = models.ForeignKey(Release)
    start_date = models.DateField(null=True, db_index=True)
    due_date = models.DateField(null=True, db_index=True)
    def __str__(self):
        return self.name

class UserStory(models.Model):
    name = models.CharField(max_length=200)
    sprint = models.ForeignKey(Sprint, null=True, db_index=True)
    role = models.ForeignKey(Role, db_index=True)
    feature = models.TextField()
    benefit = models.TextField()
    category = models.ForeignKey(Category, db_index=True)
    owners = models.ManyToManyField(User, db_index=True, blank=True)
    tags = models.ManyToManyField(Tag, db_index=True, blank=True)
    required = models.ManyToManyField("self", db_index=True, blank=True)
    points = models.IntegerField()
    due_date = models.DateField(null=True, db_index=True)
    created_date = models.DateTimeField(auto_now_add=True, editable=False, db_index=True)
    last_updated_date = models.DateTimeField(auto_now=True, editable=False, db_index=True)
    def __str__(self):
        return self.name

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

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class RoleForm(ModelForm):
    class Meta:
        model = Role
        fields = '__all__'

class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class ReleaseForm(ModelForm):
    class Meta:
        model = Release
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'mdl-textfield__input'}),
            'start_date': TextInput(attrs={'class': 'mdl-textfield__input'}),
            'due_date': TextInput(attrs={'class': 'mdl-textfield__input'}),
        }

class SprintForm(ModelForm):
    class Meta:
        model = Sprint
        fields = '__all__'

class PointForm(ModelForm):
    class Meta:
        model = Point
        fields = '__all__'