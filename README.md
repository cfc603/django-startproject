# django-startproject-template

A modified "django-admin startproject" command using a custom template.

## Usage

###### Setup virtual enviroment

```
$ mkvirtualenv project_name
```

###### Install django-startproject-template

```
$ pip install git+git://github.com/cfc603/django-startproject-template.git@django-cms#egg=django-startproject-template
```

###### run startproject

django-startproject-template sets up the entire folder structure. Just move into the directory you would like create the project, then:
```
$ django-startproject.py project_name
```
The script will prompt for values to replace boilerplate variables with. These
variables allow for both the file contents and path names to be customized to
this specific project.

###### uninstall django-startproject-template

django-startproject-template is no longer needed
```
$ pip uninstall django-startproject-template
```

###### set environment variable 'DJANGO_SETTINGS_MODULE':

*(assuming use with virtualenvwrapper)*
```
$ subl $VIRTUAL_ENV/bin/postactivate
```
```shell
#!/bin/bash
# This hook is sourced after this virtualenv is activated.
export DJANGO_SETTINGS_MODULE='project_name.settings.local'
export PROJECT_DIR=/home/trevor/projects/project_name/source

```
```
$ source $VIRTUAL_ENV/bin/postactivate
```

###### initialize repo

```
$ cd $PROJECT_DIR
$ git init
```

###### install project requirements

```
$ pip install -r requirements.txt
```

Set versions installed:

```
$ pip freeze > requirements.txt
```

###### add repo to GitHub

[Create a new repository](https://github.com/new) with project_name

```
$ git add .
$ git commit -m "init"
$ git remote add origin git@github.com:cfc603/project_name.git
$ git push -u origin master
```

##### create local database

```
$ mysql -u admin -p
```

```SQL
CREATE DATABASE project_name;
exit
```

##### migrate database

```
$ ./manage.py migrate
```

## Using a custom project template

If you would prefer to use a custom project template than the one included in
this application, create your custom project template directory and call the
command script like this::

    django-startproject.py --template-dir=/your/custom/template project_name

###### Specifying boilerplate variables

Two optional files in the root of the project template directory are used to
determine the boilerplate variables:

``.startproject_boilerplate``
    Each line should contain the boilerplate variable (and optionally, a
    description of the variable, separated from the variable by white space).

``.startproject_defaults``
    Each line should contain a variable and the default value, separated by
    whitespace. If the default value contains ``PROJECT``, it is replaced with
    the project name.

See the files included in the project_template directory of StartProject for
an example.