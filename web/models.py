from web import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.Text, unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created = db.Column(db.Date, nullable=False, server_default=db.func.current_timestamp())
    due_date = db.Column(db.Date, default=None)
    title = db.Column(db.Text, nullable=False)
    status = db.Column(db.Text, nullable=False, default="ACTIVE")
    body = db.Column(db.Text, default=None)
    author = db.relationship('User')
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Task ID {}>'.format(self.id)

class TaskComment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    task_id = db.Column(db.Integer, db.ForeignKey('task.id', ondelete='CASCADE'), nullable=False)
    created = db.Column(db.Date, nullable=False, server_default=db.func.current_timestamp())
    content = db.Column(db.Text, nullable=False)
    task = db.relationship('Task')

    def __repr__(self):
        return '<Comment ID {}>'.format(self.id)
