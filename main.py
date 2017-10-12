from flask import Flask, request, redirect, render_template
import cgi
import os 


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    return render_template('index.html', name_range_error='', name_space_error = '', pw_space_error='', pw_match_error='', pw_range_error='',
            email_space_error = '', email_range_error='', email_sign_error='', user_name='', password='', e_mail = '')

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

def test_email_entry(email_entry):
    if email_entry == '':
        return False
    else:
        return True

@app.route("/", methods=['POST'])
def validate_user():
    user_name = request.form['user_name']
    password = request.form['password']
    verify_pw = request.form['verify_pw']
    e_mail = request.form['e_mail']
    name_space_error = ''
    name_range_error = ''
    pw_range_error = ''
    pw_match_error = ''
    pw_space_error = ''
    email_space_error=''
    email_range_error=''
    email_sign_error=''
    
    if has_spaces(user_name):
        name_space_error = 'Spaces are not valid'
    if len(user_name) > 20 or len(user_name) < 3:
        name_range_error = 'User name out of range (3-20)'
        
       
    if len(password) > 20 or len(password) < 3:
        pw_range_error = 'Password out of range(3-20)'
    if password != verify_pw:
        pw_match_error = 'Passwords do not match'
    if has_spaces(password):
        pw_space_error = 'Spaces are not valid'

    if test_email_entry(e_mail):
        if has_spaces(e_mail):
            email_space_error = 'Spaces are not valid'
        if len(e_mail) > 20 or len(e_mail) < 3:
            email_range_error = "password out of range (3-20)"
        if count_email_sign(e_mail, ".") or count_email_sign(e_mail,"@"):
            email_sign_error = 'e_mail address must contain a single . and @ symbol.'
    else:
        e_mail = e_mail
    

    if pw_range_error or pw_space_error or pw_match_error or email_range_error or email_sign_error or email_space_error or name_range_error or name_space_error:
        password = ''
        verify_pw = ''  
       

         
    if not name_space_error and not name_range_error and not pw_match_error and not pw_space_error and not pw_range_error and not email_sign_error and not email_range_error and not email_space_error:
        user_name = request.form['user_name']
        return render_template('welcome_user.html', user_name=user_name)
    else:
        return render_template('index.html', name_space_error=name_space_error, name_range_error=name_range_error, pw_space_error= pw_space_error, pw_match_error=pw_match_error, pw_range_error=pw_range_error,
            email_space_error=email_space_error, email_range_error= email_range_error, email_sign_error= email_sign_error, user_name=user_name, password=password, verify_pw = verify_pw, e_mail = e_mail)

app.run()
