import json
from django.db import transaction
import django
import csv
import json

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'search.settings')
django.setup()

from searchbar.models import Location, User_Rating, Full_details, Item, Restaurant

def create_restaurant(data):
    # Create Location object
    location_data = data['full_details']['location']
    location = Location.objects.create(
        city=location_data['city'],
        address=location_data['address'],
        city_id=location_data['city_id'],
        zipcode=location_data['zipcode'],
        latitude=location_data['latitude'],
        locality=location_data['locality'],
        longitude=location_data['longitude'],
        country_id=location_data['country_id'],
        locality_verbose=location_data['locality_verbose']
    )

    # Create User_Rating object
    user_rating_data = data['full_details']['user_rating']
    user_rating = User_Rating.objects.create(
        votes=user_rating_data['votes'],
        rating_text=user_rating_data['rating_text'],
        rating_color=user_rating_data['rating_color'],
        aggregate_rating=user_rating_data['aggregate_rating']
    )

    # Create Full_details object
    full_details_data = data['full_details']
    Full_Details = Full_details.objects.create(
        name=full_details_data['name'],
        offers=full_details_data['offers'],
        cuisines=full_details_data['cuisines'],
        currency=full_details_data['currency'],
        location=location,
        price_range=full_details_data['price_range'],
        user_rating=user_rating,
        mezzo_provider=full_details_data['mezzo_provider'],
        order_deeplink = full_details_data.get('order_deeplink', 0),
        has_table_booking=full_details_data['has_table_booking'],
        is_delivering_now=full_details_data['is_delivering_now'],
        opentable_support=full_details_data['opentable_support'],
        has_online_delivery=full_details_data['has_online_delivery'],
        include_bogo_offers=full_details_data['include_bogo_offers'],
        average_cost_for_two=full_details_data['average_cost_for_two'],
        is_book_form_web_view=full_details_data['is_book_form_web_view'],
        book_form_web_view_url=full_details_data['book_form_web_view_url'],
        is_table_reservation_supported=full_details_data['is_table_reservation_supported']
    )

    items_data = data['items']
    items = []
    for item_name, item_price in items_data.items():
        item = Item.objects.create(name=item_name, price=item_price)
        items.append(item)
    #Full_Details.items.set(items)

    # Create Restaurant object
    restaurant = Restaurant.objects.create(
        id = data['id'],
        name=data['name'],
        location=data['location'],
        #items = items,
        lat_long=data['lat_long'],
        full_details=Full_Details,
    )
    restaurant.items.set(items)
    return restaurant
	# items = []  # Create an empty list
	# for item_name, item_price in items_data.items():
	# 	item = Item.objects.create(name=item_name, price=item_price)
	# 	items.append(item)

	# restaurant.items.set(items)
	
	


# Usage



data = []
#count = 0

with open('restaurants_small.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        try:
            item_dict = {
                'id': int(row['id']) if row['id'] else 0,
                'name': row['name'],
                'location': row['location'],
                'items': json.loads(row['items']),
                'lat_long': row['lat_long'],
                'full_details': json.loads(row['full_details']) if row['full_details'] else {}  # Replace with default value if empty
            }
            data.append(item_dict)
        except json.JSONDecodeError as e:
            print(f"Error in row {row['id']}: {e}")

# for item in data:
#     try:
#         with transaction.atomic():
#             restaurant = create_restaurant(item)
#             print(f"Restaurant '{restaurant.name}' created successfully.")
#     except Exception as e:
#         print(f"Error creating restaurant: {e}")
restaurant = create_restaurant(data[21])