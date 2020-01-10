# maker
![alt text](https://github.com/caocmai/maker/blob/master/static/images/logo.png)

Maker is a dating app in which users can create and view profiles. Additionally, users can chat and send monetary gifts to people they admire.

### Basic Site Walk-through

New users are presented with a splash page with the ability to sign up for an account. Once a user is logged in they are taken to a page listing all current users on the website. The user can then find/filter other users based on gender. User can initiate a chat with another user. In addition, user can gift a small monetary amount to a user that they admire. 

### Features

* Account creation
* Profile creation with image upload
* Authenticated user can make posts
* Filtering profiles
* Chat
* Payment

### Prerequisites

Must have Django 3 and Python 2.7 installed

.To log into admin 

```
username: admin
email: admin@admin.com
password: admin
```
.To test the payment functionality

```
email: email@gmail.com
card number: 424242424242
MM/YY: 01/20
CVC: 123
```

### Proposal
https://docs.google.com/document/d/1UATtl4V7DAK-aZXU4PgvbDpJBYg753k5MAeIYXOOIa8/edit

### Installing

Project code can be viewed locally by cloneing or forking then open with any integrated development environment

To run project in an IDE, run the following in terminal
```
$ python3 manage.py runserver
```

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [Python](https://www.python.org/) - Language


## Django Addons
This project uses the following third party addons
* [crispy_forms](https://django-crispy-forms.readthedocs.io/en/latest/)
* [rest_framework](https://www.django-rest-framework.org/) 
* [channels](https://channels.readthedocs.io/en/latest/tutorial/part_2.html)
* [stripe payments](https://testdriven.io/blog/django-stripe-tutorial/#whats-next)

## Deployment

Project is deployed to https://maker-s-a.herokuapp.com/

## Authors

* Cao Mai - portfolio can be found at:
https://www.makeschool.com/portfolio/Cao-Mai
* Sebastian Abarca - portfolio can be found at: 
https://www.makeschool.com/portfolio/abrusebas16


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


## Acknowledgments
From this project we learn how to build a chat app and how to let the user upload images.
