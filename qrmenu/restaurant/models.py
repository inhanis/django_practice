from django.db import models
from django.conf import settings

# Create your models here.

class Restaurant(models.Model):
	owner = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="restaurant", on_delete=models.CASCADE)
	name = models.CharField(max_length=200, db_index=True)
	slug = models.SlugField(max_length=200, unique=True)
	logo = models.ImageField(upload_to='logos/', blank=True)


	def __str__(self):
		return str(self.name)

class Category(models.Model):
	name = models.CharField(max_length=200, db_index=True)
	slug = models.SlugField(max_length=200, unique=True)
	logo = models.ImageField(upload_to='categories/', blank=True)

	class Meta:
		verbose_name_plural = 'categories'

	def __str__(self):
		return str(self.name)

class Meal(models.Model):
	restaurant = models.ForeignKey(Restaurant, related_name='meals', on_delete=models.CASCADE, db_index=True)
	category = models.ForeignKey(Category, related_name='meals', on_delete=models.CASCADE, db_index=True)
	name = models.CharField(max_length=200, db_index=True)
	slug = models.SlugField(max_length=200, db_index=True)
	price = models.DecimalField(max_digits=10, decimal_places=0)
	overview = models.TextField(blank=True)
	def get_file_path(self):
		return 'meals/%r'%(self.restaurant.name)
	image = models.ImageField(upload_to='', blank=True)
	available = models.BooleanField(default=True)

	def __str__(self):
		return str(self.name)
