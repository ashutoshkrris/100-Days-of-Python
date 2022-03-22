from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

# connect to the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500), nullable=False)
    done = db.Column(db.Boolean, nullable=False)


class NewTodo(FlaskForm):
    todo = StringField('Todo', validators=[DataRequired()])
    submit = SubmitField('Add')


@app.route('/', methods=['GET', 'POST'])
def home():
    todo_list = db.session.query(Todo).all()
    form = NewTodo()
    if form.validate_on_submit():
        new_todo = Todo(name=form.todo.data,
                        done=False)
        db.session.add(new_todo)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('index.html', todo_list=todo_list, form=form)


@app.route('/delete', methods=['GET', 'DELETE'])
def delete():
    todo_id = request.args.get('id')
    selected_todo = Todo.query.get(todo_id)
    db.session.delete(selected_todo)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/check', methods=['GET', 'PATCH'])
def check():
    todo_id = request.args.get('id')
    selected_todo = Todo.query.get(todo_id)
    selected_todo.done = not selected_todo.done
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
