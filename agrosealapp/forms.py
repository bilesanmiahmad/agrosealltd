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
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'company name'}),
                           label='Company Name')
    contact_person = forms.ModelChoiceField(
        queryset=Person.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'contact person'}),
        label='Contact Person')
    contact_phone = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'phone number'}),
        label='Phone')
    contact_email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'}),
                                     label='Email')
    address = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'address'}),
                              label='Address')

    class Meta:
        model = Company
        fields = ['name',
                  'address',
                  'contact_phone',
                  'contact_email',
                  'contact_person']


class DriverCreateForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'first name'}),
                                 label='First Name')
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'last name'}),
                                label='Last Name')
    company = forms.ModelChoiceField(
        queryset=Company.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'company name'}),
        label='Company Name')
    contact_phone = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'phone number'}),
        label='Phone')
    contact_email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'}),
                                     label='Email')
    address = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'address'}),
                              label='Address')
    license_number = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'license number'}),
        label='License')
    referee = forms.ModelChoiceField(
        queryset=Person.objects.all(),
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'referee'}),
        label='Referee')

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
    driver = forms.ModelChoiceField(
        queryset=TruckDriver.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'driver'}),
        label='Driver')
    plate_number = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'plate number'}),
        label='Plate Number')
    vehicle_model = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'vehicle model'}),
        label='Vehicle Model')
    vehicle_type = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'vehicle type'}),
        label='Vehicle Type')

    class Meta:
        model = Truck
        fields = ['driver',
                  'plate_number',
                  'vehicle_model',
                  'vehicle_type']
