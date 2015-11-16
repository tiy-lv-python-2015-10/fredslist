from post.models import Location
from django.views.generic import ListView


class LocationList(ListView):
    model = Location
    template_name = "post/post_list.html"
    queryset = Location.objects.all().order_by('state')
