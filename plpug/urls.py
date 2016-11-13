from django.conf.urls import url
from .views import IndexView, ContactView, MeetingsView, MembersView, HistoryView, PartnersView,\
    ProjectsView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^members$', MembersView.as_view(), name='members'),
    url(r'^meetings$', MeetingsView.as_view(), name='meetings'),
    url(r'^projects$', ProjectsView.as_view(), name='projects'),
    url(r'^history$', HistoryView.as_view(), name='history'),
    url(r'^partners$', PartnersView.as_view(), name='partners'),
    url(r'^contact$', ContactView.as_view(), name='contact'),
]
