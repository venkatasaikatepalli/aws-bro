from flask import Flask
from aws.s3_manager import list_buckets

__author__ = "Venkata.Sai.Kateppalli<venkatasai.k@codejukers.in>"
__version__ = "1.0"

app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome to aws bro"

@app.route("/buckets")
def buckets():
    return list_buckets()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)