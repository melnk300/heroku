#Diary

production ver

## Routes


### Users
| case  |  path | payload | error | success | jwt [get - post] |
|---|---|---|---|---|---|
| get all group members  | api/users/<group_id> (GET) | - | 404 - group_id not found| [ { Group. group_name, User.name, User.id}, ... ] | [-] [-] |
| get user data | api/user/<user_id> (GET) | - |  404 - User id not found | { Group.group_id, Group.group_name, User.id, User.login } | [-] [-] |
| register user | api/user/ (PUT) | {login, password } | 403 - User already created| { success } | [-] [x]|
| login user  | api/user/ (POST) | {login, password } | 401 - Login - password pair is incorrect| { success } | [-] [x] |
| logout user | api/user/ (DELETE) | - | - | - | [x] [x] |

**For all!Ж 402 - Unauthorized (CORS Headerless error)**

### Tasks
case  |  path | payload | error | success | jwt |
|---|---|---|---|---| --- |
| get all tasks by group  | api/tasks/<group_id>/<data>  (GET) | - | - | [ {Task.id, Task.author, Task.subject, Task.task}, ... ] | [x]|
| add task by group | api/tasks/<group_id>/<data>  (POST) | { subject, task } | - | {success} | [x] |
| delete task by group | api/tasks/<id> (DELETE) | -| 404 - task not found|{success}| [x] |

**For all!: 402 - Unauthorized (CORS Headerless error)**

### Groups

| case  |  path | payload | error | success | jwt |
|---|---|---|---|---|---|
| register group | api/group/<group_name> (POST) | - | 403 - Group already created | {success, Group.group_id} | [-] |
| update group | api/group/<group_name> (PATCH) | - |  404 - Group name not found | [-] |