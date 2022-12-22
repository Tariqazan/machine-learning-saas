from django.urls import path
from .views import *

urlpatterns = [
     path('search/', Search.as_view(),name="search"),
     path('search/result/', search_result, name="search_result"),
     path('', SupplyChainManagement.as_view(),
         name="supply_chain_management"),
    path('live/track/', LiveTracking.as_view(), name="live_track"),
    path('history/track/', HistoryTracking.as_view(), name="history_track"),

    path('add/driver/', DriverAdd.as_view(), name="add_driver"),
    path('driver/list/', DriverList.as_view(),name="driver_list"),
    path('driver/details/<int:pk>/',
         DriverDetailView.as_view(), name="driver_detail"),

    path('driver/booking/information/add/',
         DriverBooking.as_view(), name="driver_add_booking"),
         path('booking/list/', BookingList.as_view(), name="booking_list"),
     path('edit/booking/<int:pk>/',EditBooking.as_view(), name="edit_booking"),
    path('booking/delete/<pk>/',
         BookingDeleteView.as_view(), name="booking_delete"),
    path('driver/delete/<pk>/',
         DriverDeleteView.as_view(), name="driver_delete"),
    path('driver/booking/detail/pdf/<int:pk>/', GenerateDriverBookingDetailPDF.as_view(),
         name="driver_booking_detail"),

     path('add/vehicle/',AddVehicle.as_view(), name="add_vehicle"),
     path('vehicle/list/',VehicleList.as_view(), name="vehicle_list"),
     path('edit/vehicle/<int:pk>/',EditVehicle.as_view(), name="edit_vehicle"),
    path('vehicle/delete/<pk>/',
         vehicleDeleteView.as_view(), name="vehicle_delete"),
         
     path('add/maintenance/',AddMaintenance.as_view(), name="add_maintenance"),
     path('maintenance/cost/list/', MaintenanceCostList.as_view(), name="maintenance_cost_list"),
     path('edit/maintenance/<int:pk>/',EditMaintenance.as_view(), name="edit_maintenance"),
    path('maintenance/delete/<pk>/',
         MaintenanceDeleteView.as_view(), name="maintenance_delete"),

     path('overtime/',overtime, name="overtime"),
     path('status/',status, name="status"),

     path('add/reminder/', AddReminder.as_view(), name="add_reminder"),
     path('reminder/list', ReminderList.as_view(), name="reminder_list"),
     path('edit/reminder/<int:pk>/',EditReminder.as_view(), name="edit_reminder"),
    path('reminder/delete/<pk>/',
         ReminderDeleteView.as_view(), name="reminder_delete"),

     path('add/customer/', AddCustomer.as_view(), name='add_customer'),
     path('customer/list/', CustomerList.as_view(), name='customer_list'),
     path('edit/customer/<int:pk>/', EditCustomer.as_view(), name='edit_customer'),
     path('delete/customer/<int:pk>/', DeleteCustomer.as_view(), name='delete_customer'),

     
     path('add/fuel/', AddFuel.as_view(), name='add_fuel'),
     path('fuel/list/', FuelList.as_view(), name='fuel_list'),

     path('booking/report/', BookingReport.as_view(),name='booking_report'),
     path('maintenance/report/', MaintenanceReport.as_view(),name='maintenance_report'),
     path('fuel/report/', FuelReport.as_view(),name='fuel_report'),

     path('add/geofence/',AddGeofence.as_view(), name='add_geofence'),
     path('geofence/management/',GeofenceManagement.as_view(), name='geofence_management'),
     path('geofence/events/',GeofenceEvents.as_view(), name='geofence_events'),
]
