from src import app, db

def create_database():
    """
    Membuat semua database yang tercantum dalam src/models
    """
    with app.app_context():
        try:
            db.create_all()
            print("Database tables created successfully.")
        except Exception as e:
            print(f"Error creating database tables: {e}")

if __name__ == "__main__":
    create_database()
