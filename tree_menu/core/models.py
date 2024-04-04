from django.conf import settings
from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=100, unique=True)
    head_menu = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    menu_url = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        menu_url = ''
        head_menu = self.head_menu
        current_menu = self

        while head_menu:
            menu_url = current_menu.title.replace(' ', '_') + '/' + menu_url
            current_menu = current_menu.head_menu
            head_menu = current_menu.head_menu

        self.menu_url = f'/{settings.MENU_URL_PREFIX}/{current_menu.title}/{menu_url}'
        super(Menu, self).save(*args, **kwargs)
