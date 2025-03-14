# Expense Tracker Application

A full-stack expense tracking application built with Vue.js and Flask.

## Backend Setup (Server)

1. Create and activate virtual environment:
```bash
cd server
python -m venv venv
source venv/bin/activate  # For Unix/MacOS
venv\Scripts\activate     # For Windows
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create `.env` file:
```bash
cp .env.example .env
```

4. Configure your database settings in `.env`

5. Create database tables:
```bash
python create_db.py
```

6. Run the server:
```bash
python app.py
```

The backend will be available at `http://localhost:5000`

## Frontend Setup (Client)

1. Install dependencies:
```bash
cd client
npm install
```

2. Run development server:
```bash
npm run dev
```

3. Build for production:
```bash
npm run build
```

The frontend will be available at `http://localhost:3000`

## Features

- User authentication (login/register)
- Track expenses by categories
- Set budget limits for different categories
- View expense history
- Edit and delete transactions
- Real-time budget tracking

## API Endpoints

### Authentication
- POST `/users/register` - Register new user
- POST `/users/login` - Login user
- POST `/users/logout` - Logout user

### Transactions
- GET `/transactions/category/<category_name>` - Get transactions by category
- POST `/transactions/` - Create new transaction
- PUT `/transactions/<transaction_id>` - Update transaction
- DELETE `/transactions/<transaction_id>` - Delete transaction

### Budget Limits
- GET `/limits/` - Get budget limits
- PUT `/limits/` - Update budget limits

## Tech Stack

### Frontend
- Vue.js 3
- Vue Router
- Tailwind CSS
- Axios

### Backend
- Flask
- SQLAlchemy
- MySQL
- Flask-CORS

## Requirements

- Python 3.8+
- Node.js 16+
- MySQL

## License

MIT License
