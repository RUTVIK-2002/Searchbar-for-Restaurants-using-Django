from django.shortcuts import render
from .models import Restaurant,User_Rating,Location,Full_details,Item
from django.db.models import Q 

# Create your views here.

def Search(request):
    q = request.GET.get('q') if request.GET.get('q') else ''
    #print(q)
    Search = Restaurant.objects.filter(
        Q(name__icontains=q) | Q(items__name__icontains=q)).distinct().order_by('-full_details__user_rating__aggregate_rating')
    restaurants = Restaurant.objects.all()[:15]
    #print(Search)
    context = {'Restaurants': Search[:25],'q':q}
    return render(request, 'searchbar/home.html', context)
