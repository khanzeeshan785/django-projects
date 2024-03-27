# """
# URL configuration for test_prjct project.

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/4.2/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
from django.contrib import admin
# # from django.urls import path


# # urls.py
# from django.urls import path, include
# from rest_framework import routers
# from book.views import BookViewSet

# router = routers.DefaultRouter()
# router.register(r'books', BookViewSet)

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include(router.urls)),
# ]



# # books/urls.py

# from django.urls import path
# from book.views import book_list

# urlpatterns = [
#     path('books/', book_list, name='book-list'),
# ]



# urls.py

# from django.urls import path
# from book.views import task_list
# from rest_framework.authtoken import views


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('tasks/', task_list, name='task_list'),
#     path('api-token-auth/', views.obtain_auth_token)
#     # Add other URL patterns as needed
# ]
# # urls.py
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# # from book.views import ProductViewSet

# router = DefaultRouter()
# router.register(r'products', ProductViewSet, basename='product')

# urlpatterns = [
#     path('', include(router.urls)),
# ]

from django.contrib import admin
from django.urls import path , include
from book import views
from rest_framework.routers import DefaultRouter

routers = DefaultRouter()
routers.register('flight', views.FlightViewSet)
routers.register('passengers', views.PassengerViewSet)
routers.register('reservations', views.ReservationViewSet)

urlpatterns = [
    path('admin/' ,admin.site.urls),  
    path('flightServices/' , include(routers.urls)),
    path('flightServices/findFlights/' , views.find_flights),
    path('flightServices/saveReservation/' , views.save_reservation)
]



###matlab yah par  last line ne route ban jayege jaise -->
# flightServices/flight
# flightServices/passengers
# flightServices/reservations
