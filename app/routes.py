from flask import render_template, request, flash, send_from_directory
from app import app, mail
from app.forms import ContactForm
from flask_mail import Message

# view function
@app.route('/')
@app.route('/index') # 'decorator'
def index():
    # render_template is a Flask function which turns a template into a full html page
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if request.method == 'POST':
        if form.validate == False:
            flash('All fields are required.')
            return render_template('contact.html', form=form)
        else:
            msg = Message(form.subject.data, sender='contact@example.com', recipients=['lyssogor@gmail.com'])
            msg.body = """
            From: %s <%s>
            %s
            """ % (form.name.data, form.email.data, form.message.data)
            mail.send(msg)

            return render_template('email_success.html')

    elif request.method == 'GET':
        return render_template('contact.html', form=form)

@app.route('/email_success')
def email_success():
    return render_template('email_success.html')

@app.route('/algo_intro')
def algo_intro():
    return render_template('algo_intro.html')