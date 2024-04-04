from django.shortcuts import render


def get_menu(request):
    return render(request, 'core/menu.html')


def check_menu(request):
    return render(request, 'core/check_menu.html')
