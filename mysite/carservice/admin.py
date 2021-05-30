from django.contrib import admin

# Register your models here.
from .models import Address, RentalBase, Car, Order, Client, Seller, OrdersArchive, Repairments

admin.site.register(Address)
admin.site.register(RentalBase)
admin.site.register(Car)
admin.site.register(Order)
admin.site.register(Client)
admin.site.register(Seller)
admin.site.register(OrdersArchive)
admin.site.register(Repairments)
