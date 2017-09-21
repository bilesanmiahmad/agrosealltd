from django.forms import ModelForm
from django import forms
from .models import Person, TruckDriver, Company, Truck


class PersonCreateForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'first name'}),
                                 label='First Name')
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'last name'}),
                                label='Last Name')
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'phone number'}),
                            label='Phone')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'}),
                             label='Email')
    address = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'address'}),
                              label='Address')

    class Meta:
        model = Person
        fields = ['first_name',
                  'last_name',
                  'phone',
                  'email',
                  'address']


class CompanyCreateForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name',
                  'address',
                  'contact_phone',
                  'contact_email',
                  'contact_person']


class DriverCreateForm(forms.ModelForm):
    class Meta:
        model = TruckDriver
        fields = ['first_name',
                  'last_name',
                  'phone',
                  'email',
                  'address',
                  'license_number',
                  'company',
                  'referee']


class TruckCreateForm(forms.ModelForm):
    class Meta:
        model = Truck
        fields = ['driver',
                  'plate_number',
                  'vehicle_model',
                  'vehicle_type']
