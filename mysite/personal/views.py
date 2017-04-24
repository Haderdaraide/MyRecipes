from django.shortcuts import render

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
    pass

