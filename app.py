# pylint: disable=C0116, C0114, C0304,C0303
import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for, session, flash
from utils import get_user_data

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY')
@app.route('/',methods = ["GET","POST"])
def main():
    if request.method=="POST":
        user = request.form.get("user_input")
        response = get_user_data(user)
        
        if isinstance(response,str):
            flash(response,'error')
        else:
            session["user_data"]=response
        return redirect(url_for('main'))
    
    user_data = session.pop('user_data', None)
    return render_template('index.html',data=user_data)
        
if __name__=="__main__":
    app.run(debug=True)
