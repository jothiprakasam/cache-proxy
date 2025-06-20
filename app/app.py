from flask import Flask
import time

app = Flask(__name__)

@app.route("/api/data")
def get_data():
    time.sleep(2)  # Simulate slow backend
    return {"data": "This is cached data!"}
