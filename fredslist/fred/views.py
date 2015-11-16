from django.views.generic.list import ListView
from django.utils import timezone
from fred.models import Category, SubCategory, Post, Location
from django.shortcuts import render_to_response
from django.template import RequestContext

class CategoryListView(ListView):

    model = Category

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class SubCategoryListView(ListView):

    model = SubCategory

    def get_context_data(self, **kwargs):
        context = super(SubCategoryListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class PostListView(ListView):

    model = Post


class LocationListView(ListView):

    model = Location
    template_name = "fred/fred_list.html"


def index(request):
    return render_to_response('fred/index.html', context_instance=RequestContext(request))

