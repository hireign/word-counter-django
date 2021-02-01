# Word Counter with Django

Hello, this project is still in development. Meanwhile, below are a few commands to work with.

## Commands

- Creating a new project

  ```python
  django-admin startproject projectname
  ```

* Add an app to a project

  ```python
  python3 manage.py startapp appname
  ```

* Starting the server

  ```python
  python3 manage.py runserver
  ```

* Creating migrations

  ```python
  python3 manage.py makemigrations
  ```

* Migrate the database

  ```python
  python3 manage.py migrate
  ```

* Creating a Super User for the admin panel

  ```python
  python3 manage.py createsuperuser
  ```

* Collecting static files into one folder

  ```python
  python3 manage.py collectstatic
  ```

## Getting Started

### Dependencies

  - python3

    Make sure you are running python 3 with the latest version of pip installer

  - virtualenv

    To install virtualenv
    ```
    pip3 install virtualenv --user
    ```

### Running the Project

  1. Go to the project's root directory and create a virtualenv "myvenv"
  
  ```
  python3 -m venv myvenv
  ```

  2. Activate the virtualenv

  ```
  source myvenv/bin/activate
  ```

  2. Inside myvenv, update your pip
  
  ```
  python -m pip install --upgrade pip
  ```
  
  3. Install the requirements from requirements.txt
  
  ```
  pip install -r requirements.txt
  ```

  4. Run the project

  ```
  python3 manage.py runserver
  ```

  5. To deactivate the virtualenv
  
  ```
  deactivate
  ```
