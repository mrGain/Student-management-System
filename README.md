
# Student management system

This is a simple project of a Student management system.Where I used Django as backend to perform all CRUD opereations.And bootstrap in frontend to display all the data to the user in a simple manner.




### Source code :

Get the code here : [ https://github.com/mrGain/Student-management-System](https://github.com/mrGain/Student-management-System)



  
## Run Locally

Clone the project

```bash
  git clone https://github.com/mrGain/Student-management-System.git
```

Go to the project directory

```bash
  $ cd Student-management-System
```
 _Make sure you had python and  Django installed in your local system.If not follow the documents attached below._

Get the installation guide here : 
 ####
   Python installation: [ https://www.python.org/downloads/](https://www.python.org/downloads/)  \
   Django installation: [https://docs.djangoproject.com/en/3.2/topics/install/](https://docs.djangoproject.com/en/3.2/topics/install/)

If python and Djajngo is already installed in your pc than follow the following.

```bash
  ../Student-management-System $ python3 manage.py makemigrations   <hit enter_key>
  ../Student-management-System $ python3 manage.py migrate          <hit enter_key>
```
_Create the superuser_ to view the data base table in admin panel.
```bash
  ../Student-management-System $ python3 manage.py createsuperuser          <hit enter_key>
```
It will promt you to enter some basic details like _user name_ ,_email_ ,_password_ create all this than hit *Enter* .

Than to run the application in your local host just enter the following command.
```bash
../Student-management-System $ python3 manage.py runserver          <hit enter_key>
  Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
September 19, 2021 - 08:45:25
Django version 3.2.6, using settings 'student_mgmt.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

```
Now form terminal copy the development server which is http://127.0.0.1:8000/ and past is on the browser.


  
## Demo

![Alt text](relative/path/to/img.jpg?raw=true "Title")

  
## Documentation

- Here in my project I used ModelForm for taking the input from the user. Want to learn more about ModelForm get the document here :[ https://docs.djangoproject.com/...](https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/) 
- in frontend I used bootstrap chackout the documentation here :[https://getbootstrap.com/docs/..](https://getbootstrap.com/docs/5.1/getting-started/introduction/)