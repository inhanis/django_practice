from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
	#path('login/', views.user_login, name='login'),
	path('login/', auth_views.LoginView.as_view(), name='login'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),
	path('', views.dashboard, name='dashboard'),
	path('table/', views.meals_table, name='meal_table'),
	path('table/add', views.add_meal, name='add_meal'),
	path('table/update/<int:pk>', views.update, name='update'),
	path('table/delete/<int:pk>', views.delete, name='delete'),	
]
