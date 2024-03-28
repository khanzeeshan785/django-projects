# views.py
# from rest_framework import viewsets, status
# from rest_framework.decorators import action
# from rest_framework.response import Response
# from .models import Product
# from .serializers import ProductSerializer

# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

#     @action(detail=True, methods=['post'])
#     def mark_as_bestseller(self, request, pk=None):
#         """
#         Custom action to mark a product as a bestseller.
#         """
#         product = self.get_object()
#         product.is_bestseller = True
#         product.save()
#         serializer = self.get_serializer(product)
#         return Response(serializer.data, status=status.HTTP_200_OK)

from django.shortcuts import render
from book.models import Flight , Passenger , Reservation
from book.serializers import FlightSerializer, PassengerSerializer, ReservationSerializer

from rest_framework import viewsets

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# @api_view(['POST'])
# def find_flights(request):
# 	flights = Flight.objects.filter(departureCity = request.data['departureCity'], arrivalCity = request.data['arrivalCity'], dateOfDeparture = request.data['dateOfDeparture'])
# 	serializer = FlightSerializer(flights,many = True)
# 	return Response(serializer.data)

#To allow searching with any combination of the three attributes (departureCity, arrivalCity, dateOfDeparture), you can dynamically construct the query based on the provided attributes. Here's how you can modify your view to achieve this:
from django.db.models import Q
@api_view(['POST'])
def find_flights(request):
    departure_city = request.data.get('departureCity')
    arrival_city = request.data.get('arrivalCity')
    date_of_departure = request.data.get('dateOfDeparture')

    # Start with an empty query
    query = Q()

    # Dynamically add conditions if attributes are provided
    if departure_city:
        query &= Q(departureCity=departure_city)
    if arrival_city:
        query &= Q(arrivalCity=arrival_city)
    if date_of_departure:
        query &= Q(dateOfDeparture=date_of_departure)

    # Filter flights based on the constructed query
    flights = Flight.objects.filter(query)

    serializer = FlightSerializer(flights, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def save_reservation(request):
    flight_id = request.data.get('flightId')
    email = request.data.get('email')
    phone = request.data.get('phone')

    # Check if passenger with the same email or phone already exists
    existing_passenger = Passenger.objects.filter(email=email).first() or Passenger.objects.filter(phone=phone).first()  #first() retrieves the first passenger from the QuerySet of passengers with the given email. If no passenger with the given email exists, it returns None.
    if existing_passenger:
        return Response({'error': 'Passenger with the same email or phone already exists'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        flight = Flight.objects.get(id=flight_id)
    except Flight.DoesNotExist:
        return Response({'error': 'Flight not found'}, status=status.HTTP_404_NOT_FOUND)

    passenger = Passenger(
        firstName=request.data.get('firstName', ''),
        lastName=request.data.get('lastName', ''),
        middleName=request.data.get('middleName', ''),
        email=email,
        phone=phone
    )
    passenger.save()

    reservation = Reservation(flight=flight, passenger=passenger)
    reservation.save()

    return Response({'message': 'Reservation saved successfully'}, status=status.HTTP_201_CREATED)

class FlightViewSet(viewsets.ModelViewSet):
	queryset = Flight.objects.all()
	serializer_class  = FlightSerializer
	
	
class PassengerViewSet(viewsets.ModelViewSet):
	queryset = Passenger.objects.all()
	serializer_class  = PassengerSerializer


class ReservationViewSet(viewsets.ModelViewSet):
	queryset = Reservation.objects.all()
	serializer_class  = ReservationSerializer



'''

how to impose uniqneds in the save_reservarion passenger.email,passenger.phone
like if any object having this fileds already exist then it should not go ahead
'''

'''

    passenger = Passenger(
        firstName=request.data.get('firstName', ''),
        lastname=request.data.get('lastName', ''),
        middleName=request.data.get('middleName', ''),
        email=email,
        phone=phone
    )
    
    
    OR
    
        passenger = Passenger(
        firstName=request.data.get('firstName'),
        lastname=request.data.get('lastName'),
        middleName=request.data.get('middleName'),
        email=email,
        phone=phone
    )
The difference between request.data.get('firstName', '') and request.data.get('firstName'") lies in the default value provided when the key 'firstName' is not found in the request.data dictionary.


'''