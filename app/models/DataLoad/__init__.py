from app.models import db
from app.models import Scrapped

class DataLoad(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  nidn= db.Column(db.String(20), unique=False, nullable=False)
  niy= db.Column(db.String(20), unique=False, nullable=False)
  load_name= db.Column(db.String(100), unique=False, nullable=False)
  gs_id= db.Column(db.String(20), unique=False, nullable=False)
  is_scraped= db.Column(db.Boolean(), unique=False, server_default="0", default=False, nullable=False)
  scraped= db.relationship('Scrapped', backref='data_load', passive_deletes=True)

  # def __init__(self):
  #   pass
  # def _asdict(self):
  #       return {c.key: getattr(self, c.key)
  #               for c in inspect(self).mapper.column_attrs}

  # def __repr__(self):
  #   return f"{c.key: getattr(self, c.key) for c in db.inspect(self).mapper.column_attrs}"
  #    return f"DataLoad({self.id},{self.load_name}, {self.is_scraped})"
  #   # return "<User %r>" % self.username