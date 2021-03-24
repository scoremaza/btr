from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import state_choices, bedroom_choices, price_choices
from listings.models import Listing
from realtors.models import Realtor

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        
    }
    return render(request, 'pages/index.html', context)

def about(request):
    # Get all Realtors
    realtor = Realtor.objects.order_by('-hire_date')
    
    #Get MVP
    realtor_of_month = Realtor.objects.all().filter(is_mvp=True)
    
    context = {
        'realtors': realtor,
        'realtor_of_month': realtor_of_month
    }


    return render(request, 'pages/about.html', context)
