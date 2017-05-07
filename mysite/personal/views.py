from django.shortcuts import render
from accounts.forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

def index(request):
    return render(request, 'personal/home.html')

#def contact(request):
    #return render(request, 'personal/basic.html',
                 # {'content':
                   #['Want to contact me?, email me at fakeEmail@fakeEmail.com']}) 

def login(request):
    return render(request, 'personal/login.html')

def logout(request):
    return render(request, 'personal/logout.html')

def home(request):
    return render(request, 'personal/home.html')

def apology(request):
    return render(request, 'personal/apology.html')

def view_profile(request):
    return render(request, 'accounts/view_profile.html')

def edit_profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/profile')

    else:
        form = UserChangeForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)

