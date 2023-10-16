from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Vuelo
# Create your views here.

# creamos una vista en django

def index(request):

  context = {
    "vuelos": Vuelo.objects.all()
  }

  return render(request, "flights/index.html", context)


def flight(request, flight_id):
  try:
    vuelo = Vuelo.objects.get(pk=flight_id)
  except Vuelo.DoesNotExist:
    raise Http404("Vuelo no existe")
  
  context = {
    "vuelo": vuelo
  }
  return render(request, "flights/flight.html", context)



