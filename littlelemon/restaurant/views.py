from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Menu,Booking
from .serializers import MenuSerializer, BookingSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all().order_by('id')
    serializer_class = MenuSerializer
    
    filterset_fields = ['Price', 'Inventory']
    ordering_fields = ['Price', 'Inventory', 'Title']
    search_fields = ['Title']

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all().order_by('id')
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all().order_by('id')
    serializer_class = BookingSerializer