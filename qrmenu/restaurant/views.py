from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Restaurant, Category, Meal
from django.contrib.auth.decorators import login_required
from cart.forms import CartAddProductForm

# Create your views here.

def index(request):
	restaurants = Restaurant.objects.all()

	return render(request, 'index.html', {'restaurants': restaurants})


def meal_list(request, restaurant_slug, category_slug=None):
	category = None
	restaurant = get_object_or_404(Restaurant, slug=restaurant_slug)
	meals = Meal.objects.filter(restaurant=restaurant)
	categories = set(list(Category.objects.filter(meals__restaurant=restaurant)))
	cart_product_form = CartAddProductForm()
	if category_slug:
		category = Category.objects.get(slug=category_slug)
		meals = meals.filter(category=category)
	return render(request, 'meal/list.html', {'meals': meals, 'categories': categories, 'restaurant': restaurant, 'category': category, 'cart_product_form': cart_product_form})

def category_list(request, restaurant_slug):
	restaurant = get_object_or_404(Restaurant, slug=restaurant_slug)
	meals = Meal.objects.filter(restaurant=restaurant)
	categories = set(list(Category.objects.filter(meals__restaurant=restaurant)))

	return render(request, 'meal/category_list.html', {'restaurant': restaurant, 'categories': categories})
