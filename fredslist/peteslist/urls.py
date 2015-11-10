from django.conf.urls import url
from peteslist.views import LocationList, LocationListHome, ForSalePost, \
    PostDetail

urlpatterns = [
    url(r'^$', LocationList.as_view(), name='list_locations'),
    # url(r'^post/$', ForSalePost.as_view() , name='post'),
    url(r'^(?P<city>.+)/$', 'peteslist.views.loc', name='temp_only'),
]