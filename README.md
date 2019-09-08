# Django_languages_identification

# First Clone the git repo
>>https://github.com/sandeshdeshmukh1/Django_languages_identification.git

# Install Python: Windows
>>You can download Python for Windows from the website https://www.python.org/downloads/windows/. Click on the "Latest Python 3 Release - Python x.x.x"
# Install Python: Debian or Ubuntu
>>$ sudo apt install python3

# Set up virtualenv and install Django
So, let's create a virtual environment (also called a virtualenv). Virtualenv will isolate your Python/Django setup on a per-project basis. This means that any changes you make to one website won't affect any others you're also developing. Neat, right?

$ mkdir Django_languages_identification
$ cd Django_languages_identification


We will make a virtualenv called myvenv. The general command will be in the format:

$python3 -m venv myvenv

# Virtual environment: Windows
>>C:\Users\Name\Django_languages_identification> python -m venv myvenv

# Virtual environment: Linux and OS X
>>$ python3 -m venv myvenv

In this case, follow the instructions above and install the python3-venv package:
>>$ sudo apt install python3-venv

NOTE: On some versions of Debian/Ubuntu initiating the virtual environment like this currently gives the following error:
>> Error: Command '['/home/eddie/Slask/tmp/venv/bin/python3', '-Im', 'ensurepip', '--upgrade', '--default-pip']' returned non-zero exit status 1

To get around this, use the virtualenv command instead.
$ sudo apt install python-virtualenv
$ virtualenv --python=python3.6 myvenv

# Working with virtualenv

# Working with virtualenv: Windows
>>C:\Users\Name\Django_languages_identification> myvenv\Scripts\activate

# Working with virtualenv: Linux and OS X
>>$ source myvenv/bin/activate

# Installing Django

Now that you have your virtualenv started, you can install Django

we should make sure we have the latest version of pip, the software that we use to install Django:

>>(myvenv) ~$ python -m pip install --upgrade pip

# Installing Django
First create a requirements.txt file inside of the Django_languages_identification/ folder, using the code editor that you installed earlier. You do this by opening a new file in the code editor and then saving it as requirements.txt in the Django_languages_identifications/ folder. Your directory will look like this:

Django_languages_identifications
└───requirements.txt

In your  Django_languages_identification/requirements.txt file you should add the following text:
version-->>Django~=2.2.5

Now, run pip install -r requirements.txt to install Django.

output>>(myvenv) ~$ pip install -r requirements.txt
Collecting Django~=2.2.4 (from -r requirements.txt (line 1))
  Downloading Django-2.2.4-py3-none-any.whl (7.1MB)
Installing collected packages: Django
Successfully installed Django-2.2.5

# makemigrations:

$ python manage.py makemigrations
output>>Migrations for 'books':
  books/migrations/0003_auto.py:
    - Alter field author on book
  
$ python manage.py migrate
output>>Operations to perform:
  Apply all migrations: books
Running migrations:
  Rendering model states... DONE
  Applying books.0003_auto... OK
  
To run finally  You Have To Run app using below Command

$python manage.py runserver



# Credits
Hrithik Auchar-->>https://github.com/hvauchar
