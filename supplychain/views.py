from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.http.response import JsonResponse

from django.db.models import Sum

from django.views.generic.base import TemplateView, View
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView

from django.urls import reverse_lazy

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .models import *
from .forms import *

import json

from .utils import render_to_pdf

from django.core.mail import send_mail

import datetime

date = datetime.datetime.now()

# Create your views here.

class Search(View):
    def get(self,request):
        booking_list = []
        booking = Booking.objects.all()
        booking_list+=[i.trip_start for i in booking]
        return JsonResponse(booking_list,safe=False)

@csrf_exempt
def search_result(request):
    value = request.GET.get('q')
    data = Booking.objects.filter(trip_start=value)
    context = {
        'data':data
    }
    return render(request,'search/supply_chain_management_search.html',context)


class SupplyChainManagement(TemplateView):
    template_name = 'supply_chain_management/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(SupplyChainManagement, self).get_context_data(**kwargs)
        context['booking'] = Booking.objects.all()
        context['vehicle_status'] = Vehicle.objects.all()
        context['drivers'] = Driver.objects.all().count()
        context['active_vehicles'] = Vehicle.objects.filter(status=True).count()
        context['active_vehicles_percentage'] = Vehicle.objects.filter(status=True).count()/100
        distance = Booking.objects.all().aggregate(Sum('distance'))['distance__sum']
        fuel = Booking.objects.all().aggregate(Sum('fuel'))['fuel__sum']
        if distance is None or fuel is None:
            pass
        else:
            context['mileage'] = "{:.2f}".format(distance/fuel*100)

        context['jan_cost'] = json.dumps(Booking.objects.filter(trip_start__month=1).aggregate(Sum('cost')))
        context['feb_cost'] = json.dumps(Booking.objects.filter(trip_start__month=2).aggregate(Sum('cost')))
        context['mar_cost'] = json.dumps(Booking.objects.filter(trip_start__month=3).aggregate(Sum('cost')))
        context['apr_cost'] = json.dumps(Booking.objects.filter(trip_start__month=4).aggregate(Sum('cost')))
        context['may_cost'] = json.dumps(Booking.objects.filter(trip_start__month=5).aggregate(Sum('cost')))
        context['june_cost'] = json.dumps(Booking.objects.filter(trip_start__month=6).aggregate(Sum('cost')))
        context['july_cost'] = json.dumps(Booking.objects.filter(trip_start__month=7).aggregate(Sum('cost')))
        context['aug_cost'] = json.dumps(Booking.objects.filter(trip_start__month=8).aggregate(Sum('cost')))
        context['sep_cost'] = json.dumps(Booking.objects.filter(trip_start__month=9).aggregate(Sum('cost')))
        context['oct_cost'] = json.dumps(Booking.objects.filter(trip_start__month=10).aggregate(Sum('cost')))
        context['nov_cost'] = json.dumps(Booking.objects.filter(trip_start__month=11).aggregate(Sum('cost')))
        context['dec_cost'] = json.dumps(Booking.objects.filter(trip_start__month=12).aggregate(Sum('cost')))

        context['jan_fuel'] = json.dumps(Booking.objects.filter(trip_start__month=1).aggregate(Sum('fuel')))
        context['feb_fuel'] = json.dumps(Booking.objects.filter(trip_start__month=2).aggregate(Sum('fuel')))
        context['mar_fuel'] = json.dumps(Booking.objects.filter(trip_start__month=3).aggregate(Sum('fuel')))
        context['apr_fuel'] = json.dumps(Booking.objects.filter(trip_start__month=4).aggregate(Sum('fuel')))
        context['may_fuel'] = json.dumps(Booking.objects.filter(trip_start__month=5).aggregate(Sum('fuel')))
        context['june_fuel'] = json.dumps(Booking.objects.filter(trip_start__month=6).aggregate(Sum('fuel')))
        context['july_fuel'] = json.dumps(Booking.objects.filter(trip_start__month=7).aggregate(Sum('fuel')))
        context['aug_fuel'] = json.dumps(Booking.objects.filter(trip_start__month=8).aggregate(Sum('fuel')))
        context['sep_fuel'] = json.dumps(Booking.objects.filter(trip_start__month=9).aggregate(Sum('fuel')))
        context['oct_fuel'] = json.dumps(Booking.objects.filter(trip_start__month=10).aggregate(Sum('fuel')))
        context['nov_fuel'] = json.dumps(Booking.objects.filter(trip_start__month=11).aggregate(Sum('fuel')))
        context['dec_fuel'] = json.dumps(Booking.objects.filter(trip_start__month=12).aggregate(Sum('fuel')))
        return context


class LiveTracking(TemplateView):
    template_name = 'supply_chain_management/live_track.html'


class HistoryTracking(TemplateView):
    template_name = 'supply_chain_management/history_track.html'

    def get_context_data(self, **kwargs):
        context = super(HistoryTracking,self).get_context_data(**kwargs)
        context['vehicles'] = Vehicle.objects.all()
        return context


