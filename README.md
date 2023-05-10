# ProfileGen

ProfileGen is a Django-based web application that generates random user profiles. It is built using Django 3.2 and Python 3.9.

## Features

- Generate random user profiles with basic information such as name, email, phone number, and address.
- Users can download generated profiles in CSV and JSON formats.
- The application has an admin interface where admins can manage users and view their generated profiles.

## Installation

To run the application locally, you can follow these steps:

1. Clone the repository to your local machine:

```
git clone https://github.com/keshav1sharma/ProfileGen.git
```

2. Navigate to the project directory:

```
cd ProfileGen
```

3. Create a virtual environment:

```
python -m venv env
```

4. Activate the virtual environment:

On Windows:
```
env\Scripts\activate
```

On macOS and Linux:
```
source env/bin/activate
```

5. Install the project dependencies:

```
pip install -r requirements.txt
```

6. Apply the database migrations:

```
python manage.py migrate
```

7. Run the development server:

```
python manage.py runserver
```

The application should now be running on `http://localhost:8000`.

## Usage

To generate a user profile, navigate to the homepage (`/`) and click on the "Generate Profile" button. You can download the generated profile in CSV or JSON format by clicking on the corresponding download button.

To view the admin interface, navigate to `/admin`. You can login using the credentials `admin` (username) and `admin123` (password) that are set by default. From the admin interface, you can manage users and view their generated profiles.

## License

ProfileGen is licensed under the [MIT License](https://github.com/keshav1sharma/ProfileGen/blob/main/LICENSE). Feel free to use it for your own projects or modify it to suit your needs.
