from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    prep_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name}({self.pk}) - {self.prep_count} times prepared"


class Recipe(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}({self.pk})"


class RecipeProduct(models.Model):
    recipe_id = models.ForeignKey(Recipe, verbose_name="Recipe", on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, verbose_name="Product", on_delete=models.CASCADE)
    weight = models.PositiveIntegerField()

    def __str__(self):
        return f"Recipe:{self.recipe_id} Product: {self.product_id} Weight: {self.weight}"
