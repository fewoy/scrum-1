from django.db import models
from django.forms import ModelForm, Textarea, TextInput, DateInput, Select, SelectMultiple, ChoiceField, NumberInput
from django.contrib.auth.models import User

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

class Priority(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    rank = models.IntegerField()

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
    completed = models.BooleanField()
    priority = models.ForeignKey(Priority, db_index=True)
    due_date = models.DateField(null=True, db_index=True)
    created_date = models.DateTimeField(auto_now_add=True, editable=False, db_index=True)
    last_updated_date = models.DateTimeField(auto_now=True, editable=False, db_index=True)

    def __str__(self):
        return self.name

class StoryLog(models.Model):
    owner = models.ForeignKey(User, editable=False, db_index=True)
    story = models.ForeignKey(UserStory, editable=False, db_index=True)
    message = models.TextField(editable=False)
    created_date = models.DateTimeField(auto_now_add=True, editable=False, db_index=True)

    def __str__(self):
        return self.owner.username + " " + self.message

class UserStoryForm(ModelForm):
    class Meta:
        model = UserStory
        fields = '__all__'
        exclude = ['created_date', 'last_updated_date']
        widgets = {
            'name': TextInput(attrs={'class': 'mdl-textfield__input'}),
            'sprint': Select(attrs={'class': 'mdl-textfield__input'}),
            'role': Select(attrs={'class': 'mdl-textfield__input'}),
            'feature': Textarea(attrs={'class': 'mdl-textfield__input'}),
            'benefit': Textarea(attrs={'class': 'mdl-textfield__input'}),
            'category': Select(attrs={'class': 'mdl-textfield__input'}),
            'owners': SelectMultiple(attrs={'class': 'mdl-textfield__input'}),
            'tags': SelectMultiple(attrs={'class': 'mdl-textfield__input'}),
            'required': SelectMultiple(attrs={'class': 'mdl-textfield__input'}),
            'points': SelectMultiple(attrs={'class': 'mdl-textfield__input'}),
            'due_date': DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(UserStoryForm, self).__init__(*args, **kwargs)
        points = Point.objects.order_by("amount")
        point_list = [(p.amount, str(p.amount) + " hours") for p in points]
        self.fields['points'] = ChoiceField(choices=point_list)


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class RoleForm(ModelForm):
    class Meta:
        model = Role
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'mdl-textfield__input'}),
        }

class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'mdl-textfield__input'}),
        }

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'mdl-textfield__input'}),
        }

class ReleaseForm(ModelForm):
    class Meta:
        model = Release
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'mdl-textfield__input'}),
            'start_date': DateInput(attrs={'type': 'date'}),
            'due_date': DateInput(attrs={'type': 'date'}),
        }

class SprintForm(ModelForm):
    class Meta:
        model = Sprint
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'mdl-textfield__input'}),
            'release': Select(attrs={'class': 'mdl-textfield__input'}),
            'start_date': DateInput(attrs={'type': 'date'}),
            'due_date': DateInput(attrs={'type': 'date'}),
        }

class PriorityForm(ModelForm):
    class Meta:
        model = Priority
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'mdl-textfield__input'}),
            'rank': NumberInput(attrs={'class': 'mdl-textfield__input',
                                       'pattern': '[0-9]*'}),
        }

class PointForm(ModelForm):
    class Meta:
        model = Point
        fields = '__all__'
        widgets = {
            'amount': NumberInput(attrs={'class': 'mdl-textfield__input',
                                         'pattern': '[0-9]*'}),
        }