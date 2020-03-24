from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from mail import *

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]///'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return 'Task %r' % self.id


@app.route('/', methods=['POST','GET'])
def index():
    error = None
    if request.method =='POST':
        online_content = request.form['content']
        # prevent empty entries
        if online_content == '':
            error = True
            flash('WHAT')
            return redirect('/')
        to_db = Data(content=online_content)

        try:
            db.session.add(to_db)
            db.session.commit()
            send_email(subject,body)

            return redirect('/')
        except:
            return 'Could not add data to database'
    else:
        rows = Data.query.order_by(Data.date_created).all()
        return render_template('index.html', rows=rows, error=error)

@app.route('/delete/<int:id>')
def delete(id):
    to_delete = Data.query.get_or_404(id)

    try:
        db.session.delete(to_delete)
        db.session.commit()
        return redirect("/")
    except:
        return 'Could not delete'

@app.route('/update/<int:id>', methods=['POST', 'GET'])
def update(id):
    post = Data.query.get_or_404(id)
    
    if request.method =='POST':
        post.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'could not update'
    else:    
        return render_template('update.html', post=post )

if __name__ == "__main__":
    app.run(debug=True)