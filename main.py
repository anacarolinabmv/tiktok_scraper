# pylint: disable=C0116, C0114, C0304,C0303
from flask import Flask, request,render_template,jsonify

app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def index():
    if request.method=="POST":
        user = request.form["user_input"]
        print(user)
    
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)
