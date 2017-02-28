from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, validators

## chcek name length function
def CheckNameLength(form, field):
  if len(field.data) < 4:
    raise ValidationError('Name must be more then 3 characters')
## Contact Form Class
class ContactForm(FlaskForm):
  name = StringField('Your Name:', [validators.DataRequired(), CheckNameLength])
  email = StringField('Your email Address:', [validators.DataRequired(), validators.Email('your@email.com')])
  message = TextAreaField('Your Message:', [validators.DataRequired()])
  submit = SubmitField('Send Message')
  
  
