from django.contrib import admin

from .models import User
from .models import Category
from .models import Tag
from .models import Point

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Point)