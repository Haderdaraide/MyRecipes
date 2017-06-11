from django import forms

class AddRecipeForm(forms.Form):
    recipe_name = forms.CharField(label='Recipe Name', max_length=30)
    recipe_description = forms.CharField(label='Recipe Description:', max_length=300)
