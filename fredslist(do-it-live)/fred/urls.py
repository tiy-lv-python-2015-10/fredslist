from django.conf.urls import include, url
from django.contrib import admin
from fred.views import LocationListView

urlpatterns = [
    url(r'^$', 'fred.views.index'),
    url(r'^fred/', include('fred.urls'),
    url(r'^$', LocationListView.as_view()),
]