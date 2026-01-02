# FastAPI Base API (SQL Server + JWT Auth)

This repository provides a professional boilerplate for developing APIs with **FastAPI**. It is designed to be modular, scalable, and easily replicable for **Artificial Intelligence** projects that require robust user management, **SQL Server** persistence, and **JWT-based** security.

## 🚀 Key Features

* 
**Layered Architecture**: Clear separation of concerns including Routers, Services, Repositories, and Schemas.


* 
**JWT Authentication**: Implements a complete login flow and route protection using `HTTPBearer`.


* 
**SQL Server Integration**: Utilizes `SQLAlchemy` with `pyodbc` to interact efficiently with stored procedures.


* 
**Data Validation**: Powered by `Pydantic` for strict input and output data schemas.


* 
**Enhanced Security**: Industry-standard password hashing using `bcrypt`.



## 📂 Project Structure

```text
├── app/
│   ├── config/          # Database, Security, and Environment configuration [cite: 1, 2]
│   ├── core/            # Security utility functions (bcrypt) [cite: 4]
│   ├── dependencies/    # Dependency injection (Authentication) [cite: 5]
│   ├── repositories/    # Direct database access (Stored Procedures) [cite: 8, 10, 11]
│   ├── routers/         # API Endpoints and route definitions [cite: 7, 12]
│   ├── schemas/         # Pydantic data models [cite: 13]
│   ├── services/        # Business logic layer [cite: 15]
│   └── main.py          # Application entry point [cite: 7]
├── scripts.sql          # Database schema and stored procedure scripts [cite: 19, 21, 23, 25]
└── .env                 # Environment variables (Do not commit to Git) [cite: 1]

```

## 🛠️ Prerequisites

1. **Python 3.10+**
2. 
**SQL Server** instance.


3. **ODBC Driver for SQL Server**.

## ⚙️ Initial Setup

1. **Clone the repository:**
```bash
git clone https://github.com/javsan77/FastAPI-Backend-Base
cd FastAPI-Backend-Base

```


2. **Create a virtual environment and install dependencies:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install fastapi uvicorn sqlalchemy pyodbc python-dotenv python-jose[cryptography] passlib[bcrypt]

```


3. **Configure environment variables:**
Create a `.env` file in the root directory with the following credentials:


```env
DB_SERVER=your_server_address
DB_NAME=fastapi_user_api
DB_USER=your_username
DB_PASSWORD=your_password
DB_DRIVER=ODBC Driver 17 for SQL Server

```


4. **Initialize the Database:**
Execute the contents of `scripts.sql` in your SQL Server instance to generate the `Users` table and required stored procedures.



## 🚦 Running the Application

To start the development server:

```bash
uvicorn app.main:app --reload

```

The API will be available at `http://127.0.0.1:8000`. Access the interactive API documentation at `/docs`.

## 🔒 Primary Endpoints

| Method | Path 		 	| Description 								| Protected 	|
| `POST` | `/auth/login` 	| Authenticate and receive JWT access token | No 			|
| `POST` | `/users/create` 	| Register a new user 						| No 			|
| `GET`	 | `/users/` 		| List all registered users 			    | <br>**Yes** 	|
| `GET` | `/users/{id}` | Retrieve specific user details 				| No			|

## 🧠 AI Project Integration Notes

This boilerplate is ideal for AI-driven applications because:

* 
**User Persistence**: Easily store chat histories, prompt logs, or agent configurations.


* 
**Scalability**: The repository pattern allows for seamless integration of Vector Databases (like Pinecone or Milvus) alongside SQL.


* 
**Security**: Protects expensive model inference and sensitive data through robust authentication.

