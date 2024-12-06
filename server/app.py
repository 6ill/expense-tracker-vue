from src import app
import os

if __name__ == "__main__":
    app.run(host= os.environ.get('HOST'),
            port= os.environ.get('PORT'),
            debug= True)