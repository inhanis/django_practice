from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from  .forms import LoginForm, MealAddForm
from django.contrib.auth.decorators import login_required
from restaurant.models import Restaurant, Category, Meal

# Create your views here.
def user_login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate(request, username=cd['username'], password=cd['password'])
			if user is not None:
				if user.is_active:
					login(request, user)
					return HttpResponse('Authenticated successfully')
				else:
					return HttpResponse('Disabled account')
			else:
				return HttpResponse('Invalid login')
	else:
		form = LoginForm
	return render(request, 'account/login.html', {'form':form})

@login_required
def dashboard(request):
	restaurant = get_object_or_404(Restaurant, owner=request.user)
	return render(request, 'account/dashboard.html', {'section':'dashboard', 'restaurant':restaurant})
	
@login_required
def meals_table(request):
	restaurant = get_object_or_404(Restaurant, owner=request.user)
	meals = Meal.objects.filter(restaurant=restaurant)
	return render(request, 'administrator/list.html', {'meals': meals})

@login_required
def add_meal(request):
	restaurant = get_object_or_404(Restaurant, owner=request.user)
	if request.method == 'POST':
		form = MealAddForm(request.POST, files=request.FILES)
		form.instance.restaurant = restaurant
		if form.is_valid():
			form.save()
			return redirect('meal_table')
		else:
			form = MealAddForm()
	else:
		form = MealAddForm()

	return render(request, 'administrator/list.html', {'form': form})

@login_required
def update(request, pk):
	meal = get_object_or_404(Meal, id=pk)
	form = MealAddForm(instance=meal)
	if request.method=="POST":
		form = MealAddForm(request.POST, instance=meal)
		if form.is_valid():
			form.save()
			return redirect('meal_table')
	return render(request, 'administrator/list.html', {'form': form})

@login_required
def delete(request, pk):
	meal = get_object_or_404(Meal, id=pk)
	if request.method=="POST":
		meal.delete()
		return redirect('meal_table')

	return render(request, 'administrator/delete.html', {'meal':meal})
