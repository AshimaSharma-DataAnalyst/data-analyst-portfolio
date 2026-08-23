# Alumni Intelligence & Prospect Research Platform

A production-style **FastAPI-based Alumni Intelligence and Prospect Research Platform** for managing alumni records, authentication, analytics, data import/export, company and city insights, and AI-assisted prospect research.

The project demonstrates a modular backend architecture using **FastAPI, SQLAlchemy, SQLite, JWT authentication, Pydantic, Pandas, OpenPyXL, and optional LLM integration through OpenRouter**.

---

## 📌 Project Overview

The Alumni Intelligence & Prospect Research Platform provides a centralized API for:

* Managing alumni records
* User registration and authentication
* JWT-based authorization
* Searching and filtering alumni
* Pagination and sorting
* Company and city analytics
* CSV and Excel export
* CSV data import
* AI-assisted alumni/prospect research
* Application health monitoring
* Structured API documentation through Swagger UI

The application is designed with a modular service-based architecture so that database operations, authentication, AI interactions, prompts, and business logic remain separated from the API routing layer.

---

## ✨ Key Features

### 👤 Alumni Management

* Create alumni records
* Retrieve all alumni
* Retrieve an individual alumnus by ID
* Update alumni information
* Delete alumni records
* Search alumni by:

  * Name
  * Company
  * City
  * Designation
* Pagination
* Sorting by database columns
* Ascending/descending ordering

### 🔐 Authentication & Security

* User registration
* User login
* JWT access tokens
* Current-user authentication
* Token verification
* Protected endpoints
* Active-user validation
* Configurable JWT expiration

### 📊 Analytics

The platform provides:

* Overall alumni statistics
* Company-wise statistics
* City-wise statistics

Example:

```json
{
  "total_alumni": 5,
  "total_companies": 4,
  "total_cities": 5
}
```

The values depend on the records currently stored in the database.

### 📁 Data Import & Export

Supported operations include:

* Export alumni data to CSV
* Export alumni data to Excel
* Import alumni records from CSV

Generated files can be stored in the project's `exports/` directory.

### 🤖 AI Prospect Research

The `/research/profile` endpoint generates a research profile from information such as:

* Name
* Company
* Designation
* Education
* City

The system can enrich the profile with built-in company information such as:

* Industry
* Company type
* Headquarters
* Founded year
* Employee count
* Website

The AI layer is designed to use configurable LLM providers/models and can operate in fallback mode when an external API key is not configured.

### 🏥 Health Monitoring

The application provides a health endpoint for checking whether the API is running correctly.

---

# 🛠️ Tech Stack

| Technology          | Purpose                          |
| ------------------- | -------------------------------- |
| **Python**          | Backend programming language     |
| **FastAPI**         | REST API framework               |
| **Uvicorn**         | ASGI server                      |
| **SQLAlchemy**      | ORM/database interaction         |
| **SQLite**          | Local relational database        |
| **Pydantic**        | Data validation and schemas      |
| **JWT**             | Authentication and authorization |
| **python-jose**     | JWT implementation               |
| **bcrypt**          | Password hashing                 |
| **Pandas**          | Data processing                  |
| **OpenPyXL**        | Excel import/export              |
| **BeautifulSoup4**  | Web scraping/data extraction     |
| **OpenAI SDK**      | LLM client interface             |
| **OpenRouter**      | Optional LLM provider            |
| **python-dotenv**   | Environment configuration        |
| **Pytest**          | Testing                          |
| **Swagger/OpenAPI** | Interactive API documentation    |

---

# 🏗️ Project Architecture

The application follows a modular backend architecture.

```text
alumni-prospect-research/
│
├── app/
│   ├── auth/
│   ├── config/
│   ├── database/
│   ├── exceptions/
│   ├── imports/
│   ├── middleware/
│   ├── models/
│   ├── prompts/
│   ├── routers/
│   ├── scraper/
│   ├── security/
│   ├── services/
│   ├── utils/
│   │
│   ├── __init__.py
│   └── main.py
│
├── data/
├── exports/
├── logs/
├── screenshots/
├── tests/
├── uploads/
│
├── .env.example
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
└── run.py
```

---

# 📂 Important Components

