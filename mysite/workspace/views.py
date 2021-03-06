from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from workspace.forms import AddRecipeForm

# Create your views here.

@login_required
def view_workspace(request):
    args = {'user': request.user}
    return render(request, 'workspace/dashboard.html', args)


def my_recipes(request):
    args = {'user': request.user}
    return render(request, 'workspace/my_recipes.html', args)


def add_recipe(request):
    if request.method == 'POST':
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/workspace/')

    else:
        form = AddRecipeForm

    return render(request, 'workspace/add_recipe.html', {'form': form})


def view_profile(request):
    args = {'user': request.user}
    return render(request, 'workspace/view_profile.html', args)
