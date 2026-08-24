# Alumni Intelligence & Prospect Research Platform

A production-style **FastAPI-based Alumni Intelligence and Prospect Research Platform** for managing alumni records, authentication, analytics, data import/export, company and city insights, and AI-assisted prospect research.

This project demonstrates a modular backend architecture using **Python, FastAPI, SQLAlchemy, SQLite, JWT authentication, Pydantic, Pandas, OpenPyXL, web scraping, automated testing, and optional LLM integration**.

---

## 📌 Project Overview

The Alumni Intelligence & Prospect Research Platform provides a centralized API for collecting, managing, searching, analyzing, importing, exporting, and researching alumni information.

The platform includes:

- Alumni record management
- User registration and authentication
- JWT-based authentication
- Password hashing
- Alumni search and filtering
- Pagination and sorting
- Alumni analytics
- Company statistics
- City statistics
- CSV import
- CSV export
- Excel export
- Web scraping
- Data extraction and parsing
- AI-assisted prospect research
- Health monitoring
- Request logging
- Exception handling
- Automated testing

The application is structured using separate routers, services, models, security components, scraping modules, and utilities to demonstrate a maintainable backend architecture.

---

## 🚀 Features

### 🔐 Authentication & Security

- User registration
- User login
- Password hashing
- JWT access-token authentication
- Current authenticated user
- Token verification
- Protected endpoints
- Configurable token expiration
- Environment-based configuration

### 👥 Alumni Management

The platform provides complete CRUD functionality for alumni records.

**Operations**

- Create alumni
- Retrieve all alumni
- Retrieve alumni by ID
- Update alumni
- Delete alumni
- Search alumni
- Pagination
- Sorting

**Search Filters**

Alumni can be searched by:

- Name
- Company
- City
- Designation

### 📊 Analytics

The application provides statistics for understanding the alumni database.

**Available Analytics**

- Total alumni
- Total companies
- Total cities
- Company-level statistics
- City-level statistics

These endpoints demonstrate how operational data can be transformed into useful business insights.

### 📁 Data Import & Export

- **CSV Import** — Upload alumni records from a CSV file and process them through the application.
- **CSV Export** — Export alumni records into a CSV file.
- **Excel Export** — Export alumni records into an Excel workbook using OpenPyXL.

### 🤖 AI-Assisted Prospect Research

The platform includes an AI-assisted research workflow for generating additional information about alumni prospects.

The research workflow is designed around:

1. Alumni information
2. Research request
3. Data collection
4. Data extraction
5. Data parsing
6. Prompt generation
7. Optional LLM processing
8. Research profile generation

The LLM service is separated from the rest of the application so that AI functionality can be configured independently.

### 🌐 Web Scraping & Data Extraction

The project contains a modular scraping and extraction pipeline.

Components include:

- Base scraper
- Wikipedia scraper
- HTML extraction
- Data parsing
- Data validation
- Retry handling

The scraping components are separated from the API and service layers to make the system easier to extend.

---

## 🛠️ Tech Stack

**Backend**
Python · FastAPI · Uvicorn · SQLAlchemy · SQLite · Pydantic

**Authentication & Security**
JWT · Python-JOSE · Passlib · Bcrypt · Cryptography

**Data Processing**
Pandas · NumPy · OpenPyXL

**Web Scraping**
Requests · BeautifulSoup · lxml

**AI / LLM**
OpenAI-compatible architecture · OpenRouter-compatible configuration · Configurable LLM service · Prompt-based research workflow

**Testing**
Pytest

**Development**
Git · GitHub · Visual Studio Code · Python virtual environment

---

## 🏗️ Project Structure

