# Search for retakes website

![](project.gif)

Веб-сервис разработанный в качестве курсовой работы для университета. За основу был взят веб-фреймворк [Django](https://www.djangoproject.com), а также [DRF](https://www.django-rest-framework.org). 

Данное веб-приложение фильтрует имеющиеся в базе данных пересдачи при поступлении входящих данных от пользователя и выводит информацию по отфильтрованному списку пересдач обратно пользователю.

## Установка

Склонируйте git-репозиторий и установите зависимости.

```bash
git clone https://github.com/Dan1van/search_for_retakes_django.git
pip install -r requirements.txt
```

## Использование

Перейти в терминале в корневую папку и выполнить команду:

```bash
python manage.py runserver
```

Перейти в браузере по адресу: http://127.0.0.1:8000/search-retake/

Админ панель:

Адрес: http://127.0.0.1:8000/admin/

Логин: **admin**

Пароль: **admin**

# English

A web service designed for university coursework. It is based on the [Django](https://www.djangoproject.com) web framework. [DRF](https://www.django-rest-framework.org) was also used.

This web application filters the retakes available in the database upon receipt of incoming data from the user and displays information on the filtered list of retakes back to the user.

## Install


Clone the repository and install the requirements.


```bash
git clone https://github.com/Dan1van/search_for_retakes_django.git
pip install -r requirements.txt
```

## Usage

Go to the root folder and run this script:

```bash
python manage.py runserver
```

Then go to the address: http://127.0.0.1:8000/search-retake/

Admin panel:

Address: http://127.0.0.1:8000/admin/

Login: **admin**

Password: **admin**
