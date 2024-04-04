from django.contrib import admin
from .models import Menu


class MenuAdmin(admin.ModelAdmin):
    exclude = ['menu_url']


admin.site.register(Menu, MenuAdmin)
