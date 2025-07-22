# UniApp FastAPI MySQL Starter

A lightweight user management system built with FastAPI backend, UniApp frontend, and MySQL database. This project provides essential user authentication and management features for modern web applications with cross-platform support.

## 🏗️ Project Structure

```
├── backend/              # FastAPI backend service
│   ├── app/
│   │   ├── api/         # API routes and endpoints
│   │   ├── core/        # Core configurations and security
│   │   ├── crud/        # Database CRUD operations
│   │   ├── db/          # Database connection and setup
│   │   ├── models/      # SQLAlchemy data models
│   │   ├── schemas/     # Pydantic schemas for validation
│   │   └── main.py      # FastAPI application entry point
│   ├── requirements.txt # Python dependencies
│   └── .env            # Environment variables
├── frontend/            # UniApp Vue3 frontend application
│   ├── src/
│   │   ├── pages/      # Application pages
│   │   ├── utils/      # Utility functions
│   │   └── main.ts     # Application entry point
│   ├── package.json    # Node.js dependencies
│   └── vite.config.ts  # Vite configuration
├── database/           # Database initialization scripts
│   └── init.sql       # Database schema and sample data
├── logs/              # Application logs
└── scripts/           # Startup and utility scripts
```

## ✨ Features

### Backend Features
- ✅ **User Management**: Registration, authentication, and user profiles

- ✅ **JWT Authentication**: Secure token-based authentication
- ✅ **Permission Control**: Role-based access control
- ✅ **Statistics API**: Dashboard metrics and analytics
- ✅ **Admin Interface**: Built-in SQLAdmin management panel
- ✅ **API Documentation**: Auto-generated OpenAPI/Swagger docs
- ✅ **Database ORM**: SQLAlchemy with async support

### Frontend Features
- ✅ **Responsive Design**: Modern UI with mobile-first approach

- ✅ **Real-time Stats**: Dynamic dashboard with live data
- ✅ **Cross-platform**: Supports H5, WeChat Mini Program, and more
- ✅ **TypeScript**: Full type safety throughout the application
- ✅ **Vue 3 Composition API**: Modern Vue.js development patterns

### Database Features
- ✅ **MySQL Integration**: Robust relational database support
- ✅ **Schema Management**: Well-structured user management tables
- ✅ **Data Relationships**: Proper indexing and constraints
- ✅ **Sample Data**: Pre-populated demo users for quick start

## 🚀 Quick Start

### Prerequisites
- Python 3.12+
- Node.js 20+
- MySQL 8.0+

### 1. Database Setup
```bash
# Create database and tables
mysql -h 127.0.0.1 -u root -p < database/init.sql
```

### 2. Backend Setup
```bash
cd backend

# Install dependencies
pip install -r requirements.txt

# Start the FastAPI server
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### 3. Frontend Setup
```bash
cd frontend

# Install dependencies
npm install

# Start development server for H5
npm run dev:h5

# Or for WeChat Mini Program
npm run dev:mp-weixin
```

### 4. Access URLs
- **Frontend Application**: http://localhost:5174/
- **API Documentation**: http://localhost:8000/docs
- **Admin Panel**: http://localhost:8000/admin/
- **Alternative API Docs**: http://localhost:8000/redoc

## 🔐 Default Credentials

**Admin Account:**
- Username: `admin`
- Password: `secret`

**Test Users:**
- alice / secret
- bob / secret  
- charlie / secret

## 📚 API Endpoints

### Authentication
```
POST /api/v1/auth/login          # User login
POST /api/v1/users/              # User registration
GET  /api/v1/users/me            # Get current user info
```



### Statistics
```
GET  /api/v1/stats/dashboard     # Get dashboard statistics
GET  /api/v1/stats/overview      # Get application overview
```

## 🗄️ Database Schema

### Users Table
| Field | Type | Description |
|-------|------|-------------|
| id | INT | Primary key |
| username | VARCHAR(50) | Unique username |
| email | VARCHAR(100) | User email address |
| password_hash | VARCHAR(255) | Hashed password |
| full_name | VARCHAR(100) | Display name |
| is_active | BOOLEAN | Account status |
| created_at | DATETIME | Creation timestamp |
| updated_at | DATETIME | Last update timestamp |



## 🛠️ Technology Stack

### Backend
- **Framework**: FastAPI 0.116.0
- **Database**: MySQL 8.0 with SQLAlchemy ORM
- **Authentication**: JWT with python-jose
- **Password**: bcrypt hashing
- **Admin**: SQLAdmin interface
- **Validation**: Pydantic v2
- **Environment**: python-dotenv

### Frontend
- **Framework**: Vue 3.4.21 with Composition API
- **Build Tool**: Vite 5.2.8
- **Language**: TypeScript 4.9.4
- **UI Framework**: UniApp 3.0
- **Cross-platform**: H5, WeChat Mini Program, Alipay Mini Program
- **HTTP Client**: Axios with request interceptors

### Development & Deployment
- **Code Quality**: ESLint, Ruff formatter
- **Type Checking**: TypeScript, Vue TSC
- **Environment**: Docker-ready configuration
- **Logging**: Structured logging with file rotation

## 🔧 Development Commands

### Backend
```bash
cd backend

# Install dependencies
pip install -r requirements.txt

# Run with hot reload
uvicorn app.main:app --reload

# Format code with Ruff
ruff format .

# Lint code
ruff check .
```

### Frontend
```bash
cd frontend

# Install dependencies
npm install

# Development (H5)
npm run dev:h5

# Development (WeChat Mini Program)
npm run dev:mp-weixin

# Build for production
npm run build

# Type checking
npm run type-check

# Lint code
npm run lint

# Lint and fix
npm run lint:fix
```

## 🌟 Key Features Explained

### Cross-Platform Support
The UniApp framework enables deployment to multiple platforms:
- **H5**: Web browsers and mobile web
- **WeChat Mini Program**: Native WeChat integration
- **Alipay Mini Program**: Alipay ecosystem support
- **Mobile Apps**: Android and iOS with uni-app build

### API-First Design
- RESTful API architecture
- OpenAPI 3.0 specification
- Automatic documentation generation
- Request/response validation
- Error handling with proper HTTP status codes

### Security Implementation
- JWT token-based authentication
- Password hashing with bcrypt
- CORS configuration for cross-origin requests
- SQL injection prevention with SQLAlchemy ORM
- Input validation with Pydantic schemas

## 📖 Usage Examples



### User Authentication
```python
# Backend authentication
from app.core.security import verify_password, create_access_token

def authenticate_user(username: str, password: str):
    user = get_user_by_username(username)
    if not user or not verify_password(password, user.password_hash):
        return False
    return user

# Generate JWT token
access_token = create_access_token(data={"sub": user.username})
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

If you encounter any issues or have questions:

1. Check the [API documentation](http://localhost:8000/docs) when running the backend
2. Review the console logs in the `logs/` directory
3. Ensure all dependencies are properly installed
4. Verify database connection settings in `backend/.env`

## 🔄 Recent Updates

- ✅ Fixed all Ruff formatting issues
- ✅ Updated repository to git@github.com:clacky-ai/uniapp-fastapi-mysql-starter.git
- ✅ Enhanced project documentation
- ✅ Improved code structure and organization

---

**Made with ❤️ using FastAPI, Vue 3, and UniApp**