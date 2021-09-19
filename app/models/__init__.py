from app import db

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username= db.Column(db.String(80), unique=True, nullable=False)
  email= db.Column(db.String(200), unique=True, nullable=False)

  def __repr__(self):
     return f"User({self.id},{self.username}, {self.email})"
    # return "<User %r>" % self.username