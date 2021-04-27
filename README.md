#Diary

API(бот в разработке) для интернет дневника.

## Использованные технологии:
 - **postgres + psycopg2 + sqlalchemy (База находится на VPS)**
 - **flask(BP - arch) + cookie-first jwt auth + VK Callback (Хостится на Heroku - diarya.rusm.site)**
 - **bcrypt - безопасное хэширование паролей**
 - **логирование посредствам Logging**
    

## Архитектура
 - **Роутинг на основе версионированных Blueprints**
 - **Cookie-first аутентификация, позволяющая не заботиться о refresh-токене, обеспечивающая большую безопасность передачи данных**

### Структура:

1. api
    1. \<resource>_api - сервис с регистрацией Blueprint
2. data
   1. models
        1.\<model> - файл моделей объектов БД
   2. db_session - служебный файл БД
3. utils
    1. cfg - файл конфигурации подключений и хранения данных
    2. utils - файл со служебными функциями
4. Procfile - служеюный файл сервинга приложения на Heroku средствами Gunicorn
5. app - инициализирующий файл приложения
6. log.log - файл логгирования
7. .gitignore - служебный файл git

### Нюансы
**Аренда доммена и подписание SSL-сертификата - REG.RU**
**Выделенная VPS под БД - Triangle.is**  
**Колличество кода: 521 строка**![img.png](trash/img.png)
**!В связи с малой поддержкой мультиплатформы python при Import-error на Win-машинах каждую директорию в PyCharm стоит промаркировать как модуль!**
![img.png](trash/mark_as.png)
## Routes


### Users
| case  |  path | payload | error | success | jwt [get - post] |
|---|---|---|---|---|---|
| get all group members  | api/users/<group_id> (GET) | - | 404 - group_id not found| [ { Group. group_name, User.name, User.id}, ... ] | [-] [-] |
| get user data | api/user/<user_id> (GET) | - |  404 - User id not found | { Group.group_id, Group.group_name, User.id, User.login } | [-] [-] |
| register user | api/user/ (PUT) | {login, password } | 403 - User already created| { success } | [-] [x]|
| login user  | api/user/ (POST) | {login, password } | 401 - Login - password pair is incorrect| { success } | [-] [x] |
| logout user | api/user/ (DELETE) | - | - | - | [x] [x] |

**For all!: 402 - Unauthorized (CORS Headerless error)**

### Tasks
case  |  path | payload | error | success | jwt |
|---|---|---|---|---| --- |
| get all tasks by group  | api/tasks/<group_id>/\<data>  (GET) | - | - | [ {Task.id, Task.author, Task.subject, Task.task}, ... ] | [x]|
| add task by group | api/tasks/<group_id>/\<data>  (POST) | {subject, task } | - | {success} | [x] |
| delete task by group | api/tasks/<id> (DELETE) | -| 404 - task not found|{success}| [x] |

**For all!: 402 - Unauthorized (CORS Headerless error)**

### Groups

| case  |  path | payload | error | success | jwt |
|---|---|---|---|---|---|
| register group | api/group/<group_name> (POST) | - | 403 - Group already created | {success, Group.group_id} | [-] |
| update group | api/group/<group_name> (PATCH) | - |  404 - Group name not found | { success } | [-] |

## Client-side
[front](https://gitlab.com/melnk300/diaryfront)

## Использованные технологии:

- **Vue + rumex components**
- **VUEx state manager**
- **Axios**
- **LocalStorage**

### Инструкция:
0. Установка Node.js
1. git clone https://gitlab.com/melnk300/diaryfront
2. npm i
3. npm run serve
4. Перейти на localhost:8080