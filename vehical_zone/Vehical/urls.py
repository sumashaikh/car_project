from django.urls import path
from .import views

urlpatterns = [
    path('',views.vehical,name='vehical'),
    path('<int:id>',views.vehical_detail,name='vehical_detail'),
    path('search/',views.search,name='search'),





]