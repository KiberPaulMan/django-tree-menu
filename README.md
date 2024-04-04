# Запуск проекта
#### Создание и запуск виртуального окружения в директории:
1. python -m venv venv
2. .\venv\Scripts\activate
   
#### Установка зависимостей, создание и применение миграций:
3. pip install -r .\requirements.txt
4. python manage.py makemigrations
5. python manage.py migrate
   
#### Создание суперпользователя:
6. python manage.py createsuperuser
   
#### Запуск локального сервера:
7. python manage.py runserver

# Рабочий процесс
#### Создание меню в админ-панели:
8. <http://127.0.0.1:8000/admin/>
	
#### Вставка template tag в шаблон check_menu.html со своим параметром меню:
9.	<tree_menu/core/templates/core/check_menu.html>
	
#### Проверка работы меню:
10.	<http://127.0.0.1:8000/check/>
 
