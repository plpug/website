from django.conf.urls import url
from .views import IndexView, EventsListView, ContactView, MeetingsView, MembersView, \
    HistoryView, PartnersView, ProjectsView, MicrobitView, agree_on_cookie_store, NewsView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^members$', MembersView.as_view(), name='members'),
    url(r'events$',  EventsListView.as_view(), name='events'),
    # url(r'^meetings$', MeetingsView.as_view(), name='meetings'),
    url(r'^projects$', ProjectsView.as_view(), name='projects'),
    # url(r'^history$', HistoryView.as_view(), name='history'),
    url(r'^partners$', PartnersView.as_view(), name='partners'),
    url(r'^contact$', ContactView.as_view(), name='contact'),
    url(r'^microbit$', MicrobitView.as_view(), name='microbit'),
    url(r'^agree-on-cookie-store$', agree_on_cookie_store, name='agree_on_cookie_store'),
    url(r'^news$', NewsView.as_view(), name='news'),

]