### `app/routers/`

Contains FastAPI route definitions and API endpoints.

Examples:

```text
alumni.py
auth.py
research.py
health.py
```

### `app/services/`

Contains business logic separated from the API routes.

Examples include:

```text
database_service.py
company_service.py
llm_service.py
prompt_service.py
research_service.py
```

### `app/models/`

Contains database models and Pydantic request/response schemas.

### `app/security/`

Contains authentication and JWT-related functionality.

### `app/prompts/`

Contains reusable prompt templates used by the AI research service.

### `app/config/`

Centralizes application configuration and environment variables.

### `exports/`

Stores generated CSV and Excel files.

### `uploads/`

Stores uploaded files used by import operations.

### `logs/`

Stores application and error logs.

### `tests/`

Contains automated tests for application functionality.

---

# 🚀 Installation

## 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/alumni-prospect-research.git
```

Navigate into the project:

```bash
cd alumni-prospect-research
```

---

## 2. Create a virtual environment

### Windows PowerShell

```powershell
python -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks script execution for the current session:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

Then:

```powershell
.\.venv\Scripts\Activate.ps1
```

### macOS/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

# ⚙️ Environment Configuration

Create a `.env` file in the project root.

Example:

```env
PROJECT_NAME=Alumni Intelligence & Prospect Research Platform

DATABASE_URL=sqlite:///./alumni.db

JWT_SECRET=CHANGE_THIS_TO_A_LONG_RANDOM_SECRET

JWT_ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=60

OPENROUTER_API_KEY=

LLM_PROVIDER=openrouter

LLM_MODEL=deepseek/deepseek-chat-v3-0324:free

SECRET_KEY=CHANGE_THIS_SECRET
```

### Important

Do **not** commit your actual `.env` file or API keys to GitHub.

The project includes `.env.example` as a safe configuration template.

The `.gitignore` file excludes:

```text
.env
.venv/
alumni.db
logs/*.log
uploads/*
exports/*
```

---

# 🤖 Optional AI Configuration

The AI research feature can be configured with an OpenRouter API key.

For example:

```env
OPENROUTER_API_KEY=your_api_key_here
```

The application uses the OpenAI Python SDK with the OpenRouter API endpoint.

If an API key is not configured, the application can use its built-in fallback research mode rather than preventing the rest of the application from running.

This allows the core API functionality to be demonstrated without requiring an external paid AI service.

---

# ▶️ Running the Application

Start the FastAPI application with:

```bash
python run.py
```

The API will be available at:

```text
http://127.0.0.1:8000
```

---

# 📚 API Documentation

FastAPI automatically provides interactive Swagger documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

Swagger allows you to:

* View available endpoints
* Inspect request schemas
* Enter parameters
* Authenticate with JWT
* Execute API requests
* View response bodies
* Test API functionality interactively

---

# 🔌 API Endpoints

## System

| Method | Endpoint  | Description             |
| ------ | --------- | ----------------------- |
| `GET`  | `/`       | Application information |
| `GET`  | `/health` | Health/status check     |

---

## Authentication

| Method | Endpoint             | Description                    |
| ------ | -------------------- | ------------------------------ |
| `POST` | `/auth/register`     | Register a new user            |
| `POST` | `/auth/login`        | Authenticate user              |
| `GET`  | `/auth/current-user` | Get current authenticated user |
| `POST` | `/auth/verify-token` | Verify JWT token               |

> Exact authentication route prefixes may be viewed in the generated Swagger documentation.

---

# 👥 Alumni API

## Create Alumni

```http
POST /alumni/
```

Creates a new alumni record.

Example request:

```json
{
  "name": "Alex Johnson",
  "company": "Microsoft",
  "designation": "Data Analyst",
  "education": "M.S. Computer Science",
  "city": "Seattle"
}
```

---

## Get All Alumni

```http
GET /alumni/
```

Supports:

* Pagination
* Sorting
* Ascending/descending order

Example:

```text
/alumni/?page=1&size=10&sort_by=id&order=asc
```

---

## Search Alumni

```http
GET /alumni/search
```

Supported filters:

```text
name
company
city
designation
page
size
```

Example:

```text
/alumni/search?company=Microsoft
```

