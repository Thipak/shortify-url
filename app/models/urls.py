from app import db

class URL(db.Model):
    id = db.Column(db.Text(10), primary_key=True)
    url = db.Column(db.Text, unique=True, nullable=False)
