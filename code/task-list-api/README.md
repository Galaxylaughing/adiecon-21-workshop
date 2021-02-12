# Task List API

## Skills Assessed

Solving problems with...

- some cool skill about apis

## Goal

You're very motivated to make a list of tasks.

![Image of Pikachu (the Pokemon) with a hard hat and two orange construction site cones](/assets/uc.gif)

Tasks have:

- Title (string)
- Description (string, nullable)
- Completed At (datetime, nullable)
- Created At (datetime)
- Updated At (datetime)

## One-Time Project Setup

Follow these directions once, a the beginning of your project:

1. Navigate to your projects folder named `projects`

```bash
$ cd ~/Developer/projects
```

2. "Clone" (download a copy of this project) into your projects folder.

```bash
$ git clone ...
```

Use `ls` to confirm there's a new project folder

3. Move your location into this project folder

```bash
$ cd task-list-api
```

4. Create a virtual environment named `venv` for this project:

```bash
$ python3 -m venv venv
```

5. Activate this environment:

```bash
$ source venv/bin/activate
```

Verify that you're in a python3 virtual environment by running:

- `$ python --version` should output a Python 3 version
- `$ pip --version` should output that it is working with Python 3

6. Install dependencies once at the beginning of this project with

```bash
# Must be in activated virtual environment
(venv) $ pip install -r requirements.txt
```

Summary of one-time project setup:

- [ ] `cd` into your `projects` folder
- [ ] Clone the project onto your machine
- [ ] `cd` into the `task-list-api` folder
- [ ] Create the virtual environment `venv`
- [ ] Activate the virtual environment `venv`
- [ ] Install the dependences with `pip`

## TODO: More Project Setup

![Image of Pikachu (the Pokemon) with a hard hat and two orange construction site cones](/assets/uc.gif)

- [ ] Make an `.env` file with this content:

```
FLASK_ENV=development

SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://postgres:postgres@localhost:5432/task_list_flask
```

- [ ] Using `psql`, create a database `task_list_flask`
- [ ] Run `flask db init`, then `flask db migrate`, then `flask db upgrade`
- [ ] Open Postman

## Project Development Workflow

1. When you want to begin work on this project, ensure that your virtual environment is activated:

```bash
$ source venv/bin/activate
```

![Image of Pikachu (the Pokemon) with a hard hat and two orange construction site cones](/assets/uc.gif)

11. When you are finished working for the day, deactivate your environment with deactivate or closing the Terminal tab/window

```bash
$ deactivate
```

## Project Write-Up: How to Complete and Submit

The goal of this project is to write code so that as many of the tests pass as possible.

To complete this project, use the above workflow and follow these steps:

![Image of Pikachu (the Pokemon) with a hard hat and two orange construction site cones](/assets/uc.gif)

1. Repeat on all test files until submission time.

At submission time, no matter where you are, submit the project via Learn.

### Reminders on Sending Things in Postman

![Image of Pikachu (the Pokemon) with a hard hat and two orange construction site cones](/assets/uc.gif)

- No query params
- Go to Body, Raw, select "JSON" in dropdown next to it

### Debugging Tips to Add/Remind

- restart server
- run flask migrate
- run flask upgrade

- unsure about what routes exist?
  - ```python
      print(app.url_map)
    ```

## Project Directions

![Image of Pikachu (the Pokemon) with a hard hat and two orange construction site cones](/assets/uc.gif)

Major sections:

- CRUD on a model named "Task"
- "complete" a task (via using `completed_at` attribute, and toggling through the route)
- Light sorting
- Light filtering
- One-to-many with Tags

The following sections are the required endpoints.

### `GET` `/tasks`

Gets a list of all tasks.

Response:

- Note that the response is a JSON array of JSON objects.
- Note that the response asks for `is_complete`, a boolean. We implied Tasks have a `completed_at` date.
- Note that the response asks for `id`. We implied Tasks have a `task_id` column.

```json
[
  {
    "description": "Test Description",
    "id": 4,
    "is_complete": false,
    "title": "Test Title"
  },
  {
    "description": "Test Description",
    "id": 3,
    "is_complete": false,
    "title": "Test Title"
  }
]
```