---

## Get Alumni by ID

```http
GET /alumni/{alumni_id}
```

Returns a specific alumni record.

Example:

```text
/alumni/1
```

---

## Update Alumni

```http
PUT /alumni/{alumni_id}
```

Updates an existing alumni record.

---

## Delete Alumni

```http
DELETE /alumni/{alumni_id}
```

Deletes an alumni record.

---

# 📊 Statistics API

## Overall Statistics

```http
GET /alumni/stats
```

Example response:

```json
{
  "total_alumni": 5,
  "total_companies": 4,
  "total_cities": 5
}
```

---

## Company Statistics

```http
GET /alumni/stats/companies
```

Returns alumni distribution by company.

---

## City Statistics

```http
GET /alumni/stats/cities
```

Returns alumni distribution by city.

---

# 📤 Export API

## Export CSV

```http
GET /alumni/export/csv
```

Downloads:

```text
alumni.csv
```

---

## Export Excel

```http
GET /alumni/export/excel
```

Downloads:

```text
alumni.xlsx
```

---

# 📥 Import API

## Import CSV

```http
POST /alumni/import/csv
```

Accepts an uploaded CSV file and imports alumni records into the database.

---

# 🤖 AI Research API

## Generate Research Profile

```http
POST /research/profile
```

Example request:

```json
{
  "name": "Alex Johnson",
  "company": "Microsoft",
  "designation": "Data Analyst",
  "education": "M.S. Computer Science",
  "city": "Seattle"
}
```

Example response structure:

```json
{
  "name": "Alex Johnson",
  "company": "Microsoft",
  "designation": "Data Analyst",
  "education": "M.S. Computer Science",
  "city": "Seattle",
  "industry": "Technology",
  "company_type": "Public",
  "headquarters": "Redmond, Washington, USA",
  "website": "https://www.microsoft.com",
  "summary": "..."
}
```

The research service combines structured company information with the configured AI/fallback research mechanism.

---

# 🔄 Application Flow

```text
                    ┌─────────────────────┐
                    │      Client         │
                    │ Swagger / Frontend  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │     FastAPI         │
                    │      Routers        │
                    └──────────┬──────────┘
                               │
              ┌────────────────┼────────────────┐
              ▼                ▼                ▼
       ┌─────────────┐  ┌─────────────┐  ┌─────────────┐
       │   Security  │  │  Services   │  │ Middleware  │
       │ JWT/Auth    │  │ Business    │  │ Logging     │
       └─────────────┘  │ Logic       │  └─────────────┘
                        └──────┬──────┘
                               │
                    ┌──────────┴──────────┐
                    ▼                     ▼
             ┌─────────────┐       ┌─────────────┐
             │  SQLite +   │       │ AI Research │
             │ SQLAlchemy  │       │ / Fallback  │
             └─────────────┘       └─────────────┘
```

---

# 🧪 Testing

The project includes a `tests/` directory for automated testing.

Run tests using:

```bash
pytest
```

For more detailed output:

```bash
pytest -v
```

---

# 📸 Screenshots

The project includes screenshots demonstrating the major application features.

Screenshots are stored in:

```text
screenshots/
```

## Swagger & Project

### Swagger API Home

![Swagger Home](screenshots/01_swagger_home.png)

### Project Structure

![Project Structure](screenshots/02_project_structure.png)

### Root Endpoint

![Root Endpoint](screenshots/03_root_endpoint.png)

---

## Authentication

### User Registration

![Register](screenshots/04_register.png)

### User Login

![Login](screenshots/05_login.png)

### Current User

![Current User](screenshots/06_current_user.png)

### Verify Token

![Verify Token](screenshots/07_verify_token.png)

---

## Alumni Management

### Create Alumni

![Create Alumni](screenshots/08_create_alumni.png)

### Get All Alumni

![Get All Alumni](screenshots/09_get_all_alumni.png)

### Search Alumni

![Search Alumni](screenshots/10_search_alumni.png)

### Get Alumni by ID

![Get Alumni by ID](screenshots/11_get_alumni_by_id.png)

### Update Alumni

![Update Alumni](screenshots/12_update_alumni.png)

### Delete Alumni

