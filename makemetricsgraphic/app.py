import dateutil.parser
from flask import Flask
from flask import render_template
import json
import csv

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('metrics.html')

if __name__ == "__main__":
	#app.run()
    #app.run(host='0.0.0.0',port=5000,debug=True)
    app.run(host='127.0.0.1',port=5000,debug=True)

