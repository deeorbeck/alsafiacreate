from django.contrib import admin
from django.contrib.auth.models import User
from .models import (
    Category,
    Brand,
    Product,
    Offer,
    Order,
    Profile,
    News
)


# Register your models here.
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('name', 'complete')
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'card_vendor')
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Offer)
admin.site.register(News)
admin.site.register(Order, OrdersAdmin)
admin.site.register(Profile, ProfileAdmin)
