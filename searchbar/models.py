from django.db import models


class Location(models.Model):
    city = models.CharField(max_length=255)
    address = models.CharField(max_length=520)
    city_id = models.IntegerField()
    zipcode = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=12, decimal_places=10)
    locality = models.CharField(max_length=255)
    longitude = models.DecimalField(max_digits=12, decimal_places=10)
    country_id = models.IntegerField()
    locality_verbose = models.CharField(max_length=255)


class User_Rating(models.Model):
    votes = models.PositiveIntegerField()
    rating_text = models.CharField(max_length=255)
    rating_color = models.CharField(max_length=255)
    aggregate_rating = models.DecimalField(max_digits=3, decimal_places=1)


class Full_details(models.Model):  # Corrected class name
    name = models.CharField(max_length=255)
    offers = models.CharField(max_length=255)
    cuisines = models.CharField(max_length=255)
    currency = models.CharField(max_length=3)
    location = models.OneToOneField(Location, on_delete=models.CASCADE)
    price_range = models.IntegerField()
    user_rating = models.OneToOneField(User_Rating, on_delete=models.CASCADE)
    mezzo_provider = models.CharField(max_length=255)
    order_deeplink = models.CharField(max_length=255)
    has_table_booking = models.BooleanField()
    is_delivering_now = models.BooleanField()
    opentable_support = models.BooleanField()
    has_online_delivery = models.BooleanField()
    include_bogo_offers = models.CharField(max_length=10)
    average_cost_for_two = models.DecimalField(max_digits=8, decimal_places=2)
    is_book_form_web_view = models.BooleanField()
    book_form_web_view_url = models.CharField(max_length=255)
    is_table_reservation_supported = models.BooleanField()

class Item(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)

class Restaurant(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    items = models.ManyToManyField(Item)
    lat_long = models.CharField(max_length=255)
    full_details = models.OneToOneField(Full_details, on_delete=models.CASCADE)



