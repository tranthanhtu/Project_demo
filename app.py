from flask import Flask,render_template
import mongoengine
from mongoengine import Document, StringField, IntField
host = "ds021462.mlab.com"
port = 21462
db_name = "tranthanhtu"
user_name = "tranthanhtu"
password = "anhyeuem221190"
mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)
app = Flask(__name__)
class Project(Document):
    title = StringField()
    img =StringField()

@app.route("/<path:path>")
def static_file(path):
    return app.send_static_file(path)

@app.route('/')
def hello_world():
    return render_template("index.html",tennis_list = Project.objects)

if __name__ == '__main__':
    app.run()
