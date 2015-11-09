from django.conf.urls import include, url
from post.views import LocationList

urlpatterns = [
    url(r'^locations/', LocationList.as_view()),

]

