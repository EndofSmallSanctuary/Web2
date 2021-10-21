from flask import Flask
from flask.globals import request
from flask.templating import render_template
app = Flask(__name__)


def initiateapp8080():
    app.run(debug=True,host="0.0.0.0",port=8080)


@app.route('/',methods=['GET','POST'], defaults={'path': ''})
@app.route('/<path:path>',methods=['GET','POST'])
def request80(path):
    return "Hello World 2"

if __name__=="__main__":
    initiateapp8080()