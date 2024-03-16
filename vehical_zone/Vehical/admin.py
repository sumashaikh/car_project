from django.contrib import admin
from .models import Vehical
from django.utils.html import format_html


class VehicalAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="40" style="border-radius:50px;" />'.format(object.car_photo.url))

    thumbnail.short_description='car_image'

    list_display=('id','thumbnail','city','vehical_title','color','model','year','body_style','fuel_type','is_featured',)
    list_display_links=('vehical_title',)
    list_editable=('is_featured',)
    search_fields=('id','city','vehical_title','body_style','model',)
    list_filter=('city','body_style','model','fuel_type',)


admin.site.register(Vehical,VehicalAdmin)

