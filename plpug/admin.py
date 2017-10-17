from django.contrib import admin
from .models import News
from .models import Event

admin.site.register(Event)
admin.site.register(News)
