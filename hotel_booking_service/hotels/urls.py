from django.urls import path
from . import views

urlpatterns = [
    path('rooms/create/', views.create_room),
    path('rooms/delete/', views.delete_room),
    path('rooms/', views.list_rooms),

    path('bookings/create/', views.create_booking),
    path('bookings/delete/', views.delete_booking),
    path('bookings/', views.list_bookings),
]
