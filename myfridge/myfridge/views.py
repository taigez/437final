from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from foods.models import Item



# Create your views here.
def welcome(request):

    return render(request, "website/welcome.html", {'num_food':Item.objects.count()})
