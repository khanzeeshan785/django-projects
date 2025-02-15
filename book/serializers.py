# serializers.py
# from rest_framework import serializers
# from .models import Product

# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = '__all__'


from rest_framework import serializers
from book.models import Flight ,  Passenger , Reservation



class FlightSerializer(serializers.ModelSerializer):
	class Meta:
		model = Flight
		fields = '__all__'



class PassengerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Passenger
		fields = '__all__'
		

class ReservationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Reservation
		fields = '__all__'