| Edge case | Expected behavior |
| --------- | ----------------- |
| no tasks  | empty array       |

### `POST` `/tasks`

Creates a new task. Assume that `title`, `description`, and `completed_at` are always supplied (even if `null` or empty string).

Body:

```json
{
  "title": "Test Title",
  "description": "Test Description",
  "completed_at": null
}
```

Response:

- Note that the response nests details in a key `"task"`.
- Note that the response asks for `is_complete`, a boolean. We implied Tasks have a `completed_at` date.
- Note that the response asks for `id`. We implied Tasks have a `task_id` column.

```json
{
  "task": {
    "description": "Test Description",
    "id": 4,
    "is_complete": false,
    "title": "Test Title"
  }
}
```

| Edge case           | Expected behavior |
| ------------------- | ----------------- |
| title missing/empty | Error             |

### `GET` `/tasks/<task_id>`

Gets the details for one task.

Response:

- Note that the response nests details in a key `"task"`.
- Note that the response asks for `is_complete`, a boolean. We implied Tasks have a `completed_at` date.
- Note that the response asks for `id`. We implied Tasks have a `task_id` column.

```json
{
  "task": {
    "description": "Test Description",
    "id": 4,
    "is_complete": false,
    "title": "Test Title"
  }
}
```

| Edge case      | Expected behavior |
| -------------- | ----------------- |
| task not found | 404               |

### `PUT` `/tasks/<task_id>`

Updates the details for one task. Assume that `title`, `description`, and `completed_at` are always supplied (even if `null` or empty string).

Body:

```json
{
  "title": "Edited Title",
  "description": "Edited Description",
  "completed_at": null
}
```

Response:

- Note that the response nests details in a key `"task"`.
- Note that the response asks for `is_complete`, a boolean.
- Note that the response asks for `id`.

```json
{
  "task": {
    "description": "Edited Description",
    "id": 2,
    "is_complete": false,
    "title": "Edited Title"
  }
}
```

| Edge case           | Expected behavior |
| ------------------- | ----------------- |
| task not found      | 404               |
| title is null/empty | error             |

### `DELETE` `/tasks/<task_id>`

Deletes one task.

Response:

```json
{
  "details": "Task 2 \"Edited Title\" successfully deleted"
}
```

| Edge case      | Expected behavior |
| -------------- | ----------------- |
| task not found | 404               |

### `PATCH` `/tasks/<task_id>/complete`

For one task, if its `completed_at` attribute is `null`, set it to `datetime.utcnow()`. If its `completed_at` attribute has a value, set it to `None`.

Response:

- Note that the response nests details in a key `"task"`.
- Note that the response asks for `is_complete`, a boolean.
- Note that the response asks for `id`.

```json
{
  "task": {
    "description": "Test Description",
    "id": 3,
    "is_complete": true,
    "title": "Test Title"
  }
}
```

| Edge case      | Expected behavior |
| -------------- | ----------------- |
| task not found | 404               |

### `GET` `/tasks/` Enhanced With Sorting

Use a query param with `sort=asc` or `sort=desc` to sort them by ascending or descending task ids

### `GET` `/tasks/` Enhanced With Filtering

Use a query param with `complete=true` or `complete=false` to filter by completeness

### Add Tags

Need to review scale, scope, and timing of this project. If there are multiple extra days and a need to reinforce this material:

1. Add a new model, `Tag`
   - `tag_id` (int) (primary key)
   - `label` (string) (required)
1. Establish a one-to-many relationship between `Task` and `Tag`s

Create the following endpoints in this order:

1. `GET` `/tags`
1. `POST` `/tags`
1. `PATCH` `/tasks/<task_id>/tags`. This endpoint should handle both adding and removing tags.

   - Body:
     ```json
     {
       "tags": ["array", "of", "tag", "ids"]
     }
     ```
   - Response:
     ```json
     {
       "task": {
         "id": 1,
         "tags": ["array", "of", "tag", "ids"]
       }
     }
     ```

1. `GET` `/tags/<tag_id>`, which should respond with
   - ```json
     {
       "id": 2,
       "label": "Fun",
       "tasks": [
         {
           "id": 1,
           "title": "Title",
           "description": "Description",
           "is_complete": false
         }
       ]
     }
     ```
