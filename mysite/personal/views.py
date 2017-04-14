from django.shortcuts import render

def index(request):
    return render(request, 'personal/home.html')

#def contact(request):
    #return render(request, 'personal/basic.html',
                 # {'content':
                   #['Want to contact me?, email me at fakeEmail@fakeEmail.com']}) 

def login(request):
    return render(request, 'personal/login.html')