```text
alumni-prospect-research/
│
├── app/
│   ├── auth/
│   │   ├── dependencies.py
│   │   └── security.py
│   │
│   ├── config/
│   │   ├── __init__.py
│   │   └── settings.py
│   │
│   ├── database/
│   │   ├── __init__.py
│   │   ├── database.py
│   │   └── init_db.py
│   │
│   ├── exceptions/
│   │   └── __init__.py
│   │
│   ├── imports/
│   │   └── csv_import.py
│   │
│   ├── middleware/
│   │   ├── __init__.py
│   │   ├── exception_handler.py
│   │   └── request_logging.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── alumni.py
│   │   ├── auth_schemas.py
│   │   ├── response_models.py
│   │   ├── schemas.py
│   │   └── user.py
│   │
│   ├── prompts/
│   │   └── prospect_prompt.txt
│   │
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── alumni.py
│   │   ├── auth.py
│   │   ├── health.py
│   │   └── research.py
│   │
│   ├── scraper/
│   │   ├── __init__.py
│   │   ├── base_scraper.py
│   │   ├── extractor.py
│   │   ├── parser.py
│   │   └── wiki_scraper.py
│   │
│   ├── security/
│   │   ├── jwt_handler.py
│   │   └── password.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── company_service.py
│   │   ├── database_service.py
│   │   ├── etl_service.py
│   │   ├── export_service.py
│   │   ├── llm_service.py
│   │   ├── prompt_service.py
│   │   ├── research_service.py
│   │   └── user_service.py
│   │
│   └── utils/
│       ├── __init__.py
│       ├── constants.py
│       ├── helpers.py
│       ├── logger.py
│       ├── retry.py
│       └── validators.py
│
├── data/
│   └── alumni.csv
│
├── screenshots/
│   ├── 01_swagger_home.png
│   ├── 02_project_structure.png
│   ├── 03_root_endpoint.png
│   ├── 04_login.png
│   ├── 05_current_user.png
│   ├── 06_register.png
│   ├── 07_verify_token.png
│   ├── 08_create_alumni.png
│   ├── 09_get_all_alumni.png
│   ├── 10_search_alumni.png
│   ├── 11_get_alumni_by_id.png
│   ├── 12_update_alumni.png
│   ├── 13_delete_alumni.png
│   ├── 14_statistics.png
│   ├── 15_city_statistics.png
│   ├── 16_company_statistics.png
│   ├── 17_export_csv.png
│   ├── 18_export_excel.png
│   ├── 19_import_csv.png
│   ├── 20_ai_research_profile.png
│   └── 21_health_check.png
│
├── tests/
│   ├── test_ai_pipeline.py
│   ├── test_database.py
│   ├── test_etl.py
│   ├── test_export.py
│   ├── test_extractor.py
│   ├── test_llm.py
│   ├── test_parser.py
│   ├── test_prompt.py
│   ├── test_research.py
│   ├── test_scraper.py
│   └── test_wiki_scraper.py
│
├── .env.example
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
└── run.py
```

---

## ⚙️ Installation

### 1. Clone the Portfolio Repository

```bash
git clone https://github.com/AshimaSharma-DataAnalyst/data-analyst-portfolio.git
cd data-analyst-portfolio/alumni-prospect-research
```

### 2. Create a Virtual Environment

**Windows**

```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks script execution:

```bash
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Configuration

Create a `.env` file in the project root.

Example:

```env
PROJECT_NAME=Alumni Intelligence & Prospect Research Platform

DATABASE_URL=sqlite:///./alumni.db

JWT_SECRET=replace-with-a-secure-secret
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60

LLM_PROVIDER=openrouter
LLM_MODEL=deepseek/deepseek-chat-v3-0324:free
```

If an LLM API key is required for a specific deployment, configure it through the environment.

> ⚠️ **Never commit `.env` files, API keys, passwords, or other secrets to GitHub.**
> The repository includes `.env.example` as a safe configuration template.

---

## ▶️ Running the Application

From the project directory:

```bash
python run.py
```

The application runs locally at:

```
http://127.0.0.1:8000
```

---

## 📚 API Documentation

FastAPI automatically provides interactive API documentation.

| Docs Type | URL |
|---|---|
| Swagger UI | http://127.0.0.1:8000/docs |
| ReDoc | http://127.0.0.1:8000/redoc |

Swagger UI allows users to interact with the API directly, including authentication, alumni management, analytics, import/export operations, research, and health checks.

---

## 🔌 API Endpoints

**Root**

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Application information |

**Authentication**

