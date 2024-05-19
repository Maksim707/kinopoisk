from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import authenticate, login, logout



def signin(request):
	if request.user.is_authenticated:
		return redirect('profile')

	if request.method =='POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password) 
		if user == None:
			return render(request, 'Core/signin.html', {
					'error': 'Пароли не совпадают'
			})
		login(request, user)
		

	return render(request, 'Core/signin.html',)



def signup(request):
	if request.user.is_authenticated:
		return redirect('profile')


	if request.method =='POST':
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		repeat_password = request.POST['repeat_password']
		if repeat_password != password:
			return render(request, 'Core/signup.html', {
				'error': 'Пароли не совпадают'
			})
		User.objects.create_user(
			username=username,
			email=email,
			password=password,
		)
		return redirect('signin')

	return render(request, 'Core/signup.html',)

def profile(request):
	if not request.user.is_authenticated:
		return redirect('signin')


	return render(request, 'Core/profile.html')

def signout(request):
	if not request.user.is_authenticated:
		return redirect('signin')

	logout(request)
	return redirect('catalog')