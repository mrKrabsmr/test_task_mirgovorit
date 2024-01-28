from django.db import models
from app.model_core import BaseModel


class Product(BaseModel):
    name = models.CharField(max_length=255)
    usage_count = models.IntegerField(default=0)

    class Meta:
        db_table = "products"
        verbose_name = "продукт"
        verbose_name_plural = "продукты"

    def __str__(self):
        return self.name


class Recipe(BaseModel):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = "recipes"
        verbose_name = "рецепт"
        verbose_name_plural = "рецепты"

    def __str__(self):
        return self.name


class RecipeProduct(BaseModel):
    weight_gm = models.IntegerField(default=0)
    recipe = models.ForeignKey(to=Recipe, on_delete=models.CASCADE, related_name="products")
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, related_name="recipes")

    class Meta:
        db_table = "recipes_products"
        verbose_name = "Рецепт-Продукт"
        verbose_name_plural = "Рецепты-Продукты"
        unique_together = (
            ("recipe", "product"),
        )
