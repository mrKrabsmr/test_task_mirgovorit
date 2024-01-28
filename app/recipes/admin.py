from django.contrib import admin
from django.contrib.auth.models import User, Group

from app.recipes.models import Product, Recipe, RecipeProduct

admin.site.site_header = "Рецепты онлайн"

admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


class RecipeProductInline(admin.TabularInline):
    model = RecipeProduct
    extra = 0


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = (RecipeProductInline,)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.prefetch_related("products")