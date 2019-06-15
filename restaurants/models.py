from django.db import models
import uuid
from django.apps import apps
from django.db.models import Q
from datetime import datetime
# Create your models here.


def generate_code():
    Tab = apps.get_model('restaurants.Tab')
    while True:
        code = uuid.uuid4().hex[:7].upper()
        if not Tab.objects.filter(code=code).exists():
            break
    return code


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


class Tab(models.Model):
    # TODO: Override save to only allow saving when there is no other tab at the given table at the current time
    menu_items = models.ManyToManyField(MenuItem, through='TabItem')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='tabs')
    ordered_at = models.DateTimeField(auto_now_add=True)
    paid_at = models.DateTimeField(blank=True, null=True)
    code = models.CharField(default=generate_code, unique=True, editable=False, max_length=7)


class TabItem(models.Model):
    #TODO: Automatically enter Tab paid_at date when all TabItems for that tab is paid for
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    tab = models.ForeignKey(Tab, on_delete=models.CASCADE, related_name='tab_items')
    debt = models.DecimalField(max_digits=6, decimal_places=2, default=-1)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.debt = self.menu_item.price
        super(TabItem, self).save(*args, **kwargs)
        if not self.tab.tab_items.filter(~Q(debt=0.00)).exists():
            self.tab.paid_at = datetime.now()
            self.tab.save()

