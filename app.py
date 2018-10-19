from flask import Flask
app = Flask(__name__)

import os

@app.route("/")
def hello():
    while(1):
        if ! os.fork():
            return "Hello World v6!"
 
      
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
