# Django JWT Authentication and User Registration API
![CodeRabbit Pull Request Reviews](https://img.shields.io/coderabbit/prs/github/sudhanshu-jha/authservice?utm_source=oss&utm_medium=github&utm_campaign=sudhanshu-jha%2Fauthservice&labelColor=171717&color=FF570A&link=https%3A%2F%2Fcoderabbit.ai&label=CodeRabbit+Reviews)

##
This is a Django project that provides two REST APIs: one for JWT authentication and one for user registration. 
The JWT authentication API uses the Django Rest Framework SimpleJWT package to provide JSON Web Token (JWT) authentication, 
while the user registration API allows users to register a new account by providing a username, email, and password.

## Getting started
To run the project locally, follow these steps:

### 1 .Clone the repository:

```bash
git clone https://github.com/your_username/django-jwt-authentication.git
```
### 2 . Install the dependencies:
```python
pip install -r requirements
```
### 3 . Running the developement server
```python
    python manage.py runserver
```
## API endpoints

- `/admin/`: The Django admin site.
- `/api-auth/` : The Django Rest Framework built-in authentication views.
- `/`: The main project app's views.
- `/api/token` : This endpoint handled JWT authentication requests.
- `/api/token/refresh/`: This endpoint handles requests to refresh an expired JWT token.
- `/api/hello` : This endpoint is protected by JWT authentication and returns 'Hello World!' message when accessed by an authenticated user
- `/api/register` This endpoint handles user registration requests

## JWT authentication API:

To obtain and access token, send a `POST` request to `api/token` with a JSON payload containing your username and password
```curl
curl --location --request POST 'http://localhost:8000/api/token/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "your_username",
    "password": "your_password"
}'
 ```
This will return a JSON response containing the access and refresh tokens:
```json
{
    "access": "your_access_token",
    "refresh": "your_refresh_token"
}

```

To refresh an expired access token, send a `POST` request to `/api/token/refresh/` with a JSON payload containing your refresh token:

``` curl
curl --location --request POST 'http://localhost:8000/api/token/refresh/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "refresh": "your_refresh_token"
}'
```
This will return a new access token:

```json
{
    "access": "your_new_access_token"
}

```
To access the protected hello view, send a GET request to `/api/hello/` with an Authorization header containing your access token:
```curl 
curl --location --request GET 'http://localhost:8000/api/hello/' \
--header 'Authorization: Bearer your_access_token'
```
This will return a "Hello, World!" message if the access token is valid.

## User registration API:

- To register a new user, send a POST request to /api/register/ with a JSON payload containing the new user's username, email, and password:
```curl
curl --location --request POST 'http://localhost:8000/api/register/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "new_username",
    "email": "new_email@example.com",
    "password": "new_password"
}'
```

- This will create a new user with the specified username, email, and password, and return a JSON response with the user's ID and username:
```json
{
    "id": 2,
    "username": "new_username"
}

```


## Dockerize
This Dockerfile uses the official Python 3.8 image as the base, sets environment variables for MySQL connection parameters,
installs the MySQL client library as a system dependency, sets the working directory to `/code`, installs the project dependencies from `requirements.txt`, 
copies the project files to the container, exposes port `8000`, and runs the Django development server with the `CMD` instruction.
To use this Dockerfile with a MySQL database, you will need to define a service for the MySQL database in your docker-compose.yml file. You will also need to update the DATABASES settings in your Django settings file to use the MySQL database, like this:

```django
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': os.environ['MYSQL_HOST'],
        'PORT': os.environ['MYSQL_PORT'],
        'NAME': os.environ['MYSQL_DATABASE'],
        'USER': os.environ['MYSQL_USER'],
        'PASSWORD': os.environ['MYSQL_PASSWORD'],
    }
}

```




