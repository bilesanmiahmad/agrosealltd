import json

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin

# from agrosealapp.devless import Sdk
from agrosealapp.models import Person, Truck, TrackDevice, TruckDriver, TrackEvent, Trip, TruckRequest, Company
from agrosealapp.forms import PersonCreateForm, CompanyCreateForm, DriverCreateForm, TruckCreateForm
# Create your views here.


class PersonListView(generic.ListView):
    model = Person
    template_name = 'agrosealapp/person_list.html'
    context_object_name = 'person_list'


class PersonDetailView(generic.DetailView):
    model = Person
    template_name = 'agrosealapp/person-detail.html'
    context_object_name = 'person'


class PersonCreateView(generic.CreateView):
    form_class = PersonCreateForm
    template_name = 'agrosealapp/person_create_form.html'
    success_url = '/persons/'


class PersonUpdateView(generic.UpdateView):
    model = Person
    fields = ['first_name', 'last_name', 'phone', 'email', 'address']
    template_name = 'agrosealapp/person_create_form.html'
    success_url = '/persons/'


class PersonDeleteView(generic.DeleteView):
    model = Person
    success_url = '/persons/'
    template_name_suffix = '_delete_form'


class DriverListView(LoginRequiredMixin, generic.ListView):
    model = TruckDriver
    template_name = 'agrosealapp/driver_list.html'
    context_object_name = 'driver_list'


class DriverDetailView(LoginRequiredMixin, generic.DetailView):
    model = TruckDriver
    template_name = 'agrosealapp/driver-detail.html'
    context_object_name = 'driver'


class DriverCreateView(generic.CreateView):
    form_class = DriverCreateForm
    template_name = 'agrosealapp/driver_create_form.html'
    success_url = '/drivers/'


class DriverUpdateView(generic.UpdateView):
    model = TruckDriver
    fields = ['first_name',
              'last_name',
              'phone',
              'email',
              'address',
              'license_number',
              'company',
              'referee']
    template_name = 'agrosealapp/driver_create_form.html'
    success_url = '/drivers/'


class DriverDeleteView(generic.DeleteView):
    model = TruckDriver
    success_url = '/drivers/'
    template_name = 'agrosealapp/driver_delete_form.html'
    context_object_name = 'driver'


class CompanyListView(generic.ListView):
    model = Company
    template_name = 'agrosealapp/company_list.html'
    context_object_name = 'company_list'


class CompanyDetailView(generic.DetailView):
    model = Company
    template_name = 'agrosealapp/company_detail.html'
    context_object_name = 'company'


class CompanyCreateView(generic.CreateView):
    form_class = CompanyCreateForm
    template_name = 'agrosealapp/company_create_form.html'
    success_url = '/companies/'


class CompanyUpdateView(generic.UpdateView):
    model = Company
    fields = ['name', 'contact_person', 'contact_phone', 'contact_email', 'address']
    template_name = 'agrosealapp/company_create_form.html'
    success_url = '/companies/'


class CompanyDeleteView(generic.DeleteView):
    model = Company
    success_url = '/companies/'
    template_name_suffix = '_delete_form'


class TruckListView(LoginRequiredMixin, generic.ListView):
    model = Truck
    template_name = 'agrosealapp/truck_list.html'
    context_object_name = 'truck_list'


class TruckDetailView(LoginRequiredMixin, generic.DetailView):
    model = Truck
    template_name = 'agrosealapp/truck-detail.html'
    context_object_name = 'truck'


class TruckCreateView(generic.CreateView):
    form_class = TruckCreateForm
    template_name = 'agrosealapp/truck_create_form.html'
    success_url = '/trucks/'


class TruckUpdateView(generic.UpdateView):
    model = Truck
    fields = ['driver', 'plate_number', 'vehicle_model', 'vehicle_type']
    template_name = 'agrosealapp/truck_create_form.html'
    success_url = '/trucks/'


class TruckDeleteView(generic.DeleteView):
    model = Truck
    success_url = '/trucks/'
    template_name_suffix = '_delete_form'
    context_object_name = 'truck'


class RequestListView(LoginRequiredMixin, generic.ListView):
    model = TruckRequest
    template_name = 'agrosealapp/request_list.html'
    context_object_name = 'request_list'


class RequestDetailView(LoginRequiredMixin, generic.DetailView):
    model = TruckRequest
    template_name = 'agrosealapp/request-detail.html'
    context_object_name = 'request'


