from django.contrib import admin
from .models import Restaurant, MenuCategory, MenuItem, Tab, TabItem

# Register your models here.


admin.site.register(Restaurant)
admin.site.register(MenuCategory)
admin.site.register(MenuItem)
admin.site.register(Tab)
admin.site.register(TabItem)

