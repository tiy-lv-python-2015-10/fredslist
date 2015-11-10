"""fredslist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from fredslist import settings
from peteslist.forms import ContactForm1, ContactForm2
from peteslist.views import LocationList, LocationListHome, ForSalePost, \
    AddImage, ListPosts, PostDetail, CategoryListPosts
from users.views import Register



urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^locations/', include('peteslist.urls')),
    url(r'^register/', Register.as_view(), name='register'),
    url(r'^logout/', 'django.contrib.auth.views.logout',
        {'next_page': "/locations/"}, name='logout'),
    url('^', include('django.contrib.auth.urls')),
    url(r'^loc/$', LocationListHome.as_view(), name='locs_list'),
    url(r'^post/$', login_required(ForSalePost.as_view()) , name='post'),
    url(r'^post/(?P<pk>\d+)/$', PostDetail.as_view(), name='post_detail'),
    # url(r'^contact/$', ContactWizard.as_view(FORMS)),
    url(r'^image/', 'peteslist.views.add_image', name='add_image'),
    url(r'^postings/$', ListPosts.as_view(), name="list_posts"),
    url(r'^okay/(?P<category>\w+)/$', CategoryListPosts.as_view(),
        name='category_posts'),
    # url(r'^postings/(?P<category>\w+)/$', CategoryListPosts.as_view(),
    #     name='category_posts')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
