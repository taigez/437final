from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse , HttpResponse
from .models import Item
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone


def scan(request):



    return redirect('/foods/')

def in_range(x, y, newx, newy, threshold):
    if (int(newx) - x)**2 + (int(newy) - y)**2 > threshold**2:
        return False
    return True


def scan_fridge(item, x, y):
    foods = Item.objects.all()
    for food in foods:
        if food.name == item and not in_range(food.xpos, food.ypos, x, y, threshold=10):
            new_item = Item(name=item, xpos=x, ypos=y)
            new_item.in_date = timezone.now()
            new_item.save()

def myfood(request):

    return render(request, "myfood.html", {"foods":Item.objects.all(), 'num_food':Item.objects.count()})

def delete_item(request, id):
    item = get_object_or_404(Item, pk=id)
    item.delete()
    
    return redirect('/foods/myfood')


@csrf_exempt
def handle_get(request):
    item = request.GET.get('item', None)
    x = request.GET.get('posx', None)
    y = request.GET.get('posy', None)
    scan_fridge(item, x, y)

    #http://127.0.0.1:8000/foods/receive_json/?item=apple

    return HttpResponse('OK!')




