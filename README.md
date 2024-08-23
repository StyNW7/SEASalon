# SEA Salon Full Stack using Django + Basic Front-end

This repository created for a selection at Software Engineering Academy by Compfest Academy 2024 🔥🔥

The project is already deployed on pythonanywhere, so you can see the website by clicking this URL:

<a href="https://xstynwx.pythonanywhere.com/">https://xstynwx.pythonanywhere.com/</a>

## Table of Contents
1. [Project Overview](https://github.com/StyNW7/SEASalon#Project-Overview)
2. [Prerequisite](https://github.com/StyNW7/SEASalon#Prerequisite)
3. [How to Use Website](https://github.com/StyNW7/SEASalon#How-to-Use-Website)
4. [Website Information](https://github.com/StyNW7/SEASalon#Website-Information)
5. [Owner](https://github.com/StyNW7/SEASalon#Owner)

## Project Overview

### Website Name
SEA Salon

### Explanation

Introducing SEA Salon, a rising star in the salon industry known for their outstanding services
and excellent reviews. With a rapidly growing clientele and a stellar reputation, SEA Salon is your
premier destination for all your beauty needs. Because of this, SEA Salon has gained a lot of
customers. To handle the new customers, the SEA Salon management team has decided to
develop a new SEA Salon Application.
This app lets users easily browse available services, select their preferred stylist, and book
appointments quickly. With a user-friendly interface and seamless booking integration, making a
reservation with a top stylist has never been easier!
The task will be divided into five progressive levels. The higher the level, the more points you can
earn. Note that each level builds on the previous one, so you must complete the earlier levels
before proceeding to the higher ones.

### Technology and Infrastructure

Fullstack using Django + Basic Front-end

Details:
- Back-end: Django
- Database: Database SQlite
- Front-end: HTML, CSS, JavaScript, and  jQuery

## Prerequisite

1. Python 3.x has been installed in your system.
2. Pip (package manager for Python) has been installed in your system.
3. Git has been installed in your system (If you prefer to use Git)

## How to Use Website

<!-- #### *This website is not deployed* -->

Therefore, this is the guidelines to use the website

### Step 1: Download Repository (Local / Fork Repository)

Users can download this repository locally or fork / copy this repository to their personal repository
<br> <br>
Meanwhile, if the user wants to clone the repository via URL, the user can use the following URL:

<code> https://github.com/StyNW7/SEASalon.git </code>

#### User can also Clone this repository (Remember the main branch is: master not main)

<code> git clone https://github.com/StyNW7/SEASalon.git </code>

### Step 2: Virtual Environment (Optional)

If you prefer to use Virtual Environment, You can use this step to create a Virtual Environment:

<code> python -m venv env </code>

To activate and use the Virtual Environment on Windows

<code> .\env\Scripts\activate </code>

To activate and use the Virtual Environment on MacOS / Linux

<code> source env/bin/activate </code>

However, this repository is also offer a Virtual Environment Folder (just in case you don't download the Virtual Environment Folder)

### Step 3: Move to the main Folder (seasalon)

When you have download or clone the repository, you should cd to the main folder which is seasalon

Use this at Terminal:

<code> cd seasalon </code>

### Step 4: Install Dependencies

This step is crucial to use the website. Firstly, You should install all of dependencies used in this Website

Run this code in the terminal

<code> pip install -r requirements.txt </code>

### Step 5: Database Setup (Optional)

I already provide the database, however if there is any changes You want to change, you should run this code

Just run this code (run in the terminal):

<code> python manage.py makemigrations </code>
<br>
<code> python manage.py migrate </code>

### Step 6: Run the Server

If you have already follow the step given above, the server can be run using this (run in the terminal):

<code> python manage.py runserver </code>

After that, the server is starting to run and You can click the localhost server like this:

<code> Starting development server at http://127.0.0.1:8000/ </code>

Or you can also open your browser and type <code> http://127.0.0.1:8000/ </code> manually

However, if you are using different localhost server, you can go to your own localhost server port


<!-- Other Guide -->

## Website Information

### Register and Login

User can register a new account, however user can only make a new Customer Account

And then user can login using the existing account

### Creating Admin User

If You want to create a new Admin user, you must follow this step:

Run this on Terminal:

<code> python manage.py create_custom_user </code>

Just input the data and make sure that the username and any other fields is unique from other data in the Database

After Creating Custom User succeed, You can login on the Website using the username and passsword you make and that user surely have an Admin role.

### Account example

If you want to testing the customer and admin role, you can just use this Account:

#### Customer Role

username: customer1
<br>
password: Customer123

#### Admin Role

username: thomas
<br>
password: Admin123

##### Hope this documentation and the guide useful and helpful to use the website!

<!-- Translation -->

## Translation

I also provide Documentation Translation in Indonesian right here:

<a href="Translation/INDONESIAN.md"> Indonesian Translation </a>

<!-- Owner -->

## Owner

This Repository is created by:
- Stanley Nathanael Wijaya

<code> Soli Deo Gloria ✨✨ </code>
