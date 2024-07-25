# pylint: disable=C0116, C0114, C0304,C0303
from flask import Flask, request,render_template,jsonify

app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def index():
    if request.method=="POST":
        pass
    
    return render_template('index.html')