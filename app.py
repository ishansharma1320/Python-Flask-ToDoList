from flask import Flask, render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todolist.db'

db = SQLAlchemy(app)

class ToDoListModel(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    content = db.Column(db.String(200),nullable=False)
    date_created = db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__():
        return f'Task Created {id}';

@app.route('/',methods=['GET','POST'])
def getToDoList():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = ToDoListModel(content=task_content)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'Saving failed'
    else:
        tasks = ToDoListModel.query.order_by(ToDoListModel.date_created).all()
        return render_template('home.html',tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)