from django.core.urlresolvers import reverse, reverse_lazy
from django.forms import formset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.views.generic import ListView, View, CreateView, DetailView
from formtools.wizard.views import SessionWizardView
import peteslist
from peteslist.forms import ForSaleForm, ImageForm
from peteslist.models import Location, Type, Category, Image, Post
from django.utils import timezone


class LocationList(ListView):
    model = Location

    def dispatch(self, request, *args, **kwargs):
        try:
            city = self.request.session.get('location')
            return HttpResponseRedirect(reverse('temp_only', kwargs={'city': city}))
        except Exception as e:
            return super(LocationList, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        state_list = []
        context = super().get_context_data(**kwargs)
        for location in Location.objects.all():
            if location.state not in state_list:
                state_list.append(location.state)
        context['page_load'] = timezone.now()
        context['states1'] = state_list[0:13]
        context['states2'] = state_list[13:26]
        context['states3'] = state_list[26:39]
        context['states4'] = state_list[39:]
        return context


class LocationListHome(ListView):
    model = Location
    template_name = 'peteslist/location_home.html'

    def get_context_data(self, **kwargs):
        state_list = []
        context = super().get_context_data(**kwargs)
        for location in Location.objects.all():
            if location.state not in state_list:
                state_list.append(location.state)
        context['page_load'] = timezone.now()
        context['states1'] = state_list[:13]
        context['states2'] = state_list[13:26]
        context['states3'] = state_list[26:39]
        context['states4'] = state_list[39:]
        return context


def loc(request, city):

    community1 = Category.objects.filter(type__title='community')[:7]
    community2 = Category.objects.filter(type__title='community')[7:]
    housing = Category.objects.filter(type__title='housing')
    for_sale1 = Category.objects.filter(type__title='for sale')[:19]
    for_sale2 = Category.objects.filter(type__title='for sale')[19:]
    services1 = Category.objects.filter(type__title='services')[:10]
    services2 = Category.objects.filter(type__title='services')[10:]
    jobs = Category.objects.filter(type__title='jobs')
    gigs1 = Category.objects.filter(type__title='gigs')[:4]
    gigs2 = Category.objects.filter(type__title='gigs')[4:]
    # col1 = [Type.objects.all().order_by('pk')[0]]
    # col2 = Type.objects.all().order_by('pk')[1:4]
    # col3 = Type.objects.all().order_by('pk')[4:6]
    # b = Category.objects.all().order_by('title')
    # c = Category.objects.filter(type__title='housing')
    context_dict = {'community1': community1, 'community2': community2,
                    'housing': housing, 'for_sale1': for_sale1,
                    'for_sale2': for_sale2, 'services1': services1,
                    'services2': services2, 'jobs': jobs,
                    'gigs1': gigs1, 'gigs2': gigs2, 'city': city}
    # {'city': city, 'col1': col1, 'col2': col2, 'col3': col3,
    #          'categories': b, 'poo': c}
    request.session['location'] = city
    return render(request, 'peteslist/zzz.html', context_dict)

class ForSalePost(View):

    def get(self, request):
        form = ForSaleForm()
        return render(request, 'peteslist/post.html', {'form': form})

    def post(self, *args, **kwargs):
        form = ForSaleForm(self.request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.user = self.request.user
            post.location = self.request.session.get('location')
            self.request.session['post'] = post.title
            post.save()

            return HttpResponseRedirect(reverse('add_image'))

        return render(self.request, 'peteslist/post.html', {'form': form})

class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        b = self.object.image_set.all()
        context['images'] = b
        return context

class ListPosts(ListView):
    """ List of all Bookmarks ordered by the most popular """
    model = Post
    paginate_by = 20

    def get_queryset(self):
        return Post.objects.filter(location=self.request.session.get('location'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_load'] = timezone.now()
        self.queryset = Post.objects.filter(location=self.request.session.get('location'))
        images = []
        for post in self.queryset:
            images.append(post.image_set.all()[0])
        context['images'] = images
        return context

class CategoryListPosts(ListView):
    """ List of all Bookmarks ordered by the most popular """
    model = Post
    paginate_by = 20
    template_name = 'peteslist/post_list_category.html'

    def get_queryset(self, **kwargs):
        a = self.kwargs['category']
        return Post.objects.filter(location=self.request.session.get('location')).filter(category__title=a)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_load'] = timezone.now()
        a = self.kwargs['category']
        b = Post.objects.filter(location=self.request.session.get('location')).filter(category__title=a)
        images = []
        for post in b:
            images.append(post.image_set.all()[0])
        context['images'] = images
        return context


class AddImage(CreateView):
    model = Image
    form_class = ImageForm
    success_url = reverse_lazy('locs_list')

    def form_valid(self, form):
        return super(AddImage, self).form_valid(form)


def add_image(request):
    ImageFormSet = formset_factory(ImageForm, extra=5)
    if request.method == 'POST':
        formset = ImageFormSet(request.POST, request.FILES)
        if formset.is_valid():
            for form in formset:
                if form.is_valid():
                    image = form.save(commit=False)
                    if image.image:
                        image.post = \
                            Post.objects.get(title=request.session.get('post'))
                        image.save()
        return HttpResponseRedirect(reverse('locs_list'))
    else:
        formset = ImageFormSet()
    return render(request, 'peteslist/add_image.html', {'formset': formset})


# FORMS = [("address", myapp.forms.AddressForm),
#          ("paytype", myapp.forms.PaymentChoiceForm),
#          ("cc", myapp.forms.CreditCardForm),
#          ("confirmation", myapp.forms.OrderForm)]
#
# TEMPLATES = {"address": "checkout/billingaddress.html",
#              "paytype": "checkout/paymentmethod.html",
#              "cc": "checkout/creditcard.html",
#              "confirmation": "checkout/confirmation.html"}
#
# def pay_by_credit_card(wizard):
#     """Return true if user opts to pay by credit card"""
#     # Get cleaned data from payment step
#     cleaned_data = wizard.get_cleaned_data_for_step('paytype') or {'method': 'none'}
#     # Return true if the user selected credit card
#     return cleaned_data['method'] == 'cc'
#
#
# class OrderWizard(SessionWizardView):
#     def get_template_names(self):
#         return [TEMPLATES[self.steps.current]]
# TEMPLATES = {
#     'one': 'peteslist/aaa.html',
#     'two': 'peteslist/bbb.html'
# }
#
# FORMS = [
#     ('one', peteslist.forms.CategoryStep1),
#     ('two', peteslist.forms.CategoryStep2)
# ]
#
#
# class ContactWizard(SessionWizardView):
#
#     def get_form_initial(self, step):
#         return{
#             '0': {'title': 'hello'},
#             '1': {'type': None}
#         }
#
#     def get_form_instance(self, step):
#         if self.instance is None:
#             self.instance = Category()
#         return self.instance
#
#     def done(self, form_list, **kwargs):
#         return render_to_response('peteslist/done.html',
#                                   {'form_data': [form.cleaned_data
#                                                  for form in form_list],})
#     def get_template_names(self):
#         return[TEMPLATES[self.steps.current]]