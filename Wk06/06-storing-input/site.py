from flask import Flask, render_template

app = Flask(__name__)

app.config['SECRET_KEY'] = 'important to keep unknown in production'

from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired




class MyForm(Form):
	name = StringField('first name', validators=[DataRequired()])
	name1 = StringField('last name', validators=[DataRequired()])
	

from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class Visitor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    name1 = db.Column(db.String(80))


    def __init__(self, name, name1):
        self.name = name
        self.name1 = name1


    def __repr__(self):
        return '<Visitor %r, %r>' % self.name, self.name1
	
	
db.create_all()
	
@app.route('/', methods=('GET', 'POST'))
def index():
	form = MyForm(text='first name')
	previous_visitors = Visitor.query.order_by('id DESC').all()
	if form.validate_on_submit():
		name = form.name.data
		name1 = form.name1.data
		db.session.add(Visitor(name, name1))
		db.session.commit()
	else:
		name = 'Doctor'
		name1 = 'Strange'
	return render_template('index.html', form=form, name=name, name1=name1, previous_visitors=previous_visitors)
	
@app.route('/custom/<custom>/')
def custom(custom):
	return render_template('custom.html', custom=custom)
	
if __name__ == '__main__':
	app.run(debug=True)