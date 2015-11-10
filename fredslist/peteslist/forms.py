from django import forms
from django.forms import MultipleChoiceField, ChoiceField
from peteslist.models import Post, Category, Image

CONTACT_CHOICES = (
    ('by_phone', 'By Phone'),
    ('by_text', 'By Text')
    )

class ForSaleForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('type', 'category', 'by_phone', 'by_text', 'phone_number',
                  'contact_name', 'title', 'price', 'specific_location',
                  'description', 'manufacturer', 'model_name', 'serial_num',
                  'dimensions', 'condition')

        widgets = {
            # 'type': forms.TextInput(attrs={'class': 'required'}),
            # 'category': forms.TextInput(attrs={'class': 'required'}),
            # 'title': forms.TextInput(attrs={'class': 'required'}),
            # 'description': forms.TextInput(attrs={'class': 'required'}),
            # 'by_phone': forms.CheckboxInput(attrs={'class': 'optional'}),
            # 'by_text': forms.CheckboxInput(attrs={'class': 'optional'}),
            # 'phone_number': forms.CheckboxInput(attrs={'class': 'optional'}),
            # 'contact_name': forms.CheckboxInput(attrs={'class': 'optional'}),
            # 'price': forms.CheckboxInput(attrs={'class': 'optional'}),
            # 'specific_location': forms.CheckboxInput(attrs={'class': 'optional'}),
            # 'manufacturer': forms.CheckboxInput(attrs={'class': 'optional'}),
            # 'model_name': forms.CheckboxInput(attrs={'class': 'optional'}),
            # 'serial_num': forms.CheckboxInput(attrs={'class': 'optional'}),
            # 'dimensions': forms.CheckboxInput(attrs={'class': 'optional'}),
            # 'condition': forms.CheckboxInput(attrs={'class': 'optional'})
            # # 'by_phone': forms.BooleanField(attrs={'class': 'form_control'})
        }

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image',)

class CategoryStep1(forms.Form):
    class Meta:
        model = Category
        fields = ['title',]

class CategoryStep2(forms.Form):
    class Meta:
        model = Category
        fields = ['type',]

class ContactForm1(forms.Form):
    subject = forms.CharField(max_length=100)
    sender = forms.EmailField()

class ContactForm2(forms.Form):
    message = forms.CharField(widget=forms.Textarea)

#     CONTACT_CHOICES = (
#     ('by phone', 'By Phone'),
#     ('by text', 'By Text')
#     )
#
#     CONDITION_CHOICES = (
#     ('new', 'New'),
#     ('like new', 'Like New'),
#     ('excellent', 'Excellent'),
#     ('good', 'Good'),
#     ('fair', 'Fair'),
#     ('salvage', 'Salvage'),
#     ('other', 'Other')
#     )
#
#
# class ForSaleForm(forms.Form):
#     class Meta:
#         pass
#
#     contact_by = MultipleChoiceField(required=False,
#                                      widget=forms.CheckboxSelectMultiple,
#                                      choices=CONTACT_CHOICES)
#     condition = ChoiceField(required=False,
#                             widget=forms.Select, choices=CONDITION_CHOICES)