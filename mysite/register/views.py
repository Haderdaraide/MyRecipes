from django.shortcuts import render, redirect
from register.forms import RegistrationForm
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
        return render(request, 'register/register.html', args)

#def profile(request):
    #args = {'user': request.user}

