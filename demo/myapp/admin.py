from django.contrib import admin
from .models import WarehouseDelivery, Container, SeaportsStatuses, Seaports, ExportItem

admin.site.register(WarehouseDelivery)
admin.site.register(Container)
admin.site.register(SeaportsStatuses)
admin.site.register(Seaports)
admin.site.register(ExportItem)

# Register your models here.
