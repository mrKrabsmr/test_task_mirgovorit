from django.core.exceptions import ValidationError
from django.db.models import F

from app.recipes.models import Recipe, Product, RecipeProduct
from app.recipes.utils import check_required_arguments
from app.service_core import BaseService


class ProductService(BaseService):
    _queryset = Product.objects.all()

    @classmethod
    def increment_usage_count(cls, recipe):
        cls._queryset.prefetch_related("recipes").filter(recipes__recipe=recipe).update(
            usage_count=F("usage_count") + 1
        )


class RecipeProductService(BaseService):
    _queryset = RecipeProduct.objects.all()

    @classmethod
    def create(cls, **kwargs):
        recipe_product = cls.get_by_params(
            recipe=kwargs.get("recipe"), product=kwargs.get("product")
        ).first()

        weight_gm = kwargs.get("weight_gm")
        if not weight_gm.isdigit():
            raise ValidationError("weight must be a number")

        if recipe_product:
            recipe_product.weight_gm = weight_gm
            recipe_product.save()
        else:
            cls._queryset.create(**kwargs)


class RecipeService(BaseService):
    _queryset = Recipe.objects.all()

    @classmethod
    @check_required_arguments
    def add_product_to_recipe(cls, *, recipe_id, product_id, weight_gm):
        recipe = cls.get_one(recipe_id)
        product = ProductService.get_one(product_id)
        RecipeProductService.create(recipe=recipe, product=product, weight_gm=weight_gm)

    @classmethod
    @check_required_arguments
    def cook_recipe(cls, *, recipe_id):
        recipe = cls.get_one(recipe_id)
        ProductService.increment_usage_count(recipe)

    @classmethod
    @check_required_arguments
    def get_recipes_without_product(cls, *, product_id):
        product = ProductService.get_one(product_id)
        return cls._queryset.prefetch_related("products").exclude(
            products__in=RecipeProduct.objects.filter(product=product, weight_gm__gte=10)
        )
