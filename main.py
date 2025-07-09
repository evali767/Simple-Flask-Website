from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm
from flask_behind_proxy import FlaskBehindProxy
from dotenv import load_dotenv 
import os  

load_dotenv()
app = Flask(__name__)
# this line handles re-directs in codio
proxied = FlaskBehindProxy(app)

# app.config['SECRET_KEY'] =  os.getenv('SECRET_KEY')
app.config['SECRET_KEY'] = '761028b2083b5b00fdf652c2423729a1'
 
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', subtitle='Home Page', text='This is the home page')

@app.route("/second_page")
def second_page():
    return render_template('second_page.html', subtitle='Second Page', text='This is the second page')

# form
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit(): # checks if entries are valid
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home')) # if so - send to home page
    return render_template('register.html', title='Register', form=form)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")