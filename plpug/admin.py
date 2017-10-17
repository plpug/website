from django.contrib import admin

from .models import Event, News, Project

admin.site.register(Event)
admin.site.register(News)
admin.site.register(Project)
