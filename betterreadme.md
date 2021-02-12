# Enough Python/Flask to TA for C15 Workshop, AdieCon 2021

## Learning Goals

- Get familiar with how to pick up Python syntax
- Learn small common debugging hurdles
- Get a little more familiar with the Ada Core curriculum
- Make TAing at Ada more fun and approachable :)

## Assumptions

- You know a programming language like Ruby
- You’re on a machine running macOS

## Format

- Switch between talking points, livecode, and writing code rapidly.
- Get your text editor out!
- Be comfortable with tuning me out and driving your own curiosity!
- ✨ Ask questions in Slack ✨ and ✨ help each other ✨

## Resources

- [Presentation Deck](tinyurl.com/2leyu3ra)
- [Presentation Repo (this repo!)](github.com/tildeee/adiecon-21-workshop)
- Our Slack channel: #workshop-python-and-flask

## Python Installation and Python 3

The difference between Python 2 and Python 3 is huge and worth caring about.

Most macOS machines come with Python 2 installed, so `$ python` points to Python 2.

**It's important that we always use Python 3** so we'll execute most Python commands with `$ python3`

Verify this fact:

```bash
$ python --version # prints out version 2
$ python3 --version # prints out version 3
```

We'll want to prefer:

```bash
$ python3 main.py # Runs a Python program in main.py
$ python3 -m pytest # Runs a module named pytest, explicitly with Python 3
```

_There are ways around this_. One will be covered later, specifically for project workflows.

## Python Syntax Crash Course: Fizzbuzz

Read more in [Simon's Ruby to Python Guide](simons_ruby_to_python_guide.md).

Make a file named `fizzbuzz.py` and run it with `$ python3 fizzbuzz.py`.

Grab the solution code in [code/fizzbuzz/fizzbuzz.py](code/fizzbuzz/fizzbuzz.py).

## OOP in Python: `self`

- OOP syntax in Python is "straightforward"
- In Python, for every instance method, we should always define a first parameter conventionally named `self`. This represents the instance itself.
- We read/store instance members (attributes and methods) through `self`

Replace `fizzbuzz.py` with a `Fizzbuzz` class.

Grab the solution code in [code/fizzbuzz/oop_fizzbuzz.py](code/fizzbuzz/oop_fizzbuzz.py)

## Testing in Python: pytest

- We're choosing pytest as our testing library
- Globally install pytest with `$ python3 -m pip install pytest` or `$ pip3 install pytest`
- Import pytest with `import pytest`
- Run the tests with `$ python3 -m pytest fizzbuzz.py`
  - There are ways to configure your situation so you don't need this full command, but most of the time (in the curriculum) we'll do it like this
  - An exception is in projects (details below)
- Unit tests are methods that start with `test_` or end with `_test`
- To assert something, use `assert expression_that_must_be_true`

Add unit tests right below the `Fizzbuzz` class in `fizzbuzz.py`.

Grab the solution code in [code/fizzbuzz/test_fizzbuzz.py](code/fizzbuzz/test_fizzbuzz.py).

## Project: Viewing Party

![Image of Pikachu (the Pokemon) with a hard hat and two orange construction site cones](assets/uc.gif)

Included is:

- Current in-progress version of README
- Unit tests (project is TDD with 5 waves)
- Empty `viewing_party/main.py` file
- A solution in `soln/main.py`. Copy and paste content into other `main.py` to see.

From root directory, run the tests with

```bash
$ python3 -m pytest code/viewing-party/
```

## Preview of Learn

Read more in the [Learn Preview document](learn_preview.md).

## Flask Tooling

Flask is a cool micro web framework.

We are primarily using it to teach how to write back-end APIs. Flask _does_ support views/templates, and the curriculum will lightly touch on it.

Projects will ask students to use a virtual environment with `venv`.

Virtual environments in Python:

- Are one of many ways to manage dependencies. Virtual environments with `venv` are common.
- When activated, if the virtual environment was made with Python 3, then
  - the `$ python` command will default to using Python 3
  - the `$ pytest` command will default to using Python 3
  - `$ pip` will default to using Python 3
  - Virtual environments are great **while they're activated**

- We'll instruct students to name their virtual environments `venv`
  - Activate this with `$ source venv/bin/activate`
  - Deactivate with `$ deactivate`
  - You'll know it's activated if you see `(venv)` in the command prompt

- Dependencies are "managed" (listed lol) in a file conventionally named `requirements.txt`

- Postgres for DB. Students will learn basic SQL. Get your `$ psql` on.
  - Restart postgres process with `$ brew services restart postgresql`

Other commands we may anticipate seeing:

- Migrating using Flask-Migrate
  - `$ flask db init`
  - `$ flask db migrate` for initial migration
  - `$ flask db upgrade` for subsequent migrations

Create a new project directory named `hello_world_api` and create a virtual environment named `venv` in it:

```bash
$ cd ~/Developer
$ mkdir hello_world_api
$ cd hello_world_api
$ python3 -m pip install virtualenv # install virtualenv with python3
$ python3 -m venv venv # create a virtual env named venv
$ source venv/bin/activate # activate venv
(venv) $ echo "Success activation"
(venv) $ deactivate
$ echo "Successful deactivation
```

## Returning JSON in Flask

Install Flask in an activated virtual environment with `$ pip install flask`

Flask defaults to looking for the file `app.py`.

Grab the solution code in [code/flask-hello-world/app.py](code/flask-hello-world/app.py) and put it in `app.py`.

Run the server with either command:

```bash
$ flask run
$ FLASK_ENV=development flask run # Development env enables hot-reloading on code changes ;)
```

Make an endpoint for a `GET` at `/adiecon` and make it return `{ “adieCon”: True, “success”: True }`.

## Project: Task List API

![Image of Pikachu (the Pokemon) with a hard hat and two orange construction site cones](assets/uc.gif)

Included is:

- Current in-progress version of README
- A minimal version of this project in one file, `code/task-list-api/app.py`

**This project has a lot of dependencies**.

Because there are a lot of dependencies, it's worth using a virtual environment here. Copy the `task-list-api` folder over into a new project directory, or `cd` in here.

## Conclusion

The new curriculum won’t be perfect for C15, but I truly hope we get your support, patience, and partnership

We are committed to making the curriculum always better and better, but it takes time.

Thank you so much and see you online.
