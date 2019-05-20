from django.db import models

# Create your models here.


class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    category = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='restaurants/', blank=True, null=True)

    def __str__(self):
        return self.name

    def list_items_by_category(self):
        return {category: category.menu_items.all() for category in self.menu_categories.all().prefetch_related('menu_items')}


class MenuCategory(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menu_categories')
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    menu_category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE, related_name='menu_items')
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name


