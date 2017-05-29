from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def view_workspace(request):
    args = {'user': request.user}
    return render(request, 'workspace/view_workspace.html', args)

