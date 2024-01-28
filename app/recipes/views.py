from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render

from app.recipes.services import RecipeService as R_s

constSuccessHtml = "<h3>Success</h3>"
constValidationErrorHtml = "Validation error: {}"


def add_product_to_recipe(request):
    recipe_id = request.GET.get("recipe_id")
    product_id = request.GET.get("product_id")
    weight_gm = request.GET.get("weight_gm")

    try:
        R_s.add_product_to_recipe(recipe_id=recipe_id, product_id=product_id, weight_gm=weight_gm)
    except ValidationError as err:
        return HttpResponse(content=constValidationErrorHtml.format(err))

    return HttpResponse(content=constSuccessHtml)


def cook_recipe(request):
    recipe_id = request.GET.get("recipe_id")

    try:
        R_s.cook_recipe(recipe_id=recipe_id)
    except ValidationError as err:
        return HttpResponse(content=constValidationErrorHtml.format(err))

    return HttpResponse(content=constSuccessHtml)


def show_recipes_without_product(request):
    product_id = request.GET.get("product_id")

    try:
        recipes = R_s.get_recipes_without_product(product_id=product_id)
    except ValidationError as err:
        return HttpResponse(content=constValidationErrorHtml.format(err))

    return render(request=request, template_name="recipes_table.html", context={"recipes": recipes})
