from datetime import timezone
from django.shortcuts import render
from django.views.generic import ListView


# class LocationList(ListView):
#     model = Location
#
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['page_load'] = timezone.now()
#         return context