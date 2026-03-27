from flask import Flask, render_template, request
from pymongo import MongoClient
import certifi
import os

app = Flask(__name__)



# Use environment variable for MongoDB URI
# MONGO_URI = os.environ.get("MONGO_URI")

# client = MongoClient(
#     MONGO_URI,
#     tlsCAFile=certifi.where()
# )
MONGO_URI = os.environ.get("MONGO_URI", "mongodb+srv://admin:Demo123@cluster0.9hitnm3.mongodb.net/?retryWrites=true&w=majority")
client = pymongo.MongoClient(MONGO_URI)
# client = MongoClient(
#     "mongodb+srv://admin:Demo123@cluster0.9hitnm3.mongodb.net/?retryWrites=true&w=majority",
#     tlsCAFile=certifi.where()
# )
db = client["client_demo"]
collection = db["sum_data"]

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        result = num1 + num2

        collection.insert_one({
            "num1": num1,
            "num2": num2,
            "sum": result
        })

    data = list(collection.find().sort("_id", -1))
    return render_template('index.html', result=result, data=data)

if __name__ == '__main__':
    app.run(debug=True)