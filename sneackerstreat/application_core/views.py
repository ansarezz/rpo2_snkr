from django.shortcuts import render
from .models import Item

def model_page(request):
    items = Item.objects.all()
    context = {
        'items' : items
    }
    return render(request, "./snkr_page.html", context)
