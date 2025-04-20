
# 📝 Flask Blog — Portfolio Project

This is a **Flask-based Blog App**, inspired by Corey Schafer's Flask tutorial series. It demonstrates user authentication, CRUD operations, and the use of key Flask extensions such as Flask-Mail, Flask-Login, and SQLAlchemy.

This project serves as a personal portfolio piece with clean architecture and modular design.

---

## 🚀 Starting the Application

From the project root directory:

```bash
cd /Users/path/path/path/Flask_Blog
python run.py
```

Make sure your virtual environment is activated and all dependencies are installed.

---

## 🔐 Environment Variables

Create a `.env` file in the project root with the following keys:

```env
FLASK_APP_EMAIL_USER=your-email@mail.com
FLASK_APP_EMAIL_PASS=your-app-password
SECRET_KEY="key generated using secrets module (code below)"
SQLALCHEMY_DATABASE_URI="database url to be include here # example: sqlite:///site.db"
```

> 💡 **FLASK_APP_EMAIL_PASS** is an [App Password](https://support.google.com/accounts/answer/185833?hl=en) generated through your Google account for SMTP login. It is not your actual email password.


## 🔑 Generating a `SECRET_KEY` using Python

To securely generate a 16-character `SECRET_KEY`, use the `secrets` module in Python:

```python
import secrets
import string

def generate_secret_key(length=16):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(chars) for _ in range(length))

print(generate_secret_key())
```

> ⚠️ Make sure to save this key securely and do not expose it in public repositories.

---

## 📚 Useful References

This project integrates best practices and tools referenced from the following resources:

- [Install htop on macOS](https://www.cyberciti.biz/faq/install-htop-on-macos-unix-desktop-running-macbook-pro/)
- [Email verification with Flask-Mail](https://stackoverflow.com/questions/63581599/email-verification-with-flask-mail)
- [Decoding JWT payload in Python](https://stackoverflow.com/questions/59425161/getting-only-decoded-payload-from-jwt-in-python)
- [Flask API documentation](https://flask.palletsprojects.com/en/2.2.x/api/)
- [Timed JSON Web Signature serializer alternatives](https://stackoverflow.com/questions/71292764/which-timed-jsonwebsignature-serializer-replacement-for-itsdangerous-is-better)
- [Serialization and timed web tokens](https://stackoverflow.com/questions/60697422/serialisation-and-timed-web-tokens-in-python-flask)
- [Flask-Serialize Package](https://pypi.org/project/flask-serialize/)
- [Error Handling in Flask](https://flask.palletsprojects.com/en/2.2.x/errorhandling/)

### ✅ V.V. Important:
- [PyJWT — Encode/Decode with HS256](https://pyjwt.readthedocs.io/en/latest/usage.html#encoding-decoding-tokens-with-hs256)

### Helpful Packages:
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [python-utils](https://pypi.org/project/python-utils/#:~:text=%3A%3A%20BSD%20License-,Project%20description,I%20will%20keep%20extending%20it.)

---

## 🧠 Features Implemented

- User Registration & Authentication (Login/Logout)
- Profile Picture Upload
- Blog Post Creation, Editing, and Deletion
- Password Reset via Email (using Flask-Mail & App Password)
- Token-based Secure Links (JWT)
- SQLite database with SQLAlchemy ORM
- Session Management with Flask-Login

---

## 🛠️ Future Improvements

- Deploy to a cloud platform (Render, Vercel, Heroku)
- Add pagination and search
- Integrate Flask-RESTful or FastAPI for APIs
- Dockerize the app
