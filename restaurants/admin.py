from django.contrib import admin
from .models import Restaurant, MenuCategory, MenuItem, Tab, TabItem


class MenuItemInline(admin.TabularInline):
    model = MenuItem


class MenuCategoryAdmin(admin.ModelAdmin):
    inlines = [
        MenuItemInline,
    ]


admin.site.register(Restaurant)
admin.site.register(MenuCategory, MenuCategoryAdmin)
admin.site.register(MenuItem)
admin.site.register(Tab)
admin.site.register(TabItem)

