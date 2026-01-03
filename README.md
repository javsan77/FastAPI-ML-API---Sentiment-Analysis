# FastAPI ML API - Sentiment Analysis

<div align="center">

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/python-3.10+-blue.svg?style=for-the-badge&logo=python&logoColor=white)
![SQL Server](https://img.shields.io/badge/SQL%20Server-CC2927?style=for-the-badge&logo=microsoft-sql-server&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green.svg?style=for-the-badge)

**Professional REST API with Machine Learning Integration**

[Features](#-features) • [Quick Start](#-quick-start) • [API Docs](#-api-documentation) • [ML Model](#-machine-learning) • [Architecture](#-architecture)

</div>

---

## 🎯 Overview

A production-ready **FastAPI** boilerplate that combines robust user management with **Machine Learning** capabilities. Built with a clean architecture, JWT authentication, SQL Server persistence, and a trained sentiment analysis model.

Perfect foundation for building **AI-powered applications** that require user authentication, data persistence, and intelligent text analysis.

## ✨ Features

### 🔐 Security & Authentication
- **JWT Token-based authentication** with HTTPBearer
- **Password hashing** using bcrypt
- **Protected routes** with dependency injection
- Environment-based configuration

### 🗄️ Database
- **SQL Server integration** via SQLAlchemy + pyodbc
- **Stored procedures** for optimized queries
- **Connection pooling** for performance
- Clean repository pattern

### 🤖 Machine Learning
- **Sentiment Analysis** (Spanish language)
- **Naive Bayes + TF-IDF** classifier
- **Real-time predictions** via REST API
- **Batch processing** support
- **95%+ accuracy** on validation set

### 🏗️ Architecture
- **Layered architecture**: Clean separation of concerns
- **Dependency injection**: Flexible and testable
- **Pydantic schemas**: Type-safe data validation
- **Modular design**: Easy to extend and maintain

## 🚀 Quick Start

### Prerequisites

- **Python 3.10+**
- **SQL Server** (local or remote)
- **ODBC Driver 17/18 for SQL Server**

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/fastapi-ml-api.git
cd fastapi-ml-api
```

2. **Create virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Configure environment variables**

Create a `.env` file:

```env
DB_SERVER=localhost
DB_NAME=fastapi_user_api
DB_USER=your_username
DB_PASSWORD=your_password
DB_DRIVER=ODBC Driver 18 for SQL Server
```

5. **Initialize database**

Execute `scripts.sql` in your SQL Server instance to create tables and stored procedures.

6. **Train the ML model**

```bash
python train_model_final.py
```

7. **Run the application**

```bash
uvicorn app.main:app --reload
```

🎉 **API is live at:** `http://localhost:8000`

📚 **Interactive docs:** `http://localhost:8000/docs`

## 📂 Project Structure

```
fastapi-ml-api/
├── app/
│   ├── config/              # Database, Security, Environment configuration
│   │   ├── database.py
│   │   └── security.py
│   ├── core/                # Core utilities (bcrypt)
│   │   └── security.py
│   ├── dependencies/        # Dependency injection (Auth)
│   │   └── auth_dependency.py
│   ├── ml/                  # 🤖 Machine Learning Module
│   │   ├── models/
│   │   │   └── sentiment_model.py
│   │   └── services/
│   │       ├── text_preprocessor.py
│   │       └── sentiment_service.py
│   ├── repositories/        # Data access layer (Stored Procedures)
│   │   └── user_repository.py
│   ├── routers/             # API endpoints
│   │   ├── auth_router.py
│   │   ├── user_router.py
│   │   └── ml_router.py     # 🤖 ML endpoints
│   ├── schemas/             # Pydantic models
│   │   ├── auth_schema.py
│   │   ├── user_schema.py
│   │   └── ml/
│   │       └── sentiment_schema.py
│   ├── services/            # Business logic
│   │   ├── auth_service.py
│   │   └── user_service.py
│   └── main.py              # Application entry point
├── scripts.sql              # Database setup
├── train_model_final.py     # ML model training script
├── requirements.txt
└── .env                     # Environment variables (gitignored)
```

## 📖 API Documentation

### Authentication Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/auth/login` | Login and get JWT token | ❌ No |

### User Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/users/create` | Register new user | ❌ No |
| GET | `/users/` | List all users | ✅ Yes |
| GET | `/users/{id}` | Get user by ID | ❌ No |

### Machine Learning Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/ml/sentiment/analyze` | Analyze text sentiment | ✅ Yes |
| POST | `/ml/sentiment/batch` | Batch sentiment analysis | ✅ Yes |
| GET | `/ml/sentiment/health` | Check ML model status | ❌ No |

## 🤖 Machine Learning

### Sentiment Analysis Model

The API includes a trained sentiment analysis model for Spanish text that classifies input as:
- **POSITIVE** 😊
- **NEGATIVE** 😞
- **NEUTRAL** 😐

#### Model Specifications

- **Algorithm**: Multinomial Naive Bayes
- **Vectorization**: TF-IDF with n-grams (1-3)
- **Training samples**: 200+
- **Validation accuracy**: 95%+
- **Language**: Spanish

#### Example Usage

**Single text analysis:**

```bash
curl -X POST "http://localhost:8000/ml/sentiment/analyze" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Este producto es increíble, me encanta mucho"
  }'
```

**Response:**

```json
{
  "text": "Este producto es increíble, me encanta mucho",
  "sentiment": "POSITIVE",
  "confidence": 0.96,
  "scores": {
    "POSITIVE": 0.96,
    "NEGATIVE": 0.02,
    "NEUTRAL": 0.02
  },
  "analyzed_at": "2026-01-02T10:30:00"
}
```

**Batch analysis:**

```bash
curl -X POST "http://localhost:8000/ml/sentiment/batch" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "texts": [
      "Me encanta este servicio",
      "Pésima experiencia",
      "Está bien, nada especial"
    ]
  }'
```

### Retraining the Model

To retrain with your own data, edit `train_model_final.py` and run:

```bash
python train_model_final.py
```

The model will be saved to `app/ml/models/sentiment_classifier.pkl`

## 🔧 Configuration

### Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `DB_SERVER` | SQL Server address | `localhost` |
| `DB_NAME` | Database name | `fastapi_user_api` |
| `DB_USER` | Database user | `sa` |
| `DB_PASSWORD` | Database password | `YourPassword123!` |
| `DB_DRIVER` | ODBC driver name | `ODBC Driver 18 for SQL Server` |

### Security Settings

Located in `app/config/security.py`:

```python
SECRET_KEY = "CHANGE_THIS_IN_PRODUCTION"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60
```

⚠️ **Important**: Change `SECRET_KEY` before deploying to production!

## 🧪 Testing

Run the test suite:

```bash
pytest tests/ -v
```

Test ML model:

```bash
python -m pytest tests/test_ml.py
```

## 🚢 Deployment

### Docker (Recommended)

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Build and run:

```bash
docker build -t fastapi-ml-api .
docker run -p 8000:8000 --env-file .env fastapi-ml-api
```

### Production Checklist

- [ ] Change `SECRET_KEY` in `security.py`
- [ ] Set strong database password
- [ ] Configure CORS policies
- [ ] Enable HTTPS/SSL
- [ ] Set up logging and monitoring
- [ ] Configure rate limiting
- [ ] Backup database regularly
- [ ] Use production-grade WSGI server (Gunicorn/Uvicorn)

## 🎓 Use Cases

This boilerplate is ideal for:

- **Customer feedback analysis** systems
- **Social media sentiment** monitoring
- **Support ticket** classification
- **Product review** analysis
- **Chat applications** with sentiment detection
- **AI-powered chatbots** with user management
- **NLP research** projects with API interface

## 🛣️ Roadmap

- [ ] Add more ML models (NER, summarization)
- [ ] Implement model versioning
- [ ] Add metrics dashboard (Grafana)
- [ ] Vector database integration (Pinecone/Weaviate)
- [ ] LangChain integration for LLMs
- [ ] A/B testing framework for models
- [ ] Real-time monitoring and alerts
- [ ] Multi-language support

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Your Name**

- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)
- Portfolio: [yourwebsite.com](https://yourwebsite.com)

## 🙏 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) - Modern web framework
- [scikit-learn](https://scikit-learn.org/) - Machine learning library
- [SQLAlchemy](https://www.sqlalchemy.org/) - SQL toolkit
- [Pydantic](https://pydantic-docs.helpmanual.io/) - Data validation

## 📞 Support

If you have any questions or need help:

- Open an [issue](https://github.com/yourusername/fastapi-ml-api/issues)
- Email: your.email@example.com
- Twitter: [@yourhandle](https://twitter.com/yourhandle)

---

<div align="center">

**⭐ If you find this project useful, please consider giving it a star! ⭐**

Made with ❤️ and ☕ by [Your Name]

</div>