@csrf_exempt
def get_request(request):
    data = '<strong>This may not work</strong>'
    number_of_crates = ''
    pick_up_location = ''
    fruit = ''
    drop_off_location = ''
    acceptance = ''
    price = ''
    phone_number = ''
    customer_name = ''
    session_id = ''
    mobile_money_number = ''
    response = ''
    # db = Sdk('http://agroseal.herokuapp.com', '371944f0580ba01b7a576f26eba3e0b6')
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        print(body)
        session_id = body['SessionId']
        phone_number = body['Mobile']

        if body['Type'] == 'Initiation':
            # print("Welcome to this world")
            response = {'Type': 'Response', 'Message': 'Welcome To AgroSEAL LTD. \n Select a crop for transport: \n 1. Tomato\n 2. Mango\n 3. Orange\n 4. Pineapple\n 5. Salad Vegetable'}
        elif body['Type'] == 'Response':
            if body['Sequence'] == 2:
                if body['Message'] == '1':
                    fruit = 'Tomato'
                    response = {'Type': 'Response', 'Message': 'How many crates are you transporting?\n '}
                elif body['Message'] == '2':
                    fruit = 'Mango'
                    response = {'Type': 'Response', 'Message': 'How many crates are you transporting?\n '}
                elif body['Message'] == '3':
                    fruit = 'Orange'
                    response = {'Type': 'Response', 'Message': 'How many crates are you transporting?\n '}
                elif body['Message'] == '4':
                    fruit = 'Pineapple'
                    response = {'Type': 'Response', 'Message': 'How many crates are you transporting?\n '}
                elif body['Message'] == '5':
                    fruit = 'Salad Vegetable'
                    response = {'Type': 'Response', 'Message': 'How many crates are you transporting?\n '}
                else:
                    response = {'Type': 'Release', 'Message': 'Wrong Choice, Bye.'}
            elif body['Sequence'] == 3:
                number_of_crates = body['Message']
                response = {'Type': 'Response', 'Message': 'Where is the pickup location?\n '}
            elif body['Sequence'] == 4:
                pick_up_location = body['Message']
                response = {'Type': 'Response', 'Message': 'Where is the drop-off location?\n'}
            elif body['Sequence'] == 5:
                drop_off_location = body['Message']
                price = 460 * 100
                response = {'Type': 'Response', 'Message': 'The cost of transporting from {0} to {1} is {2} cedes.\n 1. Accept \n 2. Decline'.format(pick_up_location, drop_off_location, str(price))}
            if body['Sequence'] == 6:
                if body['Message'] == '1':
                    acceptance = 'True'
                    response = {'Type': 'Response', 'Message': 'Please enter your Mobile Money Number'}
                elif body['Message'] == '2':
                    acceptance = 'False'
                    response = {'Type': 'Release', 'Message': 'Thank you for reaching out to us. Please call again.'}
            if body['Sequence'] == 7:
                number = body['Message']
                response = {'Type': 'Response', 'Message': 'Please enter your full name.'}
            if body['Sequence'] == 8:
                customer_name = body['Message']
                response = {'Type': 'Release', 'Message': 'Thank you for your patronage, we will get in touch with you soon.'}
                full_request = TruckRequest.objects.create(
                    request_phone=phone_number,
                    customer_name=customer_name,
                    pickup_city=pick_up_location,
                    dropoff_city=drop_off_location,
                    fruit=fruit,
                    fruit_quatity=number_of_crates,
                    mobile_money=mobile_money_number,
                    price=price)
    return HttpResponse(json.dumps(response))


def show_dashboard(request):
    num_of_trucks = Truck.objects.all().count()
    num_of_drivers = TruckDriver.objects.all().count()
    num_of_requests = TruckRequest.objects.all().count()

    return render(request, 'agrosealapp/index.html', context={
        'num_of_trucks': num_of_trucks,
        'num_of_drivers': num_of_drivers,
        'num_of_requests': num_of_requests
    })


def show_requests(request):
    return render(request, 'agrosealapp/index.html')


def show_notifications(request):
    return render(request, 'agrosealapp/blog.html')


def show_map(request):
    return render(request, 'agrosealapp/signup.html')


def show_tmap(request):
    return render(request, 'agrosealapp/tmap.html')