class AddGeofence(TemplateView):
    template_name = 'supply_chain_management/add_geofence.html'


class GeofenceManagement(TemplateView):
    template_name = 'supply_chain_management/geofence_management.html'


class GeofenceEvents(TemplateView):
    template_name = 'supply_chain_management/geofence_events.html'


class DriverAdd(CreateView):
    model = Driver
    fields = ['name', 'number', 'driver_pic', 'driving_licence', 'nid','salary']
    template_name = 'supply_chain_management/add_driver.html'
    success_url = reverse_lazy('supply_chain_management')


class DriverList(ListView):
    model = Driver
    template_name = 'supply_chain_management/driver_list.html'


# def add_driver(request):
#     if request.method=="POST":
#         number = request.POST.get('number')
#         name = request.POST.get('name')
#         my_file = request.FILES.get('file')
#         Driver.objects.create(name=name,number=number,driver_pic=my_file)
#         return HttpResponse('')

#     return  JsonResponse({'post':'false'})


class DriverBooking(CreateView):
    model = Booking
    fields = ['customer','driver','vehicle', 'destination', 'fuel', 'distance', 'time', 'cost','email']
    template_name = 'supply_chain_management/add_booking_information.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        Driver.objects.filter(id=self.object.driver.id).update(status=True)
        Vehicle.objects.filter(id=self.object.vehicle.id).update(status=True)
        if self.object.email == True:
            send_mail(subject="Trip Start", message="The trip is starting", from_email=self.object.customer.email,recipient_list=['animo.ai.co@gmail.com'],fail_silently=False)
        else:
            pass
        form.save()
        return redirect('booking_list')

    def get_context_data(self, **kwargs):
        context = super(DriverBooking, self).get_context_data(**kwargs)
        context['drivers'] = Driver.objects.all()
        context['vehicles'] = Vehicle.objects.all()
        context['customer'] = Customer.objects.all()
        return context


class BookingList(ListView):
    model = Booking
    template_name = 'supply_chain_management/booking_list.html'


class EditBooking(UpdateView):
    model = Booking
    fields = ['customer','driver','vehicle', 'destination', 'fuel', 'distance', 'time', 'cost']
    template_name = 'supply_chain_management/edit_booking.html'
    success_url = reverse_lazy('supply_chain_management')


class BookingDeleteView(DeleteView):
    model = Booking
    template_name = 'supply_chain_management/delete_booking.html'
    success_url = reverse_lazy('supply_chain_management')


class DriverDetailView(DetailView):
    model = Driver
    template_name = 'supply_chain_management/driver_details.html'

    def get_context_data(self, **kwargs):
        context = super(DriverDetailView, self).get_context_data(**kwargs)
        id = self.kwargs.get('pk')
        driver = Driver.objects.get(id=id)
        context['booking_list'] = Booking.objects.filter(driver=driver)
        context['total'] = Booking.objects.filter(
            driver=driver).aggregate(Sum('fuel'))
        context['total_distance'] = Booking.objects.filter(
            driver=driver).aggregate(Sum('distance'))
        context['total_cost'] = Booking.objects.filter(
            driver=driver).aggregate(Sum('cost'))
        overtime = Booking.objects.filter(driver_id=id,trip_end__month=date.month).aggregate(Sum('overtime'))
        try:
            context['salary'] = self.object.salary+overtime['overtime__sum']
        except:
            context['salary'] = self.object.salary
        context['Month'] = date.strftime("%B %Y")
        return context


class DriverDeleteView(DeleteView):
    model = Driver
    template_name = 'supply_chain_management/delete_driver.html'
    success_url = reverse_lazy('supply_chain_management')


class AddVehicle(CreateView):
    model = Vehicle
    fields = ['department','vehicle_no','vehicle_model','register_number','chasis_no']
    template_name = 'supply_chain_management/add_vehicle.html'
    success_url = reverse_lazy('supply_chain_management')


class VehicleList(ListView):
    model = Vehicle
    template_name = "supply_chain_management/vehicle_list.html"


class EditVehicle(UpdateView):
    model = Vehicle
    fields = ['department','vehicle_no','vehicle_model','register_number','chasis_no']
    template_name = 'supply_chain_management/edit_vehicle.html'
    success_url = reverse_lazy('supply_chain_management')


class vehicleDeleteView(DeleteView):
    model = Vehicle
    template_name = 'supply_chain_management/delete_vehicle.html'
    success_url = reverse_lazy('supply_chain_management')


class AddMaintenance(CreateView):
    model = Maintenance
    fields = '__all__'
    template_name = 'supply_chain_management/add_maintenance.html'
    success_url = reverse_lazy('supply_chain_management')


class MaintenanceCostList(ListView):
    model = Maintenance
    template_name = 'supply_chain_management/maintenance_cost_list.html'


