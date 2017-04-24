from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm
from django.contrib.auth.models import User

def register(request):
    #return render(request, 'register/register.html')
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/')

    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'accounts/register.html', args)

def view_profile(request):
    return render(request, 'accounts/view_profile.html')

def edit_profile(request):
    pass


