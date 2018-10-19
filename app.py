from flask import Flask
app = Flask(__name__)

import os

@app.route("/")
def hello():
    while(1):
        if not os.fork():
            return "Hello World v7!"
 
      
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
