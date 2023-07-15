from flask import Flask
from views import views
app=Flask(__name__)

@app.route("/")
app.register_blueprint(views,url_prefix="/")

def home():
    return "home page"
if __name__=='__main__':
    app.run(debug=True,port=8000)

