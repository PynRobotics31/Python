from flask import Flask
import requests as rq
try:
    
    code = rq.get("https://google.com").text
    app = Flask(__name__)
    @app.route("/")
    def home():
        return code
    if __name__=="__main__":
        app.run(debug=True)
except:
    print("server error")