# from django.contrib import admin
# from book.models import Flight,Passenger,Reservation
# # Register your models here.
# admin.site.register(Flight)
# admin.site.register(Passenger)
# admin.site.register(Reservation)

from django.contrib import admin
from .models import Flight, Passenger, Reservation

class ReservationAdmin(admin.ModelAdmin):
    list_display = ['id', 'flight', 'passenger']
    list_select_related = ['flight', 'passenger']
    readonly_fields = ['flight', 'passenger']

admin.site.register(Flight)
admin.site.register(Passenger)
admin.site.register(Reservation, ReservationAdmin)