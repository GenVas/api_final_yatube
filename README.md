# Социальная сеть Yatube  с возможностями API

##Описание проекта

Проект позволяет использовать API для чтения создания, редактирования и комментирования постов в мини-социальной сети Yatube. В проекте отсутствует код для доступа через браузер. Проект написан на языке Python.
В проекте предусмотрена аутентиикация по токену JWT для возможности публикации, редактирования и комментарирования постов.
Контакты разработчика: vasilievga@yandex.ru


##Как запустить проект

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/GenVas/api_final_yatube.git
```

```
cd api_final_yatube
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


##Примеры. (Некоторые примеры запросов к API)
По адресу  http://127.0.0.1:8000/redoc/ доступна документация для **API Yatube**.
Вот **примеры запросов** API YAtube:
  http://127.0.0.1:8000/api/v1/posts/ (получение списка, и публикация поста)
  http://127.0.0.1:8000/api/v1/posts/1 (получение поста)
  http://127.0.0.1:8000/api/v1/posts/1/comments/ (комментирование поста)
  http://127.0.0.1:8000/api/v1/posts/1/follow/ (подписка на участника социальной сети)
  http://127.0.0.1:8000/api/v1/posts//groups/ (получение списка групп, создавать группы может только админ)
  http://127.0.0.1:8000/api/v1/posts//groups/1 (получение инфрмации о группе)

