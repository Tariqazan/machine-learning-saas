from django.db import models

# Create your models here.

class Driver(models.Model):
    name = models.CharField(blank=False, null=False, max_length=100)
    number = models.CharField(blank=False, null=False, max_length=100)
    driver_pic = models.ImageField(
        blank=False, null=False, upload_to='media/driver/pics/')
    driving_licence = models.ImageField(
        blank=False, null=False, upload_to='media/driver/licences/')
    salary = models.IntegerField()
    status = models.BooleanField(default=False)
    nid = models.ImageField(blank=False, null=False,
                            upload_to='media/driver/nid/')

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    DEPT=(
        ('Operation','Operation'),
        ('CRO','CRO'),
        ('GPS','GPS'),
        ('Ambulance','Ambulance'),
        ('Pool','Pool'),
        ('Delivery','Delivery')
    )
    department = models.CharField(max_length=100,choices=DEPT)
    vehicle_no = models.CharField(max_length=50)
    vehicle_model = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    register_number = models.CharField(max_length=100)
    chasis_no = models.CharField(max_length=100)
    latitude = models.CharField(blank=True, null=True, max_length=100)
    longitude = models.CharField(blank=True, null=True, max_length=100)

    def __str__(self):
        return self.vehicle_no


class Customer(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return self.name


class Booking(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    distance = models.CharField(blank=False, null=False, max_length=100)
    destination = models.CharField(blank=False, null=False, max_length=100)
    time = models.CharField(blank=False, null=False, max_length=100)
    fuel = models.CharField(blank=False, null=False, max_length=100)
    cost = models.CharField(blank=False, null=False, max_length=100)
    overtime = models.IntegerField(blank=True,null=True)
    trip_start = models.DateField(auto_now=True) 
    status = models.BooleanField(default=False)
    trip_end = models.DateField(blank=True,null=True)
    email = models.BooleanField(default=False)

    def __str__(self):
        return self.destination


class Maintenance(models.Model):
    vehicle = models.ForeignKey(Vehicle,on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    item = models.CharField(max_length=300)
    amount = models.IntegerField()
    reference = models.FileField(blank=True,null=True,upload_to='referance/')



class Reminder(models.Model):
    vehicle = models.ForeignKey(Vehicle,on_delete=models.CASCADE)
    date = models.DateField()
    message = models.TextField()


class Fuel(models.Model):
    vehicle = models.ForeignKey(Vehicle,on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver,on_delete=models.CASCADE)
    fill_date = models.DateField()
    quantity = models.IntegerField()
    odometer = models.IntegerField()
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)

    