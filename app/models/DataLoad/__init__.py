from app import db

class DataLoad(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  nidn= db.Column(db.String(20), unique=False, nullable=False)
  niy= db.Column(db.String(20), unique=False, nullable=False)
  load_name= db.Column(db.String(50), unique=False, nullable=False)
  gs_id= db.Column(db.String(20), unique=False, nullable=False)
  scraped= db.Column(db.Boolean(), unique=False, default=False, nullable=False)

  def __repr__(self):
     return f"User({self.id},{self.load_name}, {self.scraped})"
    # return "<User %r>" % self.username