from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe
from .forms import RecipeForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index_view(request):
    recipes = Recipe.objects.all().order_by('?')[:5]
    return render(request, 'index.html', {'recipes': recipes})

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipe_detail.html', {'recipe': recipe})

@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                recipe = form.save(commit=False)
                recipe.author = request.user
                recipe.save()
                return redirect('recipes:recipe_detail', pk=recipe.pk)
            except Exception as e:
                return HttpResponse(f"Ошибка сохранения: {e}")
        else:
            return render(request, 'add_recipe.html', {'form': form, 'errors': form.errors})
    else:
        form = RecipeForm()
    return render(request, 'add_recipe.html', {'form': form})