| Method | Endpoint | Description |
|---|---|---|
| POST | `/auth/register` | Register a new user |
| POST | `/auth/login` | Authenticate a user |
| GET | `/auth/me` | Retrieve the current authenticated user |
| POST | `/auth/verify-token` | Verify an authentication token |

**Alumni**

| Method | Endpoint | Description |
|---|---|---|
| POST | `/alumni/` | Create an alumni record |
| GET | `/alumni/` | Retrieve alumni records |
| GET | `/alumni/search` | Search alumni |
| GET | `/alumni/{alumni_id}` | Retrieve an alumni record by ID |
| PUT | `/alumni/{alumni_id}` | Update an alumni record |
| DELETE | `/alumni/{alumni_id}` | Delete an alumni record |

**Pagination & Sorting**

The alumni listing endpoint supports:

- Page number
- Page size
- Sort column
- Sort order

Example:

```
/alumni/?page=1&size=10&sort_by=id&order=asc
```

**Analytics**

| Method | Endpoint | Description |
|---|---|---|
| GET | `/alumni/stats` | General alumni statistics |
| GET | `/alumni/stats/companies` | Company statistics |
| GET | `/alumni/stats/cities` | City statistics |

**Data Import & Export**

| Method | Endpoint | Description |
|---|---|---|
| GET | `/alumni/export/csv` | Export alumni records to CSV |
| GET | `/alumni/export/excel` | Export alumni records to Excel |
| POST | `/alumni/import/csv` | Import alumni records from CSV |

**Research**

The application includes a dedicated research router for AI-assisted prospect research. The exact research endpoint and request schema can be explored through the Swagger documentation at `/docs`.

**Health**

| Method | Endpoint | Description |
|---|---|---|
| GET | `/health` | Application health check |

---

## 🧪 Testing

The project includes automated tests for major components of the application.

Test coverage includes:

- Database operations
- ETL processing
- Data export
- Data extraction
- Parsing
- Prompt generation
- Research workflow
- Web scraping
- Wikipedia scraping
- LLM service
- AI pipeline

Run the complete test suite:

```bash
pytest
```

For detailed output:

```bash
pytest -v
```

---

## 📸 Screenshots

The following screenshots demonstrate the application's functionality through the FastAPI Swagger interface.

**API Documentation**

| | | |
|---|---|---|
| ![Swagger Home](screenshots/01_swagger_home.png) | ![Project Structure](screenshots/02_project_structure.png) | ![Root Endpoint](screenshots/03_root_endpoint.png) |
| 01 — Swagger Home | 02 — Project Structure | 03 — Root Endpoint |

**🔐 Authentication**

| | | |
|---|---|---|
| ![Login](screenshots/04_login.png) | ![Current User](screenshots/05_current_user.png) | ![Register](screenshots/06_register.png) |
| 04 — Login | 05 — Current User | 06 — Register |

| |
|---|
| ![Verify Token](screenshots/07_verify_token.png) |
| 07 — Verify Token |

**👥 Alumni Management**

| | | |
|---|---|---|
| ![Create Alumni](screenshots/08_create_alumni.png) | ![Get All Alumni](screenshots/09_get_all_alumni.png) | ![Search Alumni](screenshots/10_search_alumni.png) |
| 08 — Create Alumni | 09 — Get All Alumni | 10 — Search Alumni |

| | | |
|---|---|---|
| ![Get Alumni by ID](screenshots/11_get_alumni_by_id.png) | ![Update Alumni](screenshots/12_update_alumni.png) | ![Delete Alumni](screenshots/13_delete_alumni.png) |
| 11 — Get Alumni by ID | 12 — Update Alumni | 13 — Delete Alumni |

**📊 Analytics**

| | | |
|---|---|---|
| ![General Statistics](screenshots/14_statistics.png) | ![City Statistics](screenshots/15_city_statistics.png) | ![Company Statistics](screenshots/16_company_statistics.png) |
| 14 — General Statistics | 15 — City Statistics | 16 — Company Statistics |

**📁 Data Import & Export**

