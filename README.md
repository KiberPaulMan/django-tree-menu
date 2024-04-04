# Запуск проекта
#### Создание и запуск виртуального окружения в директории:
1. python -m venv venv
2. .\venv\Scripts\activate
   
#### Установка зависимостей и применение миграций:
3. pip install -r .\requirements.txt
4. cd .\tree_menu\ | python manage.py migrate
   
#### Создание суперпользователя:
5. python manage.py createsuperuser
   
#### Запуск локального сервера:
6. python manage.py runserver

# Рабочий процесс
#### Создание меню в админ-панели:
7. <http://127.0.0.1:8000/admin/>
	
#### Вставка template tag {% draw_menu "your menu item" %} в шаблон check_menu.html (tree_menu/core/templates/core/check_menu.html) 
#### со своим параметром меню, например:
8. <{% draw_menu "Фрукты" %}>
	
#### Проверка работы меню:
9. <http://127.0.0.1:8000/check/>
 
