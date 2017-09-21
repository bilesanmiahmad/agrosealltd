from django.db import models

# Create your models here.


class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=11)
    email = models.EmailField(blank=True)
    address = models.TextField()

    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)

    class Meta:
        verbose_name_plural = "People"


class Company(models.Model):
    name = models.CharField(max_length=30)
    address = models.TextField()
    contact_email = models.EmailField(blank=True)
    contact_phone = models.CharField(max_length=11)
    contact_person = models.ForeignKey('Person', blank=True, null=True)

    def __str__(self):
        return '{0}'.format(self.name)

    class Meta:
        verbose_name_plural = "Companies"


class TruckDriver(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    address = models.TextField()
    license_number = models.CharField(max_length=20)
    company = models.ForeignKey('Company', blank=True, null=True)
    referee = models.ForeignKey('Person', blank=True, null=True)

    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)

    class Meta:
        verbose_name_plural = "Drivers"


class Truck(models.Model):
    driver = models.ForeignKey('TruckDriver')
    plate_number = models.CharField(max_length=8)
    vehicle_model = models.CharField(max_length=20)
    vehicle_type = models.CharField(max_length=20)

    def __str__(self):
        return '{0}'.format(self.plate_number)

    class Meta:
        verbose_name_plural = "Trucks"


class TrackDevice(models.Model):
    ref_number = models.UUIDField()
    driver = models.ForeignKey('TruckDriver')

    def __str__(self):
        return '{0}'.format(self.imei_number)

    class Meta:
        verbose_name_plural = "Devices"


class TrackEvent(models.Model):
    device = models.ForeignKey('TrackDevice')
    current_longitude = models.DecimalField(max_digits=7, decimal_places=4)
    current_latitude = models.DecimalField(max_digits=7, decimal_places=4)
    current_address = models.TextField()
    created_on = models.DateTimeField()

    class Meta:
        verbose_name_plural = "Events"


class TruckRequest(models.Model):
    request_phone = models.CharField(max_length=11, blank=True, null=True)
    customer_name = models.CharField(max_length=50, blank=True, null=True)
    pickup_city = models.CharField(max_length=20, blank=True, null=True)
    dropoff_city = models.CharField(max_length=20, blank=True, null=True)
    fruit = models.CharField(max_length=10, blank=True, null=True)
    fruit_quantity = models.IntegerField(blank=True, null=True)
    mobile_money = models.CharField(max_length=11, blank=True, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    service_date = models.DateField(blank=True, null=True)
    service_time = models.TimeField(blank=True, null=True)
    requested_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Requests"


class Trip(models.Model):
    request = models.ForeignKey('TruckRequest')
    trip_cost = models.DecimalField(max_digits=7, decimal_places=2)
    income = models.DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        verbose_name_plural = "Trips"
