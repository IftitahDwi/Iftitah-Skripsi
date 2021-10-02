from app.models import db

class Scrapped(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  scrapped_name= db.Column(db.String(500), unique=False, nullable=False)
  title= db.Column(db.String(500), unique=False, nullable=False)
  year= db.Column(db.String(10), unique=False, nullable=False)
  data_load_id=db.Column(db.Integer, db.ForeignKey('data_load.id', ondelete='CASCADE'))

  def __repr__(self):
     return f"Scrapped({self.id},{self.scrapped_name}, {self.data_load_id})"
    # return "<User %r>" % self.username  