![Delete Alumni](screenshots/13_delete_alumni.png)

---

## Analytics

### Overall Statistics

![Statistics](screenshots/14_statistics.png)

### Company Statistics

![Company Statistics](screenshots/15_company_statistics.png)

### City Statistics

![City Statistics](screenshots/16_city_statistics.png)

---

## Data Import & Export

### CSV Export

![CSV Export](screenshots/17_export_csv.png)

### Excel Export

![Excel Export](screenshots/18_export_excel.png)

### CSV Import

![CSV Import](screenshots/19_import_csv.png)

---

## AI Research

### AI Research Profile

![AI Research Profile](screenshots/20_ai_research_profile.png)

---

## Health Monitoring

### Health Check

![Health Check](screenshots/21_health_check.png)

---

# 🗂️ Generated Files

The application can generate or use files such as:

```text
exports/
├── alumni.csv
└── alumni.xlsx

logs/
├── application.log
└── errors.log

uploads/
└── uploaded CSV files
```

These runtime/generated files are excluded from version control where appropriate through `.gitignore`.

---

# 🔒 Security Considerations

The project follows several basic security practices:

* Passwords are hashed before storage.
* JWT tokens are used for authenticated API access.
* Protected endpoints use authentication dependencies.
* Environment variables are used for secrets and configuration.
* `.env` is excluded from Git.
* Runtime databases and generated files are excluded where appropriate.
* API credentials should never be hardcoded into source code.

For production deployment, replace development secrets with strong randomly generated values and configure environment variables through the deployment platform.

---

# 🚀 Future Improvements

Potential improvements include:

### AI & Research

* Live web-based prospect research
* LinkedIn profile enrichment
* More advanced LLM providers
* AI-generated personalized outreach messages
* Prospect scoring
* Alumni engagement recommendations
* Automated company research
* Research result caching

### Analytics

* Interactive alumni dashboard
* More advanced company analytics
* Geographic visualizations
* Alumni career progression analysis
* Industry distribution charts
* Time-based alumni trends

### Data Management

* Bulk Excel import
* Duplicate detection
* Data validation reports
* Advanced filtering
* Bulk update/delete operations
* Import history

### Authentication

* Refresh tokens
* Password reset
* Email verification
* Role-based access control
* Admin/user permissions
* OAuth authentication

### Infrastructure

* PostgreSQL support
* Redis caching
* Docker deployment
* CI/CD pipeline
* Cloud deployment
* Production logging and monitoring

### Frontend

A dedicated frontend could be added using:

* React
* Next.js
* Vue
* Streamlit

This could provide:

* Alumni dashboard
* Search interface
* Analytics visualizations
* AI research interface
* Import/export controls
* User management

---

# 📈 Learning Outcomes

This project demonstrates practical experience with:

* REST API development
* FastAPI
* Python backend architecture
* SQLAlchemy ORM
* Relational databases
* JWT authentication
* Password hashing
* Pydantic validation
* API documentation
* Pagination
* Sorting and filtering
* Data analytics
* CSV/Excel processing
* File uploads/downloads
* AI/LLM integration
* Environment-based configuration
* Middleware and logging
* Automated testing
* Modular service architecture

---

# 🎯 Project Highlights

### Backend Engineering

Built a modular FastAPI backend with separated routers, services, models, configuration, security, and database layers.

### Data Analytics

Implemented company and city-level statistics along with structured alumni search and reporting.

### Data Engineering

Added CSV import/export and Excel export capabilities for practical data management.

### AI Integration

Implemented an extensible LLM service with configurable models and fallback behavior.

### Security

Implemented JWT-based authentication and protected API endpoints.

### API Design

Provided interactive Swagger/OpenAPI documentation for testing and exploring the API.

---

# 📄 License

This project is licensed under the terms specified in the repository's `LICENSE` file.

---

# 👩‍💻 Author

**Ashima Sharma**

Data Analyst | Python | SQL | Power BI | Tableau | FastAPI | Data Analytics

---

## ⭐ Project Purpose

This project was developed as a portfolio project to demonstrate practical backend development, data management, analytics, authentication, API design, and AI-assisted research capabilities in a real-world alumni intelligence use case.