class EditMaintenance(UpdateView):
    model = Maintenance
    fields = '__all__'
    template_name = 'supply_chain_management/edit_maintenance.html'
    success_url = reverse_lazy('supply_chain_management')


class MaintenanceDeleteView(DeleteView):
    model = Vehicle
    template_name = 'supply_chain_management/delete_maintenance.html'
    success_url = reverse_lazy('supply_chain_management')

@csrf_exempt
def overtime(request):
    if request.POST:
        id = request.POST.get('id')
        value = request.POST.get('value')
        Booking.objects.filter(id=id).update(overtime=value)
    return JsonResponse({'data':'booking'})


@csrf_exempt
def status(request):
    if request.POST:
        id = request.POST.get('id')
        value = request.POST.get('value')
        obj = Booking.objects.get(id=id)
        Booking.objects.filter(id=id).update(trip_end=date,status=True)
        if value == "Returned":
            Vehicle.objects.filter(id=obj.vehicle.id).update(status=False)
        else:
            Vehicle.objects.filter(id=obj.vehicle.id).update(status=True)
        return JsonResponse({'status':'ok'})


class AddReminder(CreateView):
    model = Reminder
    fields = '__all__'
    template_name = 'supply_chain_management/add_reminder.html'
    success_url = reverse_lazy('reminder_list')


class ReminderList(ListView):
    model = Reminder
    template_name = 'supply_chain_management/reminder_list.html'


class EditReminder(UpdateView):
    model = Reminder
    form_class = ReminderForm
    template_name = 'supply_chain_management/edit_reminder.html'
    success_url = reverse_lazy('reminder_list')


class ReminderDeleteView(DeleteView):
    model = Reminder
    template_name = 'supply_chain_management/delete_reminder.html'
    success_url = reverse_lazy('reminder_list')


class AddCustomer(CreateView):
    model = Customer
    fields = '__all__'
    template_name = 'supply_chain_management/add_customer.html'
    success_url = reverse_lazy('customer_list')


class CustomerList(ListView):
    model = Customer
    template_name = 'supply_chain_management/customer_list.html'


class EditCustomer(UpdateView):
    model = Customer
    fields = '__all__'
    template_name = 'supply_chain_management/edit_customer.html'
    success_url = reverse_lazy('customer_list')


class DeleteCustomer(DeleteView):
    model = Customer
    template_name = 'supply_chain_management/delete_customer.html'
    success_url = reverse_lazy('customer_list')


class AddFuel(CreateView):
    model = Fuel
    fields = '__all__'
    template_name = 'supply_chain_management/add_fuel.html'
    success_url = reverse_lazy('fuel_list')


class FuelList(ListView):
    model = Fuel
    template_name = 'supply_chain_management/fuel_list.html'


class GenerateDriverBookingDetailPDF(View):
    def get(self, request, *args, **kwargs):
        obj = Driver.objects.get(id=self.kwargs['pk']) 
        data = Booking.objects.filter(driver=obj.id)
        total = Booking.objects.filter(
            driver=obj.id).aggregate(Sum('fuel'))
        total_distance = Booking.objects.filter(
            driver=obj.id).aggregate(Sum('distance'))
        total_cost = Booking.objects.filter(
            driver=obj.id).aggregate(Sum('cost'))
        overtime = Booking.objects.filter(driver_id=self.kwargs['pk'],trip_end__month=date.month).aggregate(Sum('overtime'))
        try:
            salary = obj.salary+overtime['overtime__sum']
        except:
            salary = obj.salary
        context = {
            'driver':obj,
            'data':data,
            'total':total,
            'total_distance':total_distance,
            'total_cost':total_cost,
            'salary':salary
            }
        pdf = render_to_pdf('supply_chain_management/pdf/driver_booking_detail.html',context)
        return HttpResponse(pdf, content_type='application/pdf')


@method_decorator(csrf_exempt,name='dispatch')
class BookingReport(View):

    def get(self,request,**kwargs):
        return render(request,'supply_chain_management/booking_report.html')

    def post(self,request,**kwargs):
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        booking = Booking.objects.filter(trip_start__gte=start_date,trip_start__lte=end_date)
        return render(request,'supply_chain_management/booking_report.html',{'bookings':booking})


@method_decorator(csrf_exempt,name='dispatch')
class MaintenanceReport(View):

    def get(self,request,**kwargs):
        return render(request,'supply_chain_management/maintenance_report.html')

    def post(self,request,**kwargs):
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        maintenance = Maintenance.objects.filter(date__gte=start_date,date__lte=end_date)
        return render(request,'supply_chain_management/maintenance_report.html',{'maintenances':maintenance})


@method_decorator(csrf_exempt,name='dispatch')
class FuelReport(View):

    def get(self,request,**kwargs):
        return render(request,'supply_chain_management/fuel_report.html')

    def post(self,request,**kwargs):
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        fuel = Fuel.objects.filter(fill_date__gte=start_date,fill_date__lte=end_date)
        return render(request,'supply_chain_management/fuel_report.html',{'fuels':fuel})