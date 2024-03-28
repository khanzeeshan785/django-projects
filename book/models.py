# models.py
from django.db import models

# class Product(models.Model):
#     name = models.CharField(max_length=255)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     is_bestseller = models.BooleanField(default=False)

#     def __str__(self):
#         return self.name

class Flight(models.Model):
    flightNumber = models.CharField(max_length =10)
    operatingAirlines = models.CharField(max_length =10)
    departureCity = models.CharField(max_length =20)
    arrivalCity = models.CharField(max_length =20)
    dateOfDeparture = models.DateField()
    estimatedTimeOfDeparture = models.TimeField()
        
    def __str__(self):
        return f'Flight{self.flightNumber}'

class Passenger(models.Model):
    firstName = models.CharField(max_length =20)
    lastName = models.CharField(max_length =20)
    middleName = models.CharField(max_length =20)
    email = models.CharField(max_length =20)
    phone = models.CharField(max_length =10)
        
    def __str__(self):
        return f'Passenger{self.firstName}'


class Reservation(models.Model):
    flight = models.ForeignKey(Flight, on_delete= models.CASCADE)
    passenger = models.OneToOneField(Passenger, on_delete= models.CASCADE)
    
    def __str__(self):
        return f'{self.flight}-{self.passenger}'

'''
Passenger can have only one Reservation, as indicated by the OneToOneField relationship.
Conversely, one Flight can have multiple Reservation instances, as indicated by the ForeignKey relationship

'''