# Video-courses-stripe-subscriptions

## 1. Clone the github repository and enter it
```
git clone https://github.com/MiddleZwei/Video-courses-web-app.git
cd Video-courses-web-app
```

## 2. Create and activate a virtual environment
Tested in Fedora 29:
```
virtualenv venv --python=`which python3`
```
Activate the virtual environment:
```
source venv/bin/activate
```

## 3. Install dependencies
```
pip install -r src/requirements.txt
```

## 4. Run the project
```
cd src
python manage.py runserver
```

## 5. Navigate
- Course list

``` 
http://127.0.0.1:8000/courses
```
- Amdin panel(user: admin, password: admin). You can create new users here and assign memberships types and subscriptions.
``` 
http://127.0.0.1:8000/admin
```
- Memberships. Log in to the admin panel first in order to access this page.
``` 
http://127.0.0.1:8000/memberships
```
- When "buying" new memberships, use these test card numbers
[Test cards here](https://stripe.com/docs/testing#cards)

## 5. Deactivate the virtual environment
```
deactivate
```

### PLease, note
- DB migrations are important.
- You can work with DB on the shell level, too, by using ``` python``` command in the terminal
