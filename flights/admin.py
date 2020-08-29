from django.contrib import admin
from .models import Flight, Airport,Passenger

# Register your models here.
class FlightsAdmin(admin.ModelAdmin):
    list_display=("id","origin","destination","duration")

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal=("flights",)

admin.site.register(Flight,FlightsAdmin)
admin.site.register(Airport)
admin.site.register(Passenger, PassengerAdmin)