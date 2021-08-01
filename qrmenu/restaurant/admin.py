from django.contrib import admin
from .models import Restaurant, Category, Meal

# Register your models here.

admin.site.site_header = 'Digital Menu Dashboard'



@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug': ('name',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug': ('name',)}


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
	list_display = ['name', 'restaurant', 'category', 'price', 'available']
	list_filter = ('available', 'category', 'restaurant')
	list_editable = ['available']
	prepopulated_fields = {'slug': ('name',)}
	radio_fields = {'category': admin.VERTICAL, 'restaurant':admin.VERTICAL}