| | | |
|---|---|---|
| ![CSV Export](screenshots/17_export_csv.png) | ![Excel Export](screenshots/18_export_excel.png) | ![CSV Import](screenshots/19_import_csv.png) |
| 17 — CSV Export | 18 — Excel Export | 19 — CSV Import |

**🤖 AI-Assisted Research**

| |
|---|
| ![AI Research Profile](screenshots/20_ai_research_profile.png) |
| 20 — AI Research Profile |

**❤️ Health Monitoring**

| |
|---|
| ![Health Check](screenshots/21_health_check.png) |
| 21 — Health Check |

---

## 🔄 Application Workflow

```text
                         ┌──────────────────┐
                         │      User        │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │    FastAPI       │
                         │      API         │
                         └────────┬─────────┘
                                  │
              ┌───────────────────┼───────────────────┐
              │                   │                   │
              ▼                   ▼                   ▼
       ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
       │    Auth     │     │   Alumni    │     │  Analytics  │
       │    + JWT    │     │ Management  │     │             │
       └─────────────┘     └──────┬──────┘     └─────────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │    SQLAlchemy    │
                         │      SQLite      │
                         └──────────────────┘

              ┌───────────────────┼───────────────────┐
              │                   │                   │
              ▼                   ▼                   ▼
       ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
       │ Import /    │     │  Research   │     │   Health    │
       │   Export    │     │  Pipeline   │     │   Monitor   │
       └─────────────┘     └──────┬──────┘     └─────────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │ Scraping /       │
                         │ Extraction /     │
                         │ Parsing / LLM    │
                         └──────────────────┘
```

---

## 🧩 Architecture & Design Principles

- **Separation of Concerns** — API routes, business logic, database operations, authentication, scraping, AI services, and utilities are separated into dedicated modules.
- **Service Layer** — Business logic is handled through service modules rather than placing all application logic directly inside API routes.
- **Configuration Management** — Application configuration is managed through environment variables.
- **Security** — Authentication, JWT handling, and password management are separated into dedicated security components.
- **Data Validation** — Pydantic models and validation utilities are used to validate application data.
- **Error Handling** — Middleware provides centralized exception handling.
- **Logging** — Application requests and errors can be recorded using the project's logging utilities.
- **Testability** — Major application components are separated into testable modules and covered by automated tests.

---

## 🔮 Future Improvements

- PostgreSQL production database support
- Redis caching
- Background task processing
- Celery-based asynchronous processing
- Role-based access control
- More advanced AI research workflows
- Multiple LLM provider support
- Automated company enrichment
- Advanced alumni matching
- Interactive analytics dashboard
- React frontend
- Docker containerization
- GitHub Actions CI/CD
- Cloud deployment
- API rate limiting
- Improved monitoring and observability
- Expanded automated test coverage

---

## 📈 Skills Demonstrated

Python · FastAPI · REST API development · SQLAlchemy · SQLite · Database design · JWT authentication · Password security · Pydantic · Pandas · NumPy · Excel automation · CSV processing · ETL pipelines · Web scraping · Data extraction · Data parsing · API architecture · Service-layer architecture · AI/LLM integration · Prompt engineering · Error handling · Logging · Automated testing · Git · GitHub

---

## 🎯 Portfolio Value

This project demonstrates the combination of:

**Data Analytics + Python + SQL + ETL + Automation + API Development + AI**

It showcases how a data-focused application can collect, validate, transform, analyze, export, and enrich information through a modular API-driven backend.

The project also demonstrates practical software engineering practices such as authentication, environment-based configuration, service separation, logging, testing, and documentation.

---

## 👩‍💻 Author

**Ashima Sharma**

Data Analyst | Python | SQL | Power BI | Tableau | Excel | Data Analytics

- GitHub: [https://github.com/AshimaSharma-DataAnalyst](https://github.com/AshimaSharma-DataAnalyst)
- Portfolio: [https://github.com/AshimaSharma-DataAnalyst/data-analyst-portfolio](https://github.com/AshimaSharma-DataAnalyst/data-analyst-portfolio)

---

## 📄 License

This project is available under the license included in the repository.

---

⭐ If you find this project useful, feel free to explore the repository and other projects in my data analytics portfolio.
