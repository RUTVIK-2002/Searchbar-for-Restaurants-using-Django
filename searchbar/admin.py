from django.contrib import admin
from .models import Restaurant, Item, Full_details, User_Rating, Location

admin.site.register(Restaurant)
admin.site.register(Full_details)
admin.site.register(Item)
admin.site.register(User_Rating)
admin.site.register(Location)
