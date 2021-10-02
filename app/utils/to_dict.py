from app.models import db

def object_as_dict(list_obj):
    dict_list = []
    for obj in list_obj:
      newDict = {c.key: getattr(obj, c.key) for c in db.inspect(obj).mapper.column_attrs}
      dict_list.append(newDict)
    return dict_list