from django.shortcuts import render
from .models import Team
from Vehical.models import Vehical

def home(request):
    teams=Team.objects.all()
    featured_vehical=Vehical.objects.order_by('-created_date').filter(is_featured=True)
    all_vehical=Vehical.objects.order_by('-created_date')
    #search_fields=Vehical.objects.values('model','city','year','body_style')
    models_search=Vehical.objects.values_list('model',flat=True).distinct()
    city_search=Vehical.objects.values_list('city',flat=True).distinct()
    year_search=Vehical.objects.values_list('year',flat=True).distinct()
    body_style_search=Vehical.objects.values_list('body_style',flat=True).distinct()




    data={
          'teams':teams,
          'featured_vehical':featured_vehical,
          'all_vehical':all_vehical,
          #'search_fields':search_fields,
          'models_search':models_search,
          'city_search':city_search,
          'year_search':year_search,
          'body_style_search':body_style_search,
    }
    return render(request,'pages/home.html',data) 


def about(request):
    teams=Team.objects.all()

    data={
          'teams':teams
    }

    return render(request,'pages/about.html',data) 


def services(request):
    return render(request,'pages/services.html') 

def contact(request):
    return render(request,'pages/contact.html') 