from flask import Flask, request, redirect, render_template
import cgi
import os 


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    return render_template('index.html', user_name_error='', password_error='',
            e_mail_error = '', user_name='', password='', e_mail = '')

def has_spaces(user_entry):
    if ' ' in user_entry:
        return True
    else:
        return False

def count_email_sign(email_entry, email_sign):
    count = 0
    for sign in email_entry:
        if sign == email_sign:
            count += 1
    if count == 1:
        return False
    else:
        return True

@app.route("/", methods=['POST'])
def validate_user():
    user_name = request.form['user_name']
    password = request.form['password']
    verify_pw = request.form['verify_pw']
    e_mail = request.form['e_mail']
    user_name_error = ''
    password_error = ''
    e_mail_error = ''

    if has_spaces(user_name):
        user_name_error = 'Spaces are not valid'
        user_name = ''
        
    else:
        if len(user_name) > 20 or len(user_name) < 3:
            user_name_error = 'User name out of range (3-20)'
            user_name = ''
            
    if has_spaces(password):
        password_error = 'Spaces are not valid'
        password = ''
        verify_pw = ''
    elif len(password) > 20 or len(password) < 3:
        password_error = 'Password out of range(3-20)'
        password = ''
        verify_pw = ''
    else:
        if password != verify_pw:
            password_error = 'Passwords do not match'
            password = ''
            verify_pw = ''

    if has_spaces(e_mail):
        e_mail_error = 'Spaces are not valid'
        e_mail = ''
    elif len(e_mail) > 20 or len(e_mail) < 3:
        e_mail_error = "password out of range (3-20)"
        e_mail = ''
    else:
        if count_email_sign(e_mail, ".") or count_email_sign(e_mail,"@"):
            e_mail_error = 'e_mail address must contain a single . and @ symbol.'
            e_mail = ''
                     
    if not user_name_error and not password_error and not e_mail_error:
        user_name = request.form['user_name']
        return render_template('welcome_user.html', user_name=user_name)
    else:
        return render_template('index.html', user_name_error=user_name_error, password_error=password_error,
            e_mail_error = e_mail_error, user_name=user_name, password=password, verify_pw = verify_pw, e_mail = e_mail)

app.run()
