## flask route file ##
from flask import Flask, render_template, request
from flask_mail import Mail, Message
from forms import ContactForm

app = Flask(__name__)
app.secret_key = "YourSecretKey"

