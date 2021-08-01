from django.urls import path
from . import views

app_name = 'restaurant'

urlpatterns = [
	path('', views.index, name='index'),
	path('<slug:restaurant_slug>/', views.category_list, name='category_list'),
	path('<slug:restaurant_slug>/<slug:category_slug>/', views.meal_list, name='meals_list_by_category'),
]
