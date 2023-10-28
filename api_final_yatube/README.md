# api_final
<<<<<<< HEAD
# api_final
=======
>>>>>>> eb4d463adb2b3622b492901434cfa9dfdbaaebd7
### Описание:
Великолепно сделанный API, открывающий доступ к управлению постами, подписками и комментариями в YaTube.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:pavelsabanin/api_final_yatube.git
```

```
cd api_final_yatube.
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Примеры запросов и ответы на них:
Великолепно сделанный API, открывающий доступ к управлению постами, подписками и комментариями в YaTube.

1.GET-запрос 
http://127.0.0.1:8000/api/v1/posts/

Ответ:
```
[
    {
        "id": 1,
        "author": "papa777",
        "text": "string",
        "pub_date": "2023-09-07T07:31:30.511090Z",
        "image": null,
        "group": null
    },
```
2.POST-запрос:
http://127.0.0.1:8000/api/v1/follow/
Запрос:
```
{
"following": "papa777"
}
```
Ответ:
```
{
"user": "papa777",
"following": "papa777"
}
```
3.GET-запрос:
http://127.0.0.1:8000/api/v1/groups/

Ответ:
```
[
  {
    "id": 0,
    "title": "string",
    "slug": "string",
    "description": "string"
  }
]
```
<<<<<<< HEAD

=======
>>>>>>> eb4d463adb2b3622b492901434cfa9dfdbaaebd7
