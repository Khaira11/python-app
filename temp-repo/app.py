from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    'DATABASE_URL', 'postgresql://app_user:password@db:5432/mydb'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#class Entry(db.Model):
 #   id = db.Column(db.Integer, primary_key=True)
  #  name = db.Column(db.String(100), nullable=False)
class Entry(db.Model):
    __tablename__ = 'entries'  # optional but recommended

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)



with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        db.session.add(Entry(name=request.form['name'], address=request.form['address']))
        db.session.commit()
        return redirect('/')
    return render_template('index.html')

@app.route('/view', methods=['GET'])
def view():
    entries = Entry.query.order_by(Entry.id).all()
    return render_template('records.html', entries=entries)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

