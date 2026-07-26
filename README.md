# FastAPI Blog Application

A RESTful blog application built with **FastAPI** that provides secure user authentication, authorization, and CRUD operations for blog posts. The project demonstrates modern backend development practices using JWT authentication, SQLAlchemy ORM, PostgreSQL, and Pydantic validation.

## Features

- User registration and login
- JWT-based authentication
- Secure password hashing with bcrypt
- Role-based authorization for blog ownership
- CRUD operations for blog posts
- PostgreSQL database integration
- SQLAlchemy ORM for database operations
- Request and response validation using Pydantic
- Interactive API documentation with Swagger UI
- RESTful API design following best practices

---

## Tech Stack

| Category | Technology |
|----------|------------|
| Backend | FastAPI |
| Language | Python |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Authentication | JWT (JSON Web Tokens) |
| Password Hashing | Passlib (bcrypt) |
| Validation | Pydantic |
| API Testing | Postman / Swagger UI |
| ASGI Server | Uvicorn |

---

## Project Structure

```text
.
├── app/
│   ├── database.py          # Database connection
│   ├── models.py            # SQLAlchemy models
│   ├── schemas.py           # Pydantic schemas
│   ├── oauth2.py            # JWT authentication
│   ├── utils.py             # Password hashing utilities
│   ├── routers/
│   │   ├── user.py
│   │   ├── authentication.py
│   │   └── post.py
│   └── main.py              # FastAPI application
├── requirements.txt
└── README.md
```

---

## API Features

### Authentication

- User Registration
- User Login
- JWT Token Generation
- Protected Routes

### Blog Posts

- Create Post
- Read Posts
- Read Single Post
- Update Post
- Delete Post

### Users

- Register User
- Retrieve User Information

---

## Installation

### Clone the repository

```bash
git clone https://github.com/<your-username>/<repository-name>.git
cd <repository-name>
```

### Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
DATABASE_HOST=localhost
DATABASE_PORT=5432
DATABASE_NAME=blog_db
DATABASE_USER=postgres
DATABASE_PASSWORD=your_password

SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

---

## Run the Application

```bash
uvicorn app.main:app --reload
```

Server runs on

```
http://127.0.0.1:8000
```

---

## API Documentation

FastAPI automatically generates API documentation.

### Swagger UI

```
http://127.0.0.1:8000/docs
```

### ReDoc

```
http://127.0.0.1:8000/redoc
```

---

## Example API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/login` | Authenticate user |
| POST | `/users` | Register new user |
| GET | `/posts` | Retrieve all posts |
| GET | `/posts/{id}` | Retrieve a specific post |
| POST | `/posts` | Create a new post |
| PUT | `/posts/{id}` | Update a post |
| DELETE | `/posts/{id}` | Delete a post |

---

## Learning Outcomes

- Developed RESTful APIs using FastAPI.
- Implemented JWT-based authentication and authorization.
- Designed relational database models using SQLAlchemy.
- Validated API requests and responses with Pydantic.
- Integrated PostgreSQL for persistent data storage.
- Built and tested APIs using Swagger UI and Postman.

---

## Future Improvements

- Docker support
- Refresh token authentication
- Role-based access control
- Pagination and filtering
- Search functionality
- Image upload support
- CI/CD pipeline
- Unit and integration testing

---

## License

This project is developed for learning backend development with FastAPI and PostgreSQL.
