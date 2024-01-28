from django.contrib import admin
from django.urls import path

from app.recipes.views import add_product_to_recipe, cook_recipe, show_recipes_without_product

urlpatterns = [
    path("admin/", admin.site.urls),
    path("recipes/add-product/", add_product_to_recipe),
    path("recipes/cook/", cook_recipe),
    path("recipes/list/without-product/", show_recipes_without_product)
]
