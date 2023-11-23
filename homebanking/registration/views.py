from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .forms import LoginForm

def loginView(request):
    form = LoginForm(request.POST)
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            dni = form.cleaned_data['dni']
            contrasena = form.cleaned_data['contrasena']
            user = authenticate(request, username=dni, password=contrasena) # Verificar esos nombres si estan asi en la db

            if user is not None:
                login(request, user)
                messages.success(request, 'Inicio de sesión exitoso.')
                return redirect(reverse('home'))
            else:
                messages.error(request, 'DNI o contrasena incorrectos.')

    else:
        form = LoginForm(request.POST)

    return render(request, 'home/home.html', {'form': form})
