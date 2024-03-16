from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Vehical
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator

def vehical(request):
    vehicals=Vehical.objects.order_by('-created_date')
    paginator=Paginator(vehicals,2)
    page=request.GET.get('page')
    paged_vehicals=paginator.get_page(page)
    models_search=Vehical.objects.values_list('model',flat=True).distinct()
    city_search=Vehical.objects.values_list('city',flat=True).distinct()
    year_search=Vehical.objects.values_list('year',flat=True).distinct()
    body_style_search=Vehical.objects.values_list('body_style',flat=True).distinct()

    data={
          'vehicals':paged_vehicals,
          'models_search':models_search,
          'city_search':city_search,
          'year_search':year_search,
          'body_style_search':body_style_search,

    }
    return render(request,'vehical/vehical.html',data)

def vehical_detail(request,id):
    single_vehical=get_object_or_404(Vehical,pk=id)
    data={
           'single_vehical':single_vehical,
    }
    return render(request,'vehical/vehical_detail.html',data)

def search(request):
    vehicals = Vehical.objects.order_by('-created_date')

    if 'keyword' in request.GET:
        keyword = request.GET['keyword'].strip()  # Trim whitespace
        if keyword:
            vehicals = vehicals.filter(description__icontains=keyword)

    if 'model' in request.GET:
        model = request.GET['model'].strip()  # Trim whitespace
        if model:
            vehicals = vehicals.filter(model__icontains=model)

    if 'city' in request.GET:
        city = request.GET['city'].strip()  # Trim whitespace
        if city:
            vehicals = vehicals.filter(city__iexact=city)

    if 'year' in request.GET:
        year = request.GET['year'].strip()  # Trim whitespace
        if year:
            vehicals = vehicals.filter(year__iexact=year)

    if 'body_style' in request.GET:
        body_style = request.GET['body_style'].strip()  # Trim whitespace
        if body_style:
            vehicals = vehicals.filter(body_style__icontains=body_style)

    if 'min_price' in request.GET and 'max_price' in request.GET:
        min_price = request.GET['min_price'].strip()  # Trim whitespace
        max_price = request.GET['max_price'].strip()  # Trim whitespace
        if max_price:
            vehicals = vehicals.filter(price__gte=min_price, price__lte=max_price)

    data = {
        'vehicals': vehicals
    }

    return render(request, 'vehical/search.html', data)
