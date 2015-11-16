
from django.utils import timezone
from django.views.generic import ListView
from users.models import Profile


class ListUsers(ListView):
    model = Profile
    queryset = Profile.objects.order_by('-posted_at')
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_load'] = timezone.now()
        return